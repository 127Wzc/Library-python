# -*- coding: UTF-8 -*-
import datetime
import time


# 判断时间是否符合，直到19：50返回true
def timer_setting():
    sleep_time = 1.0
    now = time.localtime()
    year = now.tm_year
    month = now.tm_mon
    day = now.tm_mday
    hour = now.tm_hour
    my_time = str(year) + '-' + str(month) + '-' + str(day) + '-' + str(hour) + '-50' + '-00'
    startTime = datetime.datetime(year, month, day, hour, 50, 0)
    print("目标时间：北京时间19:50分\t" + "预计等待：" + str(
        int(int(time.mktime(time.strptime(my_time, '%Y-%m-%d-%H-%M-%S'))) - int(time.time()))) + "秒")
    goal = time.mktime(time.strptime(my_time, '%Y-%m-%d-%H-%M-%S'))
    while datetime.datetime.now() < startTime:
        #
        wait = int(int(goal) - int(time.time()))
        if wait == 3 or wait == 2:
            sleep_time = 0.1
        print("当前时间" + str(datetime.datetime.now()) + "预计等待:" + str(wait) + "秒")
        time.sleep(sleep_time)
    return True


# 判断时间是否符合白天开馆时间
def timer_today():
    sleep_time = 1.0
    now = time.localtime()
    year = now.tm_year
    month = now.tm_mon
    day = now.tm_mday
    hour = now.tm_hour
    my_time = str(year) + '-' + str(month) + '-' + str(day) + '-' + str(hour) + '-30' + '-00'
    startTime = datetime.datetime(year, month, day, hour, 30, 0)
    print("目标时间：北京时间19:00分\t" + "预计等待：" + str(
        int(int(time.mktime(time.strptime(my_time, '%Y-%m-%d-%H-%M-%S'))) - int(time.time()))) + "秒")
    goal = time.mktime(time.strptime(my_time, '%Y-%m-%d-%H-%M-%S'))
    while datetime.datetime.now() < startTime:
        #
        wait = int(int(goal) - int(time.time()))
        if wait == 3 or wait == 2:
            sleep_time = 0.1
        print("当前时间" + str(datetime.datetime.now()) + "预计等待:" + str(wait) + "秒")
        time.sleep(sleep_time)
    return True
