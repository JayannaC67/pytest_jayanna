from http.server import executable

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class launch_google:

    def googlewebsite_launching(self):

        global driver
        driver=webdriver.Chrome()

        option=webdriver.ChromeOptions()
        option.add_experimental_option("detach",True)

        driver.get("https://google.com")
        driver.maximize_window()
        driver.implicitly_wait(5)
        #time.sleep(5)
        #driver.find_element(By.XPATH,"//textarea[@aria-label='Search']").send_keys("https://facebook.com")
        driver.find_element(By.XPATH,"//textarea[@class='gLFyf']").send_keys("facebook.com")

        driver.find_element(By.XPATH,"(//input[@value='Google Search'])[2]").click()
        time.sleep(5)




google=launch_google()
google.googlewebsite_launching()



