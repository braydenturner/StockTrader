from shared_libs.tasks.celery_app import celery_app
from .extraction.update import Updater

@celery_app.task
def do_daily_fetch():
    print("Doing daily fetch")
    updater: Updater = Updater()
    updater.run()
    