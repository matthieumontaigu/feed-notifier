from schema.item import Item
from utils.date_utils import get_now_date
from web_scraper.parser.base_parser import BaseParser


class DigitalDigestParser(BaseParser):

    def __init__(self, url):
        super().__init__(url)

    def parse(self, html) -> list[Item]:
        tds = html.find_all("td", class_="smallText")
        items = []
        for td in tds:
            a_tags = td.find_all("a")
            for a_tag in a_tags:
                if a_tag.text and len(a_tag.text) > 15:
                    item = {
                        "title": a_tag.text,
                        "link": a_tag["href"],
                        "date": get_now_date(),
                        "content": "",
                    }
                    items.append(item)
        return items
