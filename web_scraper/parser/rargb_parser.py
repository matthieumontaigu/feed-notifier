from schema.item import Item
from utils.date_utils import get_now_date
from utils.url_utils import get_domain
from web_scraper.parser.base_parser import BaseParser


class RARGBParser(BaseParser):

    def __init__(self, url):
        super().__init__(url)
        self.base_url = get_domain(url)

    def parse(self, html) -> list[Item]:
        trs = html.find_all("tr", class_="lista2")
        tds = [item.find_all("td")[1] for item in trs]
        items = [
            {
                "title": td.a.text,
                "link": f"{self.base_url}{td.a['href']}",
                "date": get_now_date(),
                "content": "",
            }
            for td in tds
        ]
        return items
