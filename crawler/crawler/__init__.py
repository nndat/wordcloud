from .newpapers import NewsCrawler, TuoiTreNews, ThanhNienNews


class Crawler:
    crawlers = [ThanhNienNews, TuoiTreNews]

    def get_trending_text(self):
        for crawler in self.crawlers:
            cw = crawler()
            trends_text = cw.get_trending_text()
            yield {
                'label': cw.label,
                'text': trends_text
            }
