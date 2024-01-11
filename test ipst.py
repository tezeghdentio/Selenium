from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from seleniumwire import webdriver
import time
from random import*
login="your_login"
passwd="your_password"
driver = webdriver.Chrome()
driver.get("http://www.ipst.edunet.tn/login/index.php")
title = driver.title
text_box = driver.find_element(by=By.ID, value="inputName")
text_box1 = driver.find_element(by=By.ID, value="inputPassword")
text_box.send_keys(login)
text_box1.send_keys(passwd)
search_box = driver.find_element("name", "submit")
search_box.send_keys('ChromeDriver')
search_box.submit()
driver.get("http://www.ipst.edunet.tn/course/view.php?id=19357")
title = driver.title

while(True):
    n=randint(1,10)
    driver.refresh()
    time.sleep(n)
    n=randint(1,300)
    driver.get("http://www.ipst.edunet.tn/mod/assign/view.php?id=330930")
    time.sleep(n)
    driver.get("http://www.ipst.edunet.tn/course/view.php?id=19357")
    n=randint(1,300)
    driver.get("http://www.ipst.edunet.tn/mod/assign/view.php?id=333613")
    time.sleep(n)
#driver.quit()
    