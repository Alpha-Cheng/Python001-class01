# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
from scrapy.selector import Selector



class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']
    #i=1
    
    def start_requests(self):
    
        url = 'https://movie.douban.com/top250'
        yield scrapy.Request(url=url, callback=self.parse,dont_filter=True)
        
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        # xml化处理
        movies = Selector(response=response).xpath('//div[@class="hd"]')[:10]
        for movie in movies:
            item = DoubanItem()
            title = movie.xpath('./a/span/text()').extract()[0]
            link = movie.xpath('./a/@href').extract_first()
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2,dont_filter=True)

    # 解析具体页面
    def parse2(self, response):
        
        item = response.meta['item']
        # xml化处理
        movies1=Selector(response=response).xpath('//div[@id="info"]')
        for movie in movies1:
            mold =movie.xpath('./span[@property="v:genre"]/text()').extract()
            release_time = movie.xpath('./span[@property="v:initialReleaseDate"]/text()').extract()
            item['mold']=mold
            item['release_time']=release_time
        yield item