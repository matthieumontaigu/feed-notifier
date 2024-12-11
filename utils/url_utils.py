from urllib.parse import urlparse


def extract_netloc(url):
    return urlparse(url).netloc


def get_domain(url: str) -> str:
    """
    https://google.com/search/level1/level2 -> https://google.com
    """
    return url.split("//")[0] + "//" + url.split("//")[1].split("/")[0]


def get_last_level(url: str) -> str:
    """
    https://google.com/search/level1 -> https://google.com/search
    """
    return url.rpartition("/")[0]
