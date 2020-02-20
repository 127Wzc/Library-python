# 来选座自动抢座脚本
------
##文件结构
```function```  具体方法实现
```header``` 请求头信息  
```jscode``` 获取js加密 字段
```timer``` 定时管理（可自行修改测试代码，目前为每天19:50:00）
```today``` 今日预约座位（无验证码）
```tomorrow``` 明日预约（有验证码，验证码通过百度API实现，自己注册账号在```function``` 的   ```initBaidu()```方法加入即可）
```url``` 各种需要的url地址
```userConfig``` 用户信息  座位信息 （自己爬取心仪的位置信息，按要求填入修改即可） session由抓包工具自行获取

------
##抓包教程
* [可参考Luo大佬B站视频](https://www.bilibili.com/video/av44994621)
------
##参考资料：
* [逻辑分析](https://blog.csdn.net/RenjiaLu9527/article/details/96843605)
* [灵感来源](https://www.bilibili.com/video/av44994621)
