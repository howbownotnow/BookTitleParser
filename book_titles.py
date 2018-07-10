from scrapy.spiders import Spider, Request
from scrapy.crawler import CrawlerProcess


class BookSpider(Spider):
    """
    Класс парсера названий всех книг с сайта http://books.toscrape.com
    """
    name = 'book_titles'
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']

    custom_settings = {'LOG_ENABLED': False}
    # отключение логгера, чтобы в консоль выводились только названия

    def parse(self, response):
        for book in response.css('article.product_pod h3'):
            # печать атрибута Title ссылки на книгу
            title = book.css('a::attr(title)').extract_first()
            print(title)
            # yield {
            #     'title': title
            # }

        # получение ссылки на следующую страницу
        next_page = response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            # Переход на следующую страницу и рекурсивный запуск функции
            yield Request(next_page, callback=self.parse)


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(BookSpider)
process.start()

input('Press Enter to finish')
