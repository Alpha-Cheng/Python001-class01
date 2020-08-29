import scrapy
import pandas as pd
from snownlp import SnowNLP
from scrapy.selector import Selector
from qipaoshui.items import QipaoshuiItem

class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['smzdm.com/fenlei/qipaoshui/']
    start_urls = ['http://smzdm.com/fenlei/qipaoshui//']

    # def parse(self, response):
    #     pass
    
    # 初始化函数，只执行一次
    def start_requests(self):
        for i in range(1,5):
            url = f'https://smzdm.com/fenlei/qipaoshui/p{i}/#feed-main'
            yield scrapy.Request(url = url, callback = self.parse,dont_filter = True)
        
    # 解析函数
    def parse(self, response):
        item = QipaoshuiItem()
        links = Selector(response=response).xpath('//li[@class="feed-row-wide"]/div/div[1]/a/@href').extract()
        for i in range(0,30):
            link = links[i]
            item['link'] = link
            yield scrapy.Request(url = link, meta = {'item': item}, callback = self.parse2,dont_filter = True)
    
    # 解析具体页面
    def parse2(self, response):
        item = response.meta['item']
        # xml化处理
        est = Selector(response=response).xpath('//span[@itemprop="description"]/text()').extract()
        estimates = pd.Series(est)
        print(estimates)
        def _sentiment(text):
            s = SnowNLP(text)
            return s.sentiments
        for i in range(0,len(estimates)):
            estimate = estimates[i].strip()
            if len(estimate) == 0:continue
            sentiment = _sentiment(estimates[i])
            item['n_star'] = sentiment // 0.2 + 1
            item['sentiment'] = sentiment
            item['estimate'] = estimate
            yield item