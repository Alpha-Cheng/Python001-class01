1、scrapy-redis
2、redis-server redis.conf
3、redis-cli 
    --keys *
    --type movie:items
    --lpop movie:items
    --keys *
redis-server --service-start redis.windows-service.conf
redis-server --service-stop

"{\"title\": \"\\u9738\\u738b\\u522b\\u59ec\", \"link\": \"https://movie.douban.com/subject/1291546/\", \"mold\": [\"\\u5267\\u60c5\", \"\\u7231\\u60c5\", \"\\u540c\\u6027\"], \"release_time\": [\"1993-01-01(\\u4e2d\\u56fd\\u9999\\u6e2f)\", \"1993-07-26(\\u4e2d\\u56fd\\u5927\\u9646)\"]}"