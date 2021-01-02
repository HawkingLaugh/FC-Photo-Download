from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from image_batch_download import download
import os
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'
# for browser option settings
chromeOptions = Options()
chromeOptions.add_argument("--disable-popup-blocking")
chromeOptions.add_argument("--lang=en")
chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(PATH,chrome_options=chromeOptions)

def login():
    ID = 'yu16.hugo@gmail.com'
    PW = '29042038'
    driver.get('https://k.lxixsxa.com/s/n29/login')
    driver.find_element_by_name('idpwLgid').click()
    driver.find_element_by_name('idpwLgid').send_keys(ID)
    driver.find_element_by_name('idpwLgpw').click()
    driver.find_element_by_name('idpwLgpw').send_keys(PW)
    driver.find_element_by_name('idpwLgpw').send_keys(Keys.RETURN)

def open_page():
    # create a list of urls for download
    f = open('Temp.txt', 'w+')
    temp = 'https://k.lxixsxa.com'
    img_list = []
    site = input('Pass me a link: ')
    driver.get(site)
    style = driver.find_elements_by_xpath("//a")
    for i in style:
        link = i.get_attribute("data-href")
        if link != "None" or link != None:
            img_list.append(link)
    for i in img_list:
        str = '{}{}'.format(temp,i)
        if i != None:
            f.write(str)
            f.write('\n')
    return img_list

if __name__ == "__main__":
    login()
    open_page()
    fr = open('Temp.txt', 'r+')
    fr.seek(0,0)
    urllist = fr.read().splitlines()
    for j in urllist:
        download(j)