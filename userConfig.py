def userinfo():
    session = input("请输入提取的系统鉴权:\n")
    #session="ehhfirjjejruwyhehe"
    return session

#明日预约
def wzcSeat():
    #10092  12 19    郑东校区-5楼中阅览区 154号
    #10092  12 23    郑东校区-5楼中阅览区 158号
    #10084 12,28  郑东校区-3楼中阅览区 247号
    #10084 12,29  郑东校区-3楼中阅览区 248号\
    #print("请输入区号")
    libid ="10086"
    #print("请输入座位号,格式为a,b")
    key = "12,18"
    return libid, key




def initTry():
    print("尝试执行")

def succeed(s):
    print("执行成功："+str(s))

def failed(e):
    print("执行失败:"+str(e))

def show(t):
    print(t)