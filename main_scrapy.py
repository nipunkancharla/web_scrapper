import scrapy

class NewsSpider(scrapy.Spider):
    name = "news_spider"
    start_urls = ['http://example.com/news-article']

    def parse(self, response):
        title = response.css('h1.article-title::text').get().strip()
        date = response.css('time.article-date::text').get().strip()
        byline = response.css('span.byline::text').get().strip()
        content = "\n".join(response.css('div.article-content p::text').getall()).strip()

        yield {
            'Title': title,
            'Date': date,
            'Byline': byline,
            'Content': content,
        }
