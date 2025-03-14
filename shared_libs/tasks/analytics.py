from .celery_app import celery_app

@celery_app.task
def store_analytics_data(data: dict) -> bool:
    celery_app.send_task("analytics_service.tasks.log_event", args=[data], kwargs={})
    
    return True