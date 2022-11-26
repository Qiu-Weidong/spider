import scrapy
import urllib.parse
from scrapy import Request, Selector
from scrapy.selector.unified import SelectorList
from spider.items import HanyuguoxueItem

# 这里设置了爬取的汉字范围
st = 0x3400
ed = 0x4db6


class HanyuguoxueSpider(scrapy.Spider):
    name = 'hanyuguoxue'
    allowed_domains = ['www.hanyuguoxue.com']

    def start_requests(self):
        for c in range(st, ed):
            url = f'https://www.hanyuguoxue.com/zidian/zi-{c}'
            yield Request(url=url, cb_kwargs={"charactor": c})

    def parse(self, response, **kwargs):
        charactor = urllib.parse.unquote(chr(kwargs['charactor']))
        print('正在爬取: ', charactor)
        selector = Selector(response)
        item = HanyuguoxueItem()
        item['key'] = charactor
        # 异体字
        variant = selector.xpath('//*[@id="ziContent"]/div[1]/div[2]/div[2]/div['
                                 '2]/div/div/p[9]/span[2]/a').xpath('normalize-space(.)').extract()
        if len(variant) > 0:
            item['variant'] = variant
        # 意思和字义
        basic = selector.xpath('//*[@id="jbzyBody"]/div/div[2]/ol/li').xpath('string(.)').extract()
        if len(basic) > 0:
            item['basic'] = basic
        # 详细解释
        contents: SelectorList[Selector] = selector.xpath('//*[@id="xxjsBody"]/div/div[2]/ul/li')
        detail: dict = {}
        for content in contents.__iter__():
            header: str = content.xpath('normalize-space(./h4/span/text() )').extract_first()
            context: [str] = content.xpath('./ol/li').xpath('string(.)').extract()
            if header not in detail.keys():
                detail[header] = context
            else:
                detail[header] += context
        if detail != {}:
            item['detail'] = detail
        translate = selector.xpath('//*[@id="fanyiBody"]/ol/li[1]/text()').extract_first()
        item['translate'] = translate
        yield item



