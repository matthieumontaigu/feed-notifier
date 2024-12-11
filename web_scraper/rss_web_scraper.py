import feedparser
from schema.item import Item
from web_scraper.base_web_scraper import BaseWebScraper


class RSSWebScraper(BaseWebScraper):

    def __init__(self, url):
        super().__init__(url)

    def get(self) -> list[Item]:
        parsed_feed = feedparser.parse(self.url)
        items = [
            {
                "title": item.title,
                "link": item.link,
                "date": item.published,
                "content": item.summary,
            }
            for item in parsed_feed.entries
        ]
        return items
