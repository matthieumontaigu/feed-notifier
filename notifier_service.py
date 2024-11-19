import time


class NotifierService(object):

    def __init__(
        self,
        sources: dict[str, dict[str, str]],
        message_type: str,
        aws_credentials: dict[str, str],
        execution_interval: int = 60,
    ):
        self.sources = sources
        self.message_type = message_type
        self.aws_credentials = aws_credentials
        self.execution_interval = execution_interval

    def start(self):
        self.send_message("RSS reader started.")
        try:
            while True:
                self.handle()
                self.sleep()
        except Exception as e:
            self.process_error(e)

    def handle(self):
        for site_name, site_params in self.sources.items():
            self.fetch_new_items(site_name, site_params)

        if time.time() - self.last_csv_written_time > self.csv_write_frequency_seconds:
            self.read_items_df.to_csv(self.read_items_path, sep="|", index=False)
            self.last_csv_written_time = time.time()

    def sleep(self):
        time.sleep(self.execution_interval)

    def process_error(exception): ...
