学习笔记

Diango web

1. 安装 pip install --upgrade django==2.2.13 
2. 创建 Django 项目 django-admin startproject MyDjango
3. 创建 Django 应用程序 
    * python manage.py help  查看该工具的具体功能 
    * python manage.py startapp index  创建程序名为 index 的目录
    * setting.py  wsgi--生产模式 app列表里添加自己的app，数据库配置添加等
    * urls调度器 增加项目urls 增加index的urls
4. views视图--Django快捷函数
    * render() 将给定的模板与给定的上下⽂字典组合在⼀起，并以渲染的⽂本返回⼀个 HttpResponse 对象。(默认的模板文件夹名字templates)
    * redirect() 将⼀个HttpResponseRedirect 返回到传递的参数的适当URL。
    * get_object_or_404() 在给定的模型管理器( model manager) 上调⽤get() ，但它会引发Http404 ⽽不是 模型的DoesNotExist 异常。
5. 模型与数据库
    * 每个模型都是一个Python 的类，这些类继承django.db.models.Model 
    * 模型类的每个属性都相当于一个数据库的字段
    * 利用这些，Django提供了一个自动生成访问数据库的API
    * 生成python中间脚本 ：
        python manage.py makemigrations 创建python脚本文件
        python manage.py migrate 应用到数据库
        python manage.py shell 交互模式下操作数据库的数据



作业背景

数据经过分析和清洗之后，需要使用适当的方式对数据进行展示，Web 就是当前最流行的展示方式之一。

作业要求

使用 Django 展示豆瓣电影中某个电影的短评和星级等相关信息：

    要求使用 MySQL 存储短评内容（至少 20 条）以及短评所对应的星级；
    展示高于 3 星级（不包括 3 星级）的短评内容和它对应的星级；
    （选做）在 Web 界面增加搜索框，根据搜索的关键字展示相关的短评。

注意

如果你对前端相关的技术不太熟悉，我们在页面下方提供了前端模版（frontend.zip 文件），可以直接在作业中使用。








1、Django安装
2、Django目录结构
3、URL规则
4、view视图
5、模型与数据库
6、模板

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