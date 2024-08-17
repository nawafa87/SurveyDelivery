import os
from redis import Redis
from rq import Worker, Queue, Connection
from flask import Flask
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
redis_conn = Redis.from_url(redis_url)

if __name__ == '__main__':
    with app.app_context():
        with Connection(redis_conn):
            worker = Worker([Queue()])
            worker.work()