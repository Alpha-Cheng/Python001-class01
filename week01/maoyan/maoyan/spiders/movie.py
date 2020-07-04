# -*- coding: utf-8 -*-
import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls =['http://maoyan.com']

    #def parse(self, response):
    #    pass

    def start_requests(self):
    
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse,dont_filter=False)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        # xml化处理
        
        movies = Selector(response=response).xpath('//div[@class="movie-item-hover"]')[:10]
        for movie in movies:
            base_url='https://maoyan.com'
            item = MaoyanItem()
            title = movie.xpath('./a/div/div[1]/span[1]/text()').extract()
            link = movie.xpath('./a/@href').extract_first()
            item['title'] = title
            hurl=base_url+link
            item['link'] = hurl
            print(hurl)
            yield scrapy.Request(url=hurl, meta={'item': item}, callback=self.parse2,dont_filter=False)

    # 解析具体页面
    def parse2(self, response):
        
        item = response.meta['item']
        # xml化处理
        movies1=Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        print(movies1)
        for movie in movies1:
            mold =movie.xpath('./ul/li[1]/a[@class="text-link"]/text()').extract()
            release_time = movie.xpath('./ul/li[3][@class="ellipsis"]/text()').extract()
            print(mold)
            print(release_time)
            item['mold']=mold
            item['release_time']=release_time
        yield item