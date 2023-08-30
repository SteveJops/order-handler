from typing import Literal
from .celery import app as celery_app

__all__: tuple[Literal['celery_app']] = ("celery_app",)