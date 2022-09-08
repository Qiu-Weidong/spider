import scrapy
from scrapy import Request, Selector
import re
from scrapy.selector import SelectorList

from spider.items import SpiderItem
import urllib.parse

# 这里设置了爬取的汉字范围
st = 0x4e00
ed = 0x9FA6


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.zdic.net']

    def start_requests(self):
        for c in range(st, ed):
            yield Request(url=f'https://www.zdic.net/hans/{urllib.parse.quote(chr(c))}')

    def parse(self, response, **kwargs):
        # print('\n-------------------\n')
        # 先选出装基本解释和详细解释的东西
        selector = Selector(response).css('body > main > div.zdict > div.res_c_center > div > div.homograph-entry > '
                                          'div > div')
        basic = selector.xpath('//*[@data-type-block="基本解释"]')

        # 获取到汉字
        char = basic.xpath('//div[1]/h2/span[1]/text()').extract_first()
        print('正在爬取: `' + char + '`')

        # 获取到基本解释的英文解释
        basic = basic.xpath('//*[@class="enbox"]/p/text()')
        detail = selector.xpath('//*[@data-type-block="详细解释"]//*[@class="encs"]/text()')

        keyword = []
        word: str
        for word in basic.extract():
            keyword += re.split('[;,]+', word)
        for word in detail.extract():
            word = word.strip('[').strip(']')
            keyword += re.split('[;,]+', word)

        # keyword = [item.strip() for item in keyword]
        words = []
        for word in keyword:
            word = word.strip()
            if word != '':
                words.append(word)
        words = list(set(words))
        if len(words) > 0:
            item = SpiderItem()
            item['name'] = char
            item['translate'] = words
            yield item
