# _*_ coding:utf-8_*_
from celery_app import task1
from celery_app import task2

print("hello world")
task1.add.delay(2, 8)  # 使用delay方法将add任务加入到消息队列中去
task2.multiply.delay(2, 8)
print("bye world")
