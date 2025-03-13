from celery import Celery
from kombu import Queue
from dotenv import load_dotenv
import os

load_dotenv()
broker = os.getenv("CELERY_BROKER_URL")

celery_app = Celery(
    "stock_app",
    broker=broker,  # RabbitMQ URL
    backend="rpc://",  # or "redis://"
)

# Optional: load config from a file or dict
celery_app.conf.update(
    task_routes={
        "shared_libs.tasks.orders.*": {"queue": "orders_queue"},
        "shared_libs.tasks.data.*":   {"queue": "data_queue"},
        "shared_libs.tasks.model.*":   {"queue": "model_queue"},
        "shared_libs.tasks.analytics.*":   {"queue": "analytics_queue"},
    }
)

celery_app.conf.beat_schedule = {
    "fetch-daily-data": {
        "task": "shared_libs.tasks.data.fetch_daily_data",
        "schedule": 86400.0,  # 24 hours in seconds
        "args": ()            # optional arguments
    },
}

celery_app.conf.task_queues = (
    Queue("orders_queue"),
    Queue("data_queue"),
    Queue("model_queue"),
    Queue("analytics_queue"),
)



import shared_libs.tasks.orders
import shared_libs.tasks.data
import shared_libs.tasks.model
import shared_libs.tasks.analytics