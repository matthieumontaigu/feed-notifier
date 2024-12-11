import boto3
from aws.base_sender import BaseSender


class AWSSMSSender(BaseSender):

    def __init__(
        self, region_name: str, aws_access_key_id: str, aws_secret_access_key: str
    ) -> None:
        self.sns = boto3.client(
            "sns",
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

    def send(self, source: str, destination: str, subject: str, message: str) -> None:
        self.sns.publish(
            PhoneNumber=destination,
            Message=message,
            MessageAttributes={
                "AWS.SNS.SMS.SenderID": {
                    "DataType": "String",
                    "StringValue": source,
                }
            },
        )
