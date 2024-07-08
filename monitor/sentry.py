from collections import Counter

from sentinel.db.contract.abi.static import ABI_EVENT_TRANSFER
from sentinel.definitions import BLOCKCHAIN
from sentinel.models.config import Configuration
from sentinel.models.event import Blockchain, Event
from sentinel.models.transaction import Transaction
from sentinel.sentry.v2.transaction import TransactionDetector
from sentinel.utils.transaction import filter_events


class TransferMonitor(TransactionDetector):
    name = "TransferMonitor"
    description = """The monitor checks transfers via monitored contract 
                     and notify if there are value higher then predefined threshold"""

    def init(self):
        super().init()

        self.databases.monitoring_conditions.ingest()
        if len(self.databases.monitoring_conditions.addresses) == 0:
            self.logger.warning("No monitored addresses detected")

        if getattr(self.inputs, "config", None):
            self.inputs.config.on_config_change = self.on_config_change

        self.log_metrics = Counter()

    async def on_config_change(self, record: Configuration):
        self.databases.monitoring_conditions.update(record)

    async def on_transaction(self, transaction: Transaction) -> None:
        # Log Metrics help to monitor detector processing/progress via metrics in log messages
        # - total transactions
        # - the number of transfers to/from monitored contract
        # - the number of cases when threshold exceed
        self.log_metrics["total transactions"] += 1
        if self.log_metrics["total transactions"] % 100 == 0:
            self.logger.info(self.log_metrics)

        # For each transaction, we are checking if there is ERC20 TRANSFER event and
        # if yes, we can check a value with threshold
        for event in filter_events(transaction.logs, [ABI_EVENT_TRANSFER]):
            # Since we can have many monitored addresses, we need to check all of them
            for monitored_address in self.databases.monitoring_conditions.addresses:
                monitored_address = monitored_address.lower()

                # Skip processing if no monitored address founded in TRANSFER event
                if monitored_address != event.address:
                    continue

                # Increase metrics for further investigation/throbleshooting
                self.log_metrics["transfer to/from monitored contract"] += 1

                # The Exatractor can have several different monitored configurations
                # for the same monitored address, so we need to check all of them
                for (
                    config
                ) in self.databases.monitoring_conditions.get_address_conditions(
                    address=monitored_address
                ):
                    config_id = config.id
                    monitoring_config = config.config
                    value = event.fields.get("value", 0)
                    threshold = monitoring_config.get("threshold")

                    # If Transfer value is greater or equal to the threshold, we need to send notification
                    if value >= threshold:
                        self.log_metrics["threshold exceed"] += 1
                        await self.send_notification(
                            config_id=config_id,
                            monitored_address=monitored_address,
                            sender_address=event.fields.get("from", ""),
                            recipient_address=event.fields.get("to", ""),
                            threshold=threshold,
                            amount=value,
                            transaction=transaction,
                        )

    async def send_notification(
        self,
        config_id: int,
        monitored_address: str,
        threshold: int,
        sender_address: str,
        recipient_address: str,
        amount: int,
        transaction: Transaction,
    ) -> None:
        network = self.parameters.get("network")
        event = Event(
            did=self.name,
            sid="ext:sentinel",
            cid=config_id,
            type="transfer_amount_threshold_exceed",
            severity=0.3,
            ts=transaction.block.timestamp,
            blockchain=Blockchain(
                network=network,
                chain_id=str(BLOCKCHAIN.get(network).chain_id),
            ),
            metadata={
                "tx_hash": transaction.hash,
                "tx_from": transaction.from_address,
                "tx_to": transaction.to_address,
                "monitored_contract": monitored_address,
                "sender_address": sender_address,
                "recipient_address": recipient_address,
                "value": amount,
                "threshold": threshold,
                "desc": "Transfer detected with a value exceeding the threshold",
            },
        )
        await self.outputs.events.send(event)
