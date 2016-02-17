import dataset
import redis

from thaangs import settings

# redis connection
rdb = redis.from_url(settings.REDIS_URL)
db = dataset.connect(settings.DATABASE_URL)