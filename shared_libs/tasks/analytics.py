from .celery_app import celery_app

@celery_app.task
def store_analytics_data(data: dict):
    return {"data": ["Apple", "Banana", "Cherry"]}