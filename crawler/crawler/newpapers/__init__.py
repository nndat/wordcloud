import requests
from bs4 import BeautifulSoup as BS


class Newspaper:
    url = None
    label = None

    def get_trending_text(self):
        news = self._get_soup()
        return self._parse_news(news)

    def _get_soup(self, url=None, parser="html.parser"):
        if not url:
            url = self.url

        news = requests.get(url)
        return BS(news.text, parser)

    def _parse_news(self, news):
        raise NotImplemented()


class TuoiTreNews(Newspaper):
    url = "https://tuoitre.vn/tin-moi-nhat.htm"
    label = "TuoiTreNews"

    def _parse_news(self, news):
        titles = news.find_all('h3', attrs={'class': 'title-news'})
        links = [item.find('a').attrs['href'] for item in titles]
        tt_tags = []
        for link in links:
            url = ''.join(['https://tuoitre.vn', link])
            soup = self._get_soup(url)
            li_tags = soup.find_all('li', attrs={'class': 'tags-item'})
            try:
                # truong hop tim thay mot list cac hashtag
                tags = [tag.text for tag in li_tags]
            except TypeError:
                # truong hop chi tra ve 1 hashtag
                tags = [li_tags.text]
            
            tt_tags += tags
        tt_tags = [tag.replace(' ', '') for tag in tt_tags]
        tt_htags = ' '.join(tt_tags)
        return tt_htags


class ThanhNienNews(Newspaper):
    url = "https://thanhnien.vn/tin-24h.html"
    label = "ThanhNienNews"

    def _parse_news(self, news):
        tn_hashtags = [hashtag.text for hashtag in news.find_all('a', attrs={'class': 'hashtag'})]
        tn_hashtags = [htag.replace(' ', '') for htag in tn_hashtags]
        tn_hashtags = ' '.join(tn_hashtags)
        return tn_hashtags


class NewsCrawler:
    label = "VnNewspaper"
    newspapers = [ThanhNienNews, TuoiTreNews]

    def get_trending_text(self):
        trends_text = ""
        for papers in self.newspapers:
            crawler = papers()
            trends_text += crawler.get_trending_text()
        return trends_text


if __name__ == '__main__':
    crawler = NewsCrawler()
    trends = crawler.get_trending_text()
    print(trends)
