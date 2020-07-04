# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd
import pymysql

# 执行批量插入
# values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
# cursor.executemany('INSERT INTO '+ TABLE_NAME +' values(%s,%s)' ,values)
class DoubanPipeline:
    def process_item(self, item, spider):
        conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user = 'root',
                        password = '123456',
                        database = 'test',
                        charset = 'utf8mb4'
                        )
        sql=''' CREATE TABLE IF NOT EXISTS `douban`(
                `id` INT UNSIGNED AUTO_INCREMENT,
                `title` VARCHAR(80) NOT NULL,
                `mold` VARCHAR(80) NOT NULL,
                `release_time` VARCHAR(100) NOT NULL,
                PRIMARY KEY ( `id` )
                )ENGINE=InnoDB DEFAULT CHARSET=utf8;'''
        
        #sql1="INSERT INTO douban(`id`,`title`,`mold`,`release_time`) VALUES( 1,'{}','{}','{}')".format(item['title'],item['mold'],item['release_time']);
        sql1="INSERT INTO movies(?,?,?) VALUES ('{title}', '{mold}', '{release_time}')".format(title=item['title'],mold=item['mold'],release_time=item['release_time']);
    
        try:
            # 获得cursor游标对象
            con1 = conn.cursor()
            # 操作的行数
            con1.execute(sql)
            print('-------------------------------------------')
            con1.execute(sql1)
            print('--------------------------------------------')
            con1.commit()
        except Exception as e:
            print(e,'操作失败====================================')
        con1.close()
        conn.close()

        #output = f'|{title}|\t|{link}|\t|{mold}|\t|{release_time}|\n\n'
        #with open('./doubanmovie.txt', 'a+', encoding='utf-8') as article:
        #    article.write(output)
        #    article.close()
        return item 