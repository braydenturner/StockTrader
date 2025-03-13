from .celery_app import celery_app

@celery_app.task
def fetch_daily_data() -> dict:
    print("fetch_daily_data")
    return {"succeeded": True}