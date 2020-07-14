import random
from bs4 import BeautifulSoup
import requests,base64,json
from PIL import Image


def get_proxy(orderid):
    url = 'https://proxyapi.mimvp.com/api/fetchsecret?orderid='+orderid+'&result_fields=1,2,3'
    res = requests.get(url).text
    ips = res.split('\r\n')
    proxy = []
    for ip in ips:
        proxy.append('http://'+ip)
        proxy.append('https://'+ip)
    return proxy

headers = {
    'Cookie':'MIMVPSESSID=81lstsj1d71kfn33b3gl7ucikd; Hm_lvt_51e3cc975b346e7705d8c255164036b3=1593955763,1593991990; Hm_lpvt_51e3cc975b346e7705d8c255164036b3=1594004102'
}

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)

url = 'https://proxy.mimvp.com/common/ygrcode?rcode=123456'
picture = requests.get('https://proxy.mimvp.com/common/ygrcode?rcode=123456',headers=headers).content

with open('cap.jpg','wb') as File:
    File.write(picture)

im = Image.open('cap.jpg')
im.show()

with open('cap.jpg' ,'rb' ) as File:
    data = base64.b64encode(File.read())
    

url =  'https://v2-api.jsdama.com/upload'

param_1 =  {
"softwareId":20269,
"softwareSecret":"DWIopt0a8tg2fwtTbfOm5mF2MSnb3PKt6taBVYiI",
"username":"ganmingxuan2018",
"password":"Gan000803.",
"captchaData":str(data)[2:-1],
"captchaType":1013,
"captchaMinLength":5,
"captchaMaxLength":5,
"workerTipsId":0
}

res = requests.post(url,data=json.dumps(param_1,cls=MyEncoder,indent=4)).json()
valid = list(res['data']['recognition'])

a = tuple(input('哪些位是小写:'))
for i in a :
    valid[int(i)-1] = valid[int(i)-1].lower()

valid = ''.join(valid)

def RandomEmail( emailType=None, rang=None):
    __emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
    # 如果没有指定邮箱类型，默认在 __emailtype中随机一个
    if emailType == None:
        __randomEmail = random.choice(__emailtype)
    else:
        __randomEmail = emailType
    # 如果没有指定邮箱长度，默认在4-10之间随机
    if rang == None:
        __rang = random.randint(4, 10)
    else:
        __rang = int(rang)
    __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
    __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
    _email = __randomNumber + __randomEmail
    return _email

def create_phone():

    # 最后八位数字
    suffix = random.randint(9999999,100000000)

    # 拼接手机号
    return "1{}{}{}".format(5, 5, suffix)

s = requests.Session()

def register():
    mail = RandomEmail()
    phone = create_phone()
    pwd = 'hdDdqjjww123.'
    print('注册邮箱:',mail)
    print('注册手机号:',phone)
    print('密码:',pwd)
    print('验证码',valid)



    data = {
    'user_email':mail, 
    'user_pwd':pwd,        
    'user_mobile':phone,    
    'user_rcode':valid,
    'forurl':'/usercenter/?p=myinfo'
    }

    url = 'https://proxy.mimvp.com/lib/user_regist_check'

    res = s.post(url,data=data,headers=headers).json()
    return (res['code_msg'])

msg = register()
print(msg)

res = s.get('https://proxy.mimvp.com/usercenter/').text

soup = BeautifulSoup(res,'html.parser')
body = soup.find('tbody')
orderid = body.find('tr').find_all('td')[1].text
while(True):
    print(get_proxy(orderid))
    key =input('输入e退出,输入任意键继续获取:')
    if key == 'e':
        break
