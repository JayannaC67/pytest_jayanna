
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class Qualitrix_automation:


    def launch_the_application(self):
        global driver  # making driver as global variable
        driver = webdriver.Chrome()  # instanciating Chrome driver inside driver variable
        driver.get("https://qualitrix.com/")  # Using ".get" we can launch the URL.
        driver.maximize_window()
        time.sleep(3)
       # title=driver.title()
        #print(driver.title())

    #def validate_qualitrix_homepag(self):

        # Validate the logo
        if driver.find_element(By.XPATH, "//img[contains(@alt,'Best automation testing')]").is_displayed():
            print("The Qualitrix logo is avalilable")
        else:
            print("The Qualitrix logo is not available")

    #to count the main menu
        count_mainmenu=len(driver.find_elements(By.XPATH,"//ul[@id='menu-the-main-menu']/li"))
        print(count_mainmenu)
        #print(driver.title())
        time.sleep(2)
        if count_mainmenu==8:
            print("success")
        else:
            print("fail")

        count_company_tabs=len(driver.find_elements(By.XPATH,"//ul[h4[text()='Company ']]/li"))
        print(count_company_tabs)

obj=Qualitrix_automation()
obj.launch_the_application()
#obj.validate_qualitrix_homepag()

