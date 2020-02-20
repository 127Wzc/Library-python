
#首页
pageIndex = 'https://wechat.laixuanzuo.com/index.php/reserve/index.html?f=wechat'


#明日预约
pagePre = 'https://wechat.laixuanzuo.com/index.php/prereserve/index.html'

AJAX_URL_s="https://wechat.laixuanzuo.com/index.php/reserve/get/"

def getbook_url(libid,code,key):
    #选座请求地址
    """url = "https://wechat.laixuanzuo.com/index.php/reserve/get/libid=11082&" + recode + "=19,13&yzm=\""""
    pageBook = "https://wechat.laixuanzuo.com/index.php/reserve/get/libid="+libid+"&"+code+"="+key+"&yzm="
    return pageBook

def getbook_preurl(libid,code,key,yzm):
    #选座请求地址
    """url = "https://wechat.laixuanzuo.com/index.php/reserve/get/libid=11082&" + recode + "=19,13&yzm=\""""
    pageBook = "https://wechat.laixuanzuo.com/index.php/prereserve/save/libid="+libid+"&"+code+"="+key+"&yzm="+yzm
    return pageBook


#个人中心
pageCenter = 'https://wechat.laixuanzuo.com/index.php/center.html'
