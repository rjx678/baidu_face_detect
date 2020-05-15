import json
import urllib
import cv2
import base64
from baidu_face_detect.token11 import GetToken

###########################################################
def img_detect_data(filepath):
    with open(filepath, 'rb') as fp:
        pic1 = base64.b64encode(fp.read())
        params = json.dumps(
            {"image": str(pic1, 'utf-8'), "image_type": "BASE64", "face_field": "age,beauty,expression,faceshape" ,"max_face_num":10}
        )
        return params.encode(encoding='UTF8')

def img_detect(fp1):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    params =img_detect_data(fp1)
    access_token = GetToken()
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)

    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read()
    content = eval(content)
    print(content['result']['face_list'][0]['age'])
    img = cv2.imread(fp1)

    face_num = content['result']['face_num']
    for i in range(face_num):
        location = content['result']['face_list'][i-1]['location']
        left = int(location['left'])
        top = int(location['top'])
        width = int(location['width'])
        height= int(location['height'])
        left_top = (left,top-16)
        right_bottom = (left+width,top-16+height)
        cv2.rectangle(img,left_top,right_bottom,(0,255,0),2)

    cv2.imshow("img",img)
    cv2.waitKey(0)


if __name__ == '__main__':
    filepath = r'C:\Users\rjx\PycharmProjects\untitled1\facenet-master\data\test\test3.jpg'
    img_detect(filepath)

