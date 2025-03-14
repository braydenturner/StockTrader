from .celery_app import celery_app

@celery_app.task
def fetch_daily_data() -> dict:
    print("fetch_daily_data")
    daily_fetchs_sig = celery_app.signature("data_collector.tasks.do_daily_fetch")
    daily_fetchs_sig.delay()
    return {"succeeded": True}