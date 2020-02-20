
function  具体方法实现
header 请求头信息   
jscode 获取js加密 字段
timer 定时管理（可自行修改测试代码，目前为每天19:50:00）
today 今日预约座位（无验证码）
tomorrow 明日预约（有验证码，验证码通过百度API实现，自己注册账号在function 的   initBaidu()方法加入即可）
url 各种需要的url地址
userConfig 用户信息  座位信息 （自己爬取心仪的位置信息，按要求填入修改即可） session由抓包工具自行获取

参考资料：
1.Wheeehan大佬：
    我去图书馆-抢座主逻辑详解 https://blog.csdn.net/RenjiaLu9527/article/details/96843605
2.Luo大佬
     https://www.bilibili.com/video/av44994621 该大佬所发Android抓包教程
     https://github.com/luoenen/AI-HUELSeat       该大佬git地址（为我学习提供了基础，不过该地址的程序暂时不能跑咯需要修改）
