from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from img_down import downloads
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
    ID = os.environ['TMID']
    PW = os.environ['TMPW']
    driver.get('https://smavoice.jp/s/sma03/artist/45/contents?ima=0631&ct=45_122_02&tp=122&arti=45')
    button = driver.find_element_by_xpath('//*[@id="login"]/table/tbody/tr/td[1]/form/div/button')
    button.click()
    driver.find_element_by_name('idpwLgid').click()
    driver.find_element_by_name('idpwLgid').send_keys(ID)
    driver.find_element_by_name('idpwLgpw').click()
    driver.find_element_by_name('idpwLgpw').send_keys(PW)
    driver.find_element_by_name('idpwLgpw').send_keys(Keys.RETURN)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="main_in"]/form/div/button').click()

def get_imgs():
    aera = driver.find_elements_by_tag_name('img')
    imgs = []
    for i in aera:
        link = i.get_attribute("src")
        if 'images' in link:
            imgs.append(link)
    return imgs
    
if __name__ == "__main__":
    login()
    urls = get_imgs()
    downloads(urls)