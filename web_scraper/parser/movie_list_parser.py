import datetime
import re

from schema.item import Item
from utils.url_utils import get_last_level
from web_scraper.parser.base_parser import BaseParser


class MovieListParser(BaseParser):

    def __init__(self, url):
        super().__init__(url)
        self.base_url = get_last_level(url)

    def parse(self, html) -> list[Item]:
        threads = html.find_all("li", class_=re.compile(r"^threadbit"))
        items = []
        for thread in threads:
            thread_title = thread.find_all("h3", class_="threadtitle")[0].a
            if thread_title.text in (
                "Trailer Requests",
                "Filled Requests",
                "Please Read Before Posting",
                "Blu-ray, DVD Trailers and More (Anything Blu-ray & DVD Related)",
            ):
                continue
            thread_date = self.get_date(thread)
            item = {
                "title": f"{thread_title.text} [{thread_date}]",
                "link": f"{self.base_url}/{thread_title['href']}",
                "date": thread_date,
                "content": "",
            }
            items.append(item)

        return items

    @staticmethod
    def get_date(thread) -> str:
        """
        'Today, 09:34 AM' -> '08-19-2024, 09:34 AM'
        'Yesterday, 09:34 AM' -> '08-18-2024, 09:34 AM'
        """
        displayed_date = (
            thread.find_all("dl", class_="threadlastpost td")[0]
            .find_all("dd")[1]
            .text[:-2]
        )
        if displayed_date[:5] == "Today":
            today_date = (
                datetime.datetime.now() - datetime.timedelta(hours=7)
            ).strftime("%m-%d-%Y")
            return f"{today_date}{displayed_date[5:]}"
        elif displayed_date[:9] == "Yesterday":
            yesterday_date = (
                datetime.datetime.now()
                - datetime.timedelta(hours=7)
                - datetime.timedelta(days=1)
            ).strftime("%m-%d-%Y")
            return f"{yesterday_date}{displayed_date[9:]}"
        else:
            return displayed_date
