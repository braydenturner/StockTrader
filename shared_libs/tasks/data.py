from .celery_app import celery_app

@celery_app.task
def fetch_daily_data() -> dict:
    print("fetch_daily_data")
    celery_app.send_task(
        name="data_collector.tasks.do_daily_fetch",
        args=[],
        kwargs={}
    )
    return {"succeeded": True}