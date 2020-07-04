# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class MaoyanPipeline:
    def process_item(self, item, spider):
        title=item['title']
        link=item['link']
        mold=item['mold']
        release_time = item['release_time']
        movielist = [(title,mold,release_time)]
        movies_info = pd.DataFrame(data = movielist)
        movies_info.to_csv('./movie2.csv',encoding='utf8',mode='a', index=False, header=False)
        
        #output = f'|{title}|\t|{link}|\t|{mold}|\t|{release_time}|\n\n'
        #with open('./doubanmovie.txt', 'a+', encoding='utf-8') as article:
        #    article.write(output)
        #    article.close()
        
        return item
