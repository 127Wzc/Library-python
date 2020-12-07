import ssl

ssl._create_default_https_context = ssl._create_unverified_context
context = ssl._create_unverified_context()
def initGetNameVerify():
    header = {
        "Host": "wechat.laixuanzuo.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116"
                      " Safari/537.36 QBCore/4.0.1219.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501"
                      " NetType/WIFI WindowsWechat",
        "Accept": "image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5",
        "Referer":"https://wechat.laixuanzuo.com/index.php/prereserve/index.html",
        "Accept-Encoding": "br, gzip, deflate",
        "Accept-Language": "zh-CN",
        "Cookie": "Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=1568210257; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=1568206136,1568206651,1568209459,1568210040; FROM_TYPE=weixin; wechatSESS_ID=5811cdc6edce02182c7b486abf1b1c03",
    }
    return header

def initPagePre():
    header = {
        "Host": "wechat.laixuanzuo.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=1568209459; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=1568205321,1568206136,1568206651,1568209459; FROM_TYPE=weixin; wechatSESS_ID=5811cdc6edce02182c7b486abf1b1c03",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko)"
                      " MicroMessenger/2.3.26(0x12031a10) MacWechat NetType/WIFI WindowsWechat",
        "Accept-Language": "zh-cn",
        "Referer":"https://wechat.laixuanzuo.com/index.php/reserve/index.html",
        "Accept-Encoding": "br, gzip, deflate"
    }

    return header

import requests

url = 'https://wechat.laixuanzuo.com/index.php/misc/verify.html'
result = requests.get(url,headers=initGetNameVerify(),verify=False)
print("状态码：")
print(result.status_code)
print("\n")
print("返回体：")
print(result.text)
print("\n")

url = 'https://wechat.laixuanzuo.com/index.php/prereserve/index.html'
result = requests.get(url,headers=initPagePre(),verify=False)
print("状态码：")
print(result.status_code)
print("\n")
print("返回体：")
print(result.text)
print("\n")
