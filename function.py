import datetime
import math
import random
import threading
import time
import requests
import header
import jscode
import url
import userConfig


def myWork(url,config):
    return requests.get(url=url,headers=config,verify=False).text;

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
                return fp.read()

def initBaidu():
    from aip import AipOcr
    """ 你的 APPID AK SK """
    APP_ID = 'XXXXXXXX'
    API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXX'
    SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    return client

def optical(client,image):
    """ 调用通用文字识别（高精度版） """
    client.basicAccurate(image);
    """ 如果有可选参数 """
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "true"
    print("开始加载图像验证码人工智能视觉识别技术，请保持网络链接...")
    yzm = client.basicAccurate(image, options).get("words_result")[0].get("words")
    return str(yzm).replace(" ", "")


def downImage(time,session):
    x=random.random()
    image = 'https://wechat.laixuanzuo.com/index.php/misc/verify.html?'+str(x)
    print("图片地址:"+image)
    image=requests.get(url=image, headers=header.initImage(time, session), verify=False).content
    with open('code' + '.jpg', 'wb') as f:
        f.write(image)
        f.flush()
        f.close()


def start_reserve(url_t,first_Time,session):
    start_Time = time.time()
    Jsresult = myWork(url_t, header.initPageIndex(start_Time, session))
    libid,key= userConfig.userSeat()
    js_url = jscode.obtain_js(Jsresult)
    js_code = ''
    try:
        js_code = js_url[1]
    except Exception as e:
        print("获取js加密地址错误，请重试！")
    code = jscode.obtain_code(js_code)
    url2 = url.getbook_url(libid, code, key)
    pre_Time = math.floor(time.time())
    result =myWork(url2, header.initBook(first_Time, pre_Time, session))
    result_time = time.time()
    print("\n用时:" + str(result_time - start_Time))
    print("当前时间" + str(datetime.datetime.now()))
    return result


def start_tomorrow(url_t,first_Time,session):
    secondTime = time.time()
    Jsresult = myWork(url_t, header.initPageIndex(secondTime, session))
    libid,key= userConfig.userSeat()
    js_url = jscode.obtain_js(Jsresult)
    print(js_url)
    js_code = ''
    try:
        js_code = js_url[1]
        print(js_code)
    except Exception  as e:
        print("未到时间！或已经预定")
        return "获取参数错误"
    code = jscode.obtain_code(js_code)
    t = threading.Thread(target=downImage(str(secondTime), session))
    t.setDaemon(True)
    t.start()
    t.join()
    client = initBaidu()
    """ 读取图片 """
    image = get_file_content('code.jpg')
    yzm = ""
    try:
        yzm =optical(client, image)
        print("来选座系统验证码自动识别为：" + yzm)
    except Exception  as e:
        print("初次识别失败")
    for i in range(1, 5):
        if len(str(yzm)) != 4:
            t = threading.Thread(target=downImage(str(secondTime), session))
            t.setDaemon(True)
            t.start()
            t.join()
            print("验证码识别为：" + str(len(str(yzm))) + "个字符，与系统不匹配，默认开始继续识别！" + "第" + str(i) + "次识别")
            image = get_file_content('code.jpg')
            try:
                yzm = optical(client, image)
                print("来选座系统验证码自动识别为：" + yzm)
            except:
                print("此次识别失败")
        else:
            break
    pre_url = url.getbook_preurl(libid, code, key, yzm)
    secondTime = math.floor(time.time())
    result = myWork(pre_url, header.initBookPre(first_Time, secondTime, session))
    result_time = time.time()
    print("\n用时:" + str(result_time - secondTime))
    print("当前时间" + str(datetime.datetime.now()))
    return result
