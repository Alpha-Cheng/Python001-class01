# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pandas as pd
import pymysql
from itemadapter import ItemAdapter
# 执行批量插入
# values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
# cursor.executemany('INSERT INTO '+ TABLE_NAME +' values(%s,%s)' ,values)

class QipaoshuiPipeline:
    def process_item(self, item, spider):
        conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user = 'root',
                        password = '123456',
                        database = 'test',
                        charset = 'utf8mb4'
                        )
        sql=''' CREATE TABLE IF NOT EXISTS `qipaoshui_qipaoshui`(
                `id` INT UNSIGNED AUTO_INCREMENT,
                `estimate` LONGTEXT NOT NULL,
                PRIMARY KEY ( `id` )
                )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;'''
        
        #sql1="INSERT INTO douban(`title`,`mold`,`release_time`) VALUES('{title}', '{mold}', '{release_time}')",(item['title'],item['mold'],item['release_time']);
        # sql1="INSERT INTO douban(`title`,`mold`,`release_time`) VALUES ('{title}', '{mold}', '{release_time}')".format(title=item['title'], mold=' '.join(item['mold']), release_time=' '.join(item['release_time']));
        sql1="INSERT INTO qipaoshui_qipaoshui(`estimate`) VALUES ('{estimate}')".format(estimate=item['estimate']);
        try:
            # 获得cursor游标对象
            con1 = conn.cursor()
            # 操作的行数
            con1.execute(sql)
            con1.execute(sql1)
            conn.commit()
        except Exception as e:
            print(sql1)
            print(e,'操作失败====================================')
        con1.close()
        conn.close()
        return item 
    

    
        # rt = {'title': item['title'],'mold': item['mold'],'release_time': item['release_time']}
        # #写数据到Redis
        # idkey = 'douban_movie'
        # #hash表数据写入命令hmget，可以一次写入多个键值对
        # print(r.hmget(idkey,rt))
        
        #output = f'|{title}|\t|{link}|\t|{mold}|\t|{release_time}|\n\n'
        #with open('./doubanmovie.txt', 'a+', encoding='utf-8') as article:
        #    article.write(output)
        #    article.close()
        
        #  redis 存储了item
        #  bash$  redis-cli
        #  redis> keys *
        #  redis> type cluster:items
        #  redis> lpop cluster:items
        #  redis> keys *