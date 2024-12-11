from web_scraper.parser.digital_digest_parser import DigitalDigestParser
from web_scraper.parser.digital_theater_parser import TheDigitalTheaterParser
from web_scraper.parser.movie_list_parser import MovieListParser
from web_scraper.parser.rargb_parser import RARGBParser


def get_parser(url):
    if "movie-list" in url:
        return MovieListParser(url)
    elif "digital-digest" in url:
        return DigitalDigestParser(url)
    elif "thedigitaltheater" in url:
        return TheDigitalTheaterParser(url)
    elif "rargb" in url:
        return RARGBParser(url)
    else:
        raise ValueError(f"No parser implemented for {url}")
