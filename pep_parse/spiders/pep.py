import scrapy
from scrapy.exceptions import CloseSpider

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """
    Spider для парсинга PEP на странице http://peps.python.org/ с передачей
    PepParseItem для формирования результатов в виде csv-файла.
    """

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response, **kwargs):
        """
        Парсинг индексного нумератора PEP и переход по ссылке на страницу
        каждого PEP.
        """
        links = response.css('section[id=numerical-index]').css(
            'tbody a::attr(href)'
        )
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    @staticmethod
    def parse_pep(response) -> PepParseItem:
        """Парсинг страницы конкретного PEP с возвращением PepParseItem."""
        header = response.css('h1.page-title::text').get()
        lst_header = header.split('–', maxsplit=1)
        if len(lst_header) != 2:
            raise CloseSpider(f'Неверная структура заголовка: {header}')
        pep_number = lst_header[0].replace('PEP', '').lstrip()
        pep_name = lst_header[1].replace('PEP', '').lstrip()
        pep_status = response.css('dt:contains("Status") + dd').css(
            'abbr::text'
        ).get()
        data = {
            'number': pep_number,
            'name': pep_name,
            'status': pep_status
        }
        yield PepParseItem(data)
