from shared_libs.tasks.celery_app import celery_app

celery_app.conf.beat_schedule = {
    "fetch-daily-data": {
        "task": "data_collector.tasks.do_daily_fetch",
        "schedule": 5 ,#86400.0,  # 24 hours in seconds
        "args": ()            # optional arguments
    },
}

@celery_app.task
def do_daily_fetch():
    print("Doing daily fetch")