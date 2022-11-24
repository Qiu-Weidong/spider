import scrapy
from scrapy import Request, Selector
import urllib.parse

from spider.items import HwxnetItem

# 这里设置了爬取的汉字范围
st = 0x20000
ed = 0x20800


# ed = 2A6D6


class HwxnetSpider(scrapy.Spider):
    name = 'hwxnet'
    allowed_domains = ['wyw.hwxnet.com']

    def start_requests(self):
        for c in range(st, ed):
            charactor: str = urllib.parse.quote(chr(c))
            param = {"charactor": c}
            yield Request(url=f'https://wyw.hwxnet.com/view.do?keyword={charactor}', cb_kwargs=param)

    def parse(self, response, **kwargs):
        # 通过参数将正在爬取的字符传递过来
        charactor = urllib.parse.unquote(chr(kwargs['charactor']))
        print('正在爬取汉字: ' + charactor)
        selector: Selector = Selector(response).xpath('/html/body/div[1]/div[2]/div[1]/div[5]')[0]
        context: str = selector.xpath('string(.)').extract()[0].strip()
        item = HwxnetItem()
        item['key'] = charactor
        item['value'] = context
        yield item
