from aws.email_sender import AWSEmailSender
from aws.sms_sender import AWSSMSSender


def get_sender(
    message_type: str, aws_credentials: dict[str, str]
) -> AWSEmailSender | AWSSMSSender:
    if message_type == "sms":
        return AWSSMSSender(**aws_credentials)
    elif message_type == "email":
        return AWSEmailSender(**aws_credentials)
    else:
        raise ValueError(f"Unsupported message_type {message_type}.")
