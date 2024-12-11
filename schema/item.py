from typing import TypedDict


class Item(TypedDict):
    type: str
    domain: str
    title: str
    link: str
    date: str
    content: str
