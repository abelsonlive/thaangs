import dataset
import redis
from flask import Flask 

from thaangs import settings

# redis connection
rdb = redis.from_url(settings.REDIS_URL)

# database 
db = dataset.connect(settings.DATABASE_URL)

# app
app = Flask(__name__)
