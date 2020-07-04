# 1.安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。


import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import lxml

myurl = 'https://maoyan.com/films?showType=3'
header = {
    
    'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN',
    'Cache-Control': 'max-age=0',
    'Connection':'keep-alive',
    'Cookie': 'uuid_n_v=v1; uuid=BA92A880BB9B11EAB07F039E5A9B22193D5D60FD0C614811B4DC3CEF63E55674; _csrf=a17df1836c0b97139a2dbb64ef0608a84d699b6e4930ade9a78b10f58631c308; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593608816; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593608816; _lxsdk_cuid=1730a7cc8059f-086a3cdba10101-2c3d184f-140000-1730a7cc806c8; _lxsdk_s=1730a7cc808-26c-03b-16f%7C%7C2; _lxsdk=BA92A880BB9B11EAB07F039E5A9B22193D5D60FD0C614811B4DC3CEF63E55674; __mta=214719784.1593608817865.1593608817865.1593608817865.1',
    'Host': 'maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

response = requests.get(myurl, headers=header)
bs_info = bs(response.text, 'html.parser')
base_url='https://maoyan.com'
mylist=[]
for n in bs_info.find_all('div', attrs={'class': 'movie-item-hover'})[:10]:
    m = n.find('a')
    extr_url=m.get('href')
    url=base_url+extr_url
    print(url)
    res = requests.get(url, headers=header)
    selector = lxml.etree.HTML(res.text)
    film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
    film_class = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[@class="text-link"]/text()')
    plan_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
    movies=(film_name, film_class, plan_date)
    mylist.append(movies)
    output = f'|{movies}|\t|\n\n'
    with open('./Python001-class01/week01/doubanmovie.txt','a+', encoding='utf-8') as article:
        article.write(output)
        article.close()
print('mylist=',mylist)
movie1 = pd.DataFrame(data = mylist)

movie1.to_csv('./Python001-class01/week01/movie1.csv', encoding='utf8', index=False, header=False)

            


      



