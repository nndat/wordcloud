# task running
from wordcloud import WordCloud
from crawler import Crawler
from datetime import datetime


def to_wordcloud(text, filepath):
    wordcloud = WordCloud().generate(text)
    wordcloud.to_file(filepath)


def to_stogare(filepath):
    pass


def to_db(filepath, label):
    pass


def _get_filepath(label, ext="png"):
    now = datetime.now()
    time_str = now.strftime("%Y%m%d%H")
    return f"stogare/{label}_{time_str}.{ext}"


if __name__ == "__main__":
    # text = newpapers.get_trending_text()
    # text = "new new 123 zo 242"
    # to_wordcloud(text)
    crawler = Crawler()
    for trend in crawler.get_trending_text():
        label = trend['label']
        text = trend['text']
        filepath = _get_filepath(label)
        to_wordcloud(text, filepath)
        print(label)
