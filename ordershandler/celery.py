import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ordershandler.settings")


app = Celery("ordershandler")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
