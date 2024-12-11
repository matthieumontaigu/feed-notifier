import datetime


def get_now_date() -> str:
    return datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S") + " +0000"
