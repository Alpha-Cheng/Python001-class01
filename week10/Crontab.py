from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import pymysql
import os

# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user = 'root',
                        password = '123456',
                        database = 'django',
                        charset = 'utf8mb4'
                        )
    sql = 'DROP TABLE IF EXISTS shouji_shouji;'
    try:
        # 获得cursor游标对象
        con1 = conn.cursor()
        # 操作的行数
        con1.execute(sql)
        conn.commit()
    except Exception as e:
        print(e,'Crontab---操作失败====================================')
    con1.close()
    conn.close()
    os.system('cd C:\\Users\\ccmx\\python\\Github\\Python001-class01\\week10\\qipaoshui\\qipaoshui & scrapy crawl smzdm')
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='0-6', hour=17, minute=48)
scheduler.start()