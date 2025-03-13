from shared_libs.tasks.celery_app import celery_app

if __name__ == "__main__":
    # Start Celery worker, listening for tasks in 'orders_queue'
    celery_app.worker_main(["worker", "--loglevel=info", "--queues=model_queue"])