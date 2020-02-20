# -*- coding: UTF-8 -*-
import datetime
import time


# 判断时间是否符合，直到19：50返回true
def timer_setting():
    now = time.localtime()
    year = now.tm_year
    month = now.tm_mon
    day = now.tm_mday
    hour = now.tm_hour
    my_time = str(year) + '-' + str(month) + '-' + str(day) + '-' + str(19) + '-50' + '-00'
    startTime = datetime.datetime(year, month, day, 19, 50, 0)
    while datetime.datetime.now() < startTime:
        goal = time.mktime(time.strptime(my_time, '%Y-%m-%d-%H-%M-%S'))
        print("目标时间：北京时间19:50分\t" + "预计等待：" + str(int(int(goal) - int(time.time()))) + "秒")
        print("当前时间"+str(datetime.datetime.now()))
        time.sleep(0.1)
    return True
