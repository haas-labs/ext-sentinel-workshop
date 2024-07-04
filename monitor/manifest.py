from pydantic import Field
from sentinel.manifest import BaseSchema, MetadataModel, NetworkTag, Status


class Schema(BaseSchema):
    threshold: float = Field(title="Threshold", description="Threshold Amount")


metadata = MetadataModel(
    name="Contract Monitor",
    version="0.1.0",
    status=Status.ACTIVE,
    description=" ".join(
        [
            "The Contract Detector tracks transfer transactions towards monitored contracts ",
            "and notify the Extractor if amount exceed",
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
