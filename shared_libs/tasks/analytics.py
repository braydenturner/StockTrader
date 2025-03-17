from .celery_app import celery_app

@celery_app.task
def store_analytics_data(data: dict) -> dict:
    celery_app.send_task("analytics_service.tasks.log_event", args=[data], kwargs={})
    
    return {"status": "logged"}


@celery_app.task
def log_message(message: str):
    print("Logging Message")
    print(message)