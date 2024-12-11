import requests
from bs4 import BeautifulSoup
from requests.exceptions import ChunkedEncodingError, ConnectionError
from schema.item import Item
from web_scraper.base_web_scraper import BaseWebScraper
from web_scraper.parser.parser_factory import get_parser


class HTMLWebScraper(BaseWebScraper):

    def __init__(self, url):
        super().__init__(url)
        self.parser = get_parser(url)

    def get(self) -> list[Item]:
        try:
            response = requests.get(self.url)
        except (ChunkedEncodingError, ConnectionError) as e:
            print(f"Will skip {self.url} because of {e}")
            return []
        html = BeautifulSoup(response.text, "html.parser")
        items = self.parser.parse(html)
        return items
