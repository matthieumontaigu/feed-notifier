from schema.item import Item
from utils.date_utils import get_now_date
from web_scraper.parser.base_parser import BaseParser


class TheDigitalTheaterParser(BaseParser):

    def __init__(self, url):
        super().__init__(url)

    def parse(self, html) -> list[Item]:
        elements = self.get_elements(html)
        items = [
            {
                "title": element.text,
                "link": element["href"],
                "date": get_now_date(),
                "content": "",
            }
            for element in elements
        ]
        return items

    def get_elements(self, html):
        if "user-uploaded-trailers" in self.url:
            return html.find_all("a", class_="bbp-topic-permalink")
        return [h2.a for h2 in html.find_all("h2", class_="entry-title")]
