1、scrapy-redis
2、redis-server redis.conf
3、redis-cli 
    --keys *
    --type movie:items
    --lpop movie:items
    --leys *
redis-server --service-start redis.windows-service.conf
redis-server --service-stop