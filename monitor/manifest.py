from pydantic import Field
from sentinel.manifest import BaseSchema, MetadataModel, NetworkTag, Status


class Schema(BaseSchema):
    threshold: float = Field(title="Threshold", description="Threshold Amount")


metadata = MetadataModel(
    name="Transfer Monitor",
    version="0.1.2",
    status=Status.ACTIVE,
    description=" ".join(
        [
            "The Transfer Monitor tracks transfers via monitored contracts ",
            "and notify the Extractor if amount exceed predefined threshold",
        ]
    ),
    tags=[
        NetworkTag.EVM,
    ],
    faq=[
        {
            "name": "How to define a threshold?",
            "value": " ".join(
                [
                    "To define a threshold, specify the transfer amount that will trigger an alert. ",
                    "This should be in integer format, for example, 1000000",
                ]
            ),
        },
    ],
)
