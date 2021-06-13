# task running
from wordcloud import WordCloud
from datetime import datetime

from crawler import Crawler
from db import get_session
from db.models import WordCloud as WCModel


def to_wordcloud(text, filepath):
    wordcloud = WordCloud().generate(text)
    wordcloud.to_file(filepath)


def to_stogare(filepath):
    pass


def to_db(filepath, label, content):
    session = get_session()
    wc = WCModel(file_path=filepath, label=label, content=content)
    session.add(wc)
    session.commit()


def _get_filepath(label, ext="png"):
    now = datetime.now()
    time_str = now.strftime("%Y%m%d%H")
    return f"stogare/{label}_{time_str}.{ext}"


def crawle():
    crawler = Crawler()
    for trend in crawler.get_trending_text():
        label = trend['label']
        text = trend['text']
        filepath = _get_filepath(label)
        to_wordcloud(text, filepath)
        to_db(filepath, label, text)
        print(label)


if __name__ == "__main__":
    crawle()
