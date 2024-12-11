import argparse

from services.notifier_service import NotifierService
from utils.config_utils import load_config


def main():
    parser = argparse.ArgumentParser(description="Start feed notifier")
    parser.add_argument("--config-path", help="Location of the config file")

    args = parser.parse_args()
    config = load_config(args.config_path)
    feeds_config = config["feeds"]
    message_sender_config = config["message_sender"]
    memory_manager_config = config["memory_manager"]
    execution_interval = config["execution_interval"]

    notifier_service = NotifierService(
        feeds_config, message_sender_config, memory_manager_config, execution_interval
    )
    notifier_service.start()


if __name__ == "__main__":
    main()
