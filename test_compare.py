import json
import urllib
import base64
from baidu_face_detect.token11 import GetToken


# 转换图片 读取文件内容 转换为base64编码
# 二进制打开图片
def img_compare_data(fp1, fp2):
    f = open(fp1, 'rb')
    pic1 = base64.b64encode(f.read())
    f.close()
    f = open(fp2, 'rb')
    pic2 = base64.b64encode(f.read())
    f.close()
    # 将图片信息格式化为可提交信息，注意str
    params = json.dumps(
        [{"image": str(pic1, 'utf-8'), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
         {"image": str(pic2, 'utf-8'), "image_type": "BASE64", "face_type": "IDCARD", "quality_control": "LOW"}]
    )
    return params.encode(encoding='UTF8')


# 人脸比对
def img_compare(fp1, fp2):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
    params = img_compare_data(fp1, fp2)
    access_token = GetToken()
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read()
    content = eval(content)
    score = content['result']['score']
    if score > 80:
        return '照片相似度：' + str(score) + ',同一个人'
    else:
        return '照片相似度：' + str(score) + ',不是同一个人'

import time
if __name__ == '__main__':
    file1path = r'C:\Users\rjx\PycharmProjects\untitled1\facenet-master\data\self_data\ldh\ldh_1.jpg'
    file2path = r'C:\Users\rjx\PycharmProjects\untitled1\facenet-master\data\self_data\ldh\ldh_0.jpg'
    s = time.time()
    res = img_compare(file1path, file2path)
    t = time.time()-s
    print(res)
    print(t)







