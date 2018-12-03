# _*_coding:utf-8 _*_
from selenium import webdriver
import time


def open_chrome():
    driver = webdriver.Chrome()
    driver.get("https://pan.baidu.com/s/1kWv4FVT")
    elem = driver.find_element_by_xpath("//dd[@class='clearfix']/input")
    elem.send_keys("11wj")
    driver.find_element_by_xpath("//a[@class='g-button g-button-blue-large']").click().perform()  # 点击提交
    time.sleep(4)
    driver.refresh()
    driver.find_element_by_xpath("//*[@id='layoutMain']/div[1]/div[1]/div/div[2]/div/div/div[2]/a[1]").click().perform()


def get_cookie(url):
    d = webdriver.Chrome()
    d.get(url)
    time.sleep(10)
    d.find_element_by_id('loginname').send_keys("13034118040")
    time.sleep(5)
    d.find_element_by_xpath("//div[@class='info_list password']/div[1]/input[1]").send_keys("test_for_python")
    time.sleep(5)
    d.find_element_by_xpath("//div[@class='info_list login_btn']/a[1]").click().perform()
    cu = d.current_url
    print(cu)

if __name__ == '__main__':
    # open_chrome()
    get_cookie("https://pan.baidu.com/")
