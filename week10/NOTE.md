学习笔记

毕业项目：构建一个舆情分析平台

项目背景：某公司计划新上线一款苏打水饮料，为了了解用户对苏打水的接受程度，需要抓取“什么值得买”( https://www.smzdm.com/fenlei/qipaoshui/ ) 网站中气泡水种类前 10 的产品的用户评论，通过对用户评论的正向、负向评价了解排名前 10 的气泡水产品的用户接受程度。

具体需求：

1. 正确使用 Scrapy 框架或 Selenium 获取评论，如果评论有多页，需实现自动翻页功能，将原始评论结果存入 MySQL 数据库，并使用定时任务每天定期更新。
2. 对评论数据进行清洗（可借助 Pandas 库），并进行语义情感分析，将分析结果存入数据库。
3. 使用 Django 集成在线图表对采集数、舆情进行展示，需包括该产品正、负评价比例，以及评价内容等。
4. 数据展示支持按时间筛选和按关键词筛选功能（参考百度情感分析后台 https://ai.baidu.com/tech/nlp_apply/sentiment_classify）。

评分标准：（实现相应功能，每项 +10 分，部分实现 +5 分）

1. 正确使用 Scrapy 框架获取评论，如果评论有多页，需实现自动翻页功能。
2. 评论内容能够正确存储到 MySQL 数据库中，不因表结构不合理出现数据截断情况。
3. 数据清洗后，再次存储的数据不应出现缺失值。
4. Django 能够正确运行，并展示采集到的数据，数据不应该有乱码、缺失等问题。
5. 在 Django 上采用图表方式展示数据分类情况。
6. 舆情分析的结果存入到 MySQL 数据库中。
7. 在 Django 上采用图表方式展示舆情分析的结果。
8. 可以在 Web 界面根据关键字或关键词进行搜索，并能够在页面展示正确的搜索结果。
9. 支持按照时间（录入时间或评论时间）进行搜索，并能够在页面展示正确的搜索结果。
10. 符合 PEP8 代码规范，函数、模块之间的调用高内聚低耦合，具有良好的扩展性和可读性。

# 作业完成过程

## 爬取数据放入数据库

### 创建scrapy爬虫
```shell
    scrapy -help
    scrapy startproject qipaoshui
    scrapy genspider smzdm www.smzdm.com/fenlei/qipaoshui
```
### 获取评论
```python
    def start_requests(self):
        for i in range(1,2):
            url = f'https://smzdm.com/fenlei/qipaoshui/p{i}/#feed-main'
            yield scrapy.Request(url = url, callback = self.parse,dont_filter = True)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数
            # dont_filter = false 代表打开请求过滤，请求次数过多就会被拦截
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
        estimates = Selector(response=response).xpath('//span[@itemprop="description"]/text()').extract()
        print(estimates)
        for i in range(0,len(estimates)):
            estimate = estimates[i]
            item['estimate'] = estimate
            yield item
```
### 运行爬虫获取数据
```shell
    scrapy crawl smzdm
```


## 创建Django项目

### 创建 Django 项目 
    *django-admin startproject MyDjango

### 创建 Django 应用程序 
     
    * python manage.py startapp qipaoshui
    * setting.py 添加app 添加数据库设置 
    * urls调度器 增加项目urls 增加index的urls

    * python manage.py makemigrations 
    * python manage.py migrate



常见报错
1.  django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 'MySQLdb'
    解决方法：在 __init__.py 文件中添加以下代码即可
    import pymysql
    pymysql.install_as_MySQLdb()

2.   version = Database.version_info
    # if version < (1, 3, 13):
    # raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)

3.  AttributeError: 'str' object has no attribute 'decode'
    出现这个错误之后可以根据错误提示找到文件位置，打开 operations.py 文件，找到以下代码：
    def last_executed_query(self, cursor, sql, params):
    query = getattr(cursor, '_executed', None)
    # if query is not None:
    #     query = query.decode(errors='replace')
    return query