from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# x = 384000
x = 384000
i = 33100

while(i <= x ):
# for t in range(i, i+100):
    driver = webdriver.Firefox()
    driver.get("http://gfy.com")

    username = driver.find_element_by_id("navbar_username")
    password = driver.find_element_by_id("navbar_password")

    username.send_keys("johnnyloadproductions")
    time.sleep(1)
    password.send_keys("Supermon12")
    time.sleep(1)

    login_form = driver.find_element_by_xpath("//input[@value='Log in']")
    time.sleep(1)
    login_form.click()
    time.sleep(5)

    for t in range(i, i+10000):
        string = "http://gfy.com/member.php?u={}".format(t)
        driver.get(string)


        f = open("/Users/andrewsyc/Desktop/gfyprofiles/{}.html".format(t),"wb+")
        f.write(driver.page_source)
        f.close()

    driver.close()
    i += 10000
    time.sleep(3)

time.sleep(3)

# driver.close()