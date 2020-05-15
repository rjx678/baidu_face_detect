import urllib, urllib.request

# 定义常量
APP_ID = '16141140'
API_KEY = 'Q2cWGu6tIAluykcL0PM2mezG'
SECRET_KEY = 'qeXpKRZk8y44P48KEHZM0u2Opjtt8ezf'


# token 请求 url 与图片不一样
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
       '&client_id=%s' \
       '&client_secret=%s' % (API_KEY, SECRET_KEY)

def GetToken():
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    #获取请求结果
    content = response.read()
    #转换为字符
    content = bytes.decode(content)
    #转换为字典
    content = eval(content[:-1])
    return content['access_token']
    # if (content):
    #     js = json.loads(content)
    #     # return js['refresh_token']
    #     return js['access_token']
    # return None





