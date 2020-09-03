from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os

# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # os.system('cd C:\\Users\\ccmx\\python\\Github\\Python001-class01\\week10\\shouji\\shouji\\spiders')
    os.system('cd C:\\Users\\ccmx\\python\\Github\\Python001-class01\\week10\\qipaoshui\\qipaoshui\\spiders')
    # os.system('mysql -u root -p123456')
    # os.system('use django')
    # os.system('drop table shouji_shouji')
    # os.system('exit')
    os.system('scrapy crawl smzdm')
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='0-6', hour=12, minute=45)
scheduler.start()