from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# x is the starting value, under 400k profiles at the time of this scrape
x = 384000
# i is the starting value
i = 1

while(i <= x ):
#Firefox used
    driver = webdriver.Firefox()
    # base url
    driver.get("http://gfy.com")

    username = driver.find_element_by_id("navbar_username")
    password = driver.find_element_by_id("navbar_password")

# password and username need to go into these values 
    username.send_keys("username")
    time.sleep(1)
    password.send_keys("password")
    time.sleep(1)

    login_form = driver.find_element_by_xpath("//input[@value='Log in']")
    time.sleep(1)
    login_form.click()
    time.sleep(5)

    for t in range(i, i+10000):
        string = "http://gfy.com/member.php?u={}".format(t)
        driver.get(string)

        # make sure to pick the correct directory to save the files to
        f = open("/directorytosave/{}.html".format(t),"wb+")
        f.write(driver.page_source)
        f.close()

    driver.close()
    i += 10000
    time.sleep(3)

time.sleep(3)

driver.close()
