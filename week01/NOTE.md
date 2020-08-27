今天是本周的第一天，今晚把本周的视频看了一遍，对本周的学习任务有了整体的认识和把握。第一个作业任务的基本实现了，还需要优化和改进，git工具用的不好，这几天多多练习和学习。
今天是本周的第二天， 把昨天写的代码优化了一下，有一点小收获，今天把视频又看了一遍，可能是接受能力太差做题太没有一点头绪，每天能进步一点就好，好好训练思维。
今天是本周的第三天，今天先把视频又看了一遍，打算今天把作业二完成，对程序代码了逻辑结构还不是很清楚的时候就开始先把老师的代码抄过来，先理解一下看一看老师的思路，看代码听视频，听了三四遍才把要要点知识罗列差不多了，基本能够理解个来龙去脉了，以前听别人讲多读几遍就会有收获，这次也体会到了这个方法的效果，前提是动力十足的干劲。
今天终于把作业全部完成了，思路也有一点启发，就是学习的能力太差了，进步太慢了，不断地锤炼自我，精进自我是唯一的选择，努力锤炼吧。

1. requests结构
    git clone https://github.com/Alpha-Cheng/geekbangtrain
    cd geekbangtrain
    git checkout 1a
    git checkout --track origin/1a

    也可以使用 https://github.com/hellysmile/fake-useragent 这个库随机生成哈：

    ctrl + F
    pip install -r requirements.txt
    pip install xxx -i https://pypi.douban.com/simple
    git checkout 1b
    git checkout 1c
    git diff 1b
    dir(math)
    help(math)
2. scrapy 架构工具
    pip install scrapy
    pip install -r requirements.txt
3. 创建项目
    创建爬虫项目scrapy startproject spiders
    创建目标模块scrapy genspider example example.com
4. 运行爬虫
    scrapy crawl movie

推导式是为了创建新的字典，列表，集合的
    
bs4 是python实现的  lxml是用c语言实现的
## 作业一：

安装并使用 requests、bs4、lxml 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

## 作业二：

使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

猫眼电影网址： https://maoyan.com/films?showType=3

要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。
    

