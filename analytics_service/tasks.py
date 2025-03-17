from shared_libs.tasks.celery_app import celery_app


@celery_app.task
def log_event(data: dict):
    print("Logging Event")
    
    

