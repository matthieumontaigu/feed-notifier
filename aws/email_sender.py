from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import boto3
from aws.base_sender import BaseSender


class AWSEmailSender(BaseSender):

    def __init__(
        self, region_name: str, aws_access_key_id: str, aws_secret_access_key: str
    ) -> None:
        self.ses = boto3.client(
            "ses",
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

    def send(self, source: str, destination: str, subject: str, message: str) -> None:
        mail_message = MIMEMultipart("mixed")

        mail_message["From"] = source
        mail_message["To"] = destination
        mail_message["Subject"] = subject

        body_text = message
        body_html = message
        textpart = MIMEText(body_text.encode("utf-8"), "plain", "utf-8")
        htmlpart = MIMEText(body_html.encode("utf-8"), "html", "utf-8")

        mail_body = MIMEMultipart("alternative")
        mail_body.attach(textpart)
        mail_body.attach(htmlpart)
        mail_message.attach(mail_body)

        self.ses.send_raw_email(
            Source=source,
            Destinations=[],
            RawMessage={
                "Data": mail_message.as_string(),
            },
        )
