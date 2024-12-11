from web_scraper.html_web_scraper import HTMLWebScraper
from web_scraper.rss_web_scraper import RSSWebScraper


def get_web_scraper(scraper_type: str, url: str):
    if scraper_type == "html":
        return HTMLWebScraper(url)
    elif scraper_type == "rss":
        return RSSWebScraper(url)
    else:
        raise ValueError(f"Unsupported scraper_type {scraper_type}.")
