def initBook(firsttime,time,session):
    header = {
        "Host": "wechat.laixuanzuo.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1295.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://wechat.laixuanzuo.com/index.php/reserve/index.html?f=wechat",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
        "Cookie": "wechatSESS_ID=" + session + "; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098="+str(firsttime)+"; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=" + str(time) + "",
    }
    return header


def initBookPre(time,solidtime,session):
    header = {
        "Host": "wechat.laixuanzuo.com",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Connection": "keep-alive",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1295.400 QQBrowser/9.0.2524.400 Mozilla/5.0 ("
                      "Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 "
                      "Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
        "Referer":"https://wechat.laixuanzuo.com/index.php/prereserve/index.html",
        "Accept-Encoding": "gzip, deflate",
        "Cookie": "wechatSESS_ID="+session+"; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098="+str(time)+","+str(solidtime)+"; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098="+str(solidtime)+"",
    }
    return header


def initPageIndex(solidtime,session):
    header = {
        "Host":"wechat.laixuanzuo.com",
        "Connection": "keep-alive",
        "Cache-Control":"max-age=0",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Cookie":"Hm_lpvt_7838cef374eb966ae9ff502c68d6f098="+str(solidtime)+";"
                 " Hm_lvt_7838cef374eb966ae9ff502c68d6f098="+str(solidtime)+";"
                 " FROM_TYPE=weixin; wechatSESS_ID="+(str(session))+"",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko)"
                     " MicroMessenger/2.3.26(0x12031a10) MacWechat NetType/WIFI WindowsWechat",
        "Accept-Language":"zh-cn",
        "Accept-Encoding":"br, gzip, deflate",

    }
    return header

def initImage(time,session):
    header = {
        "Host": "wechat.laixuanzuo.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 "
                      "Safari/537.36 QBCore/4.0.1295.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI "
                      "MicroMessenger/7.0.5 WindowsWechat",
        "Accept": "image/webp,image/*,*/*;q = 0.8",
        "Referer": "https://wechat.laixuanzuo.com/index.php/prereserve/index.html",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
        "Cookie": "FROM_TYPE=weixin;wechatSESS_ID=" + session + ";Hm_lvt_7838cef374eb966ae9ff502c68d6f098=" + str(
            time) + ";Hm_lpvt_7838cef374eb966ae9ff502c68d6f098" + str(time) + ""
    }
    return header
