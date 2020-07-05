import time
from selenium import webdriver

# 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie， 
# 期间使用 urllib3 的 connection pooling 功能。
# 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
try:
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html
    browser = webdriver.Chrome(executable_path='D:\Files\chromedriver_win32(1)39\chromedriver')

    browser.get('https://shimo.im/login?from=home')
    time.sleep(1)

    # browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    # btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    # btm1.click()

    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('15146893256')
    browser.find_element_by_xpath('//input[@name="password"]').send_keys('123456')
    time.sleep(1)
    browser.find_element_by_xpath('//button[contains(@class,"sm-button")]').click()

    cookies = browser.get_cookies() # 获取cookies
    #print(browser.page_source) #爬取的网页的源代码
    print(cookies)

    time.sleep(3)

except Exception as e:
    print('================================')
    print(e)
finally:    
    browser.close()
    