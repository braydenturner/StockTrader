from shared_libs.tasks.celery_app import celery_app
from celery.schedules import crontab

schedule = 86400.0 # 24 hours in seconds, can also set specific time with cron
schedule_5 = 5.0
schedule_8am = crontab(minute=0, hour=8)

# Beat
celery_app.conf.beat_schedule = {
    "fetch-daily-data": {
        "task": "data_collector.tasks.do_daily_fetch",
        "schedule": schedule_5,  
        "args": ()            # optional arguments
    },
}
