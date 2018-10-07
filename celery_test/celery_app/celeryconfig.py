from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://127.0.0.1:6379'  # broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  # backend
CELERY_TIMEZONE = 'Asia/Shanghai'  # 设置时区
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2'
)  # 指定导入的任务模块

CELERY_SCHEDULE = {
    'task1': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=10),
        'args': (2, 8)
    },
    'task2': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=17, minute=17)
        'args': (2, 8)
    }
}
