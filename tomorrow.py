# -*- coding: UTF-8 -*-
import math
import introduce
import helper
import function
import url
import header
import time
from bs4 import BeautifulSoup
import timer
import userConfig

if __name__ == "__main__":
    introduce.initDesc()
    helper.initTry()
    session = userConfig.userinfo()
    first_Time =  math.floor(time.time())
    result = function.myWork(url.pageIndex, header.initPageIndex(first_Time, session))
    if "您好" in result:
        helper.succeed("成功进入选座系统")
    else:
        helper.failed("进入选座系统失败")
    html = function.myWork(url.pageCenter, header.initPageIndex(first_Time, session))
    soup = BeautifulSoup(html, "html.parser")
    print("您的个人信息如下：")
    for k in soup.find_all('div', class_='nick'):
        print("您的系统昵称：" + k.string)
    for k in soup.find_all('div', class_='userinfo'):
        print(str(k).replace("</div>", "").replace('<div class="userinfo" data-href="/index.php/times/index.html">', "")
              .replace('<div class="nick">', "用户名：").replace('<div class="study-detail">', "").replace("<div>", "")
              .replace('<div class="bg">', "").replace("学习时间", "：学习时间").replace("排名", "：排名").replace("单日最长", "：单日最长")
              .replace("\t", ""))
    print("信息通过 ，开始继续执行！")
    if timer.timer_setting():
        url_t = url.pagePre
        print(url_t)
        result=function.start_tomorrow(url_t,first_Time,session)
        #不成功则一直请求，可手动ctal+z关闭
        while "成功" not in result:
            result=function.start_tomorrow(url_t,first_Time,session)
            print(result)
        print(result+"\n成功")
