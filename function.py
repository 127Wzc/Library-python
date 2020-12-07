import datetime
import math
import random
import threading
import time
import requests
import browerConfig
import jscode
import url
import userConfig


def myWork(url, config):
    return requests.get(url=url, headers=config, verify=False).text;


# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def initBaidu():
    from aip import AipOcr
    APP_ID = '18419446'
    API_KEY = 'cgAN2pXz0YheYqSZ9KQAlTT3'
    SECRET_KEY = 'z5p7MgZRhlLE2FA3GXIOa0hE7ZrsoOWw'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    return client


def optical(client, image):
    client.basicAccurate(image);
    """ 如果有可选参数 """
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "true"
    yzm = client.basicAccurate(image, options).get("words_result")[0].get("words")
    return str(yzm).replace(" ", "")


def downImage(time, session):
    x = random.random()
    image = 'https://wechat.laixuanzuo.com/index.php/misc/verify.html?' + str(x)
    image = requests.get(url=image, headers=browerConfig.initImage(session, time), verify=False).content
    with open('code' + '.jpg', 'wb') as f:
        f.write(image)
        f.flush()
        f.close()


def start_tomorrow(url_t, first_Time, session,libid,key):
    secondTime = time.time()
    print(datetime.datetime.now())

    Jsresult = myWork(url_t, browerConfig.initPageIndex(secondTime, session))
    image = 'https://wechat.laixuanzuo.com/index.php/misc/verify?' + str(round(time.time() * 1000))
    data = requests.get(url=image,
                        headers=browerConfig.initGetNameVerify(session, str(time.time())),
                        verify=False, allow_redirects=False)


    img_adress = data.headers['location'].split("/")[-1]
    img_name = img_adress.split(".")[0]

    yzm = jscode.obtain_code_yzm(img_name)
    if yzm is None:
        return "验证码错误"

    js_url = jscode.obtain_js(Jsresult)
    print(js_url)
    js_code = ''
    try:
        # 获得js脚本中动态码地址
        js_code = js_url[1]
    except Exception  as e:

        return "未到时间"
    # 获取动态ajax加密餐宿
    code = jscode.obtain_code_test(js_code)
    if code is None:
        return "已经预定或未到时间"
    if yzm is None:
        yzm = ""
        client = initBaidu()
        """ 下载图片 """
        image_file = requests.get(url=img_adress, headers=browerConfig.initImage(session, time), verify=False).content
        with open('0' + '.jpg', 'wb') as f:
            f.write(image_file)
            f.flush()
            f.close()
        """ 读取图片 """
        image_now = get_file_content('0.jpg')
        yzm = optical(client, image_now)
        try:
            yzm = optical(client, image)
            print("初次识别成功" + str(yzm))
        except Exception  as e:
            print("初次识别失败")
        if len(yzm) != 4:
            for i in range(1, 10):
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
    # 拼接获取请求地址(场馆号，加密字段，座位key)
    print(code)
    pre_url = url.getbook_preurl(libid, code, key, yzm)
    print(pre_url)
    # 开始发起请求
    result = myWork(pre_url, browerConfig.initBookPre(first_Time, secondTime, session))
    # 获取结束的时间
    result_time = time.time() * 1000
    print("\n用时:" + str((result_time - first_Time) / 1000) + "秒")
    print("当前时间" + str(datetime.datetime.now()))
    return result


def start_today(url_t, first_Time, session):
    # 获取开始请求的时间戳
    start_Time = time.time()
    # 请求选座页面
    Jsresult = myWork(url_t, browerConfig.initPageIndex(start_Time, session))
    # 座位信息
    libid, key = userConfig.userToday()
    # 开始拉去js验证码获取js脚本
    js_url = jscode.obtain_js(Jsresult)
    js_code = ''
    try:
        # 获得js脚本中动态码地址
        js_code = js_url[1]
        print(js_code)
    except Exception  as e:
        print("Session 值错误，检查重试！")
    # 获取动态ajax加密参数
    code = jscode.obtain_code_test(js_code)
    # 拼接获取请求地址(场馆号，加密字段，座位key)
    url2 = url.getbook_url(libid, code, key)
    # 获取请求选座的时间戳
    pre_Time = math.floor(time.time())
    # 开始发起请求
    result = myWork(url2, browerConfig.initBookNow(first_Time, pre_Time, session))
    # 获取结束的时间
    result_time = time.time()
    print("\n用时:" + str(result_time - start_Time))
    print("当前时间" + str(datetime.datetime.now()))
    return result
