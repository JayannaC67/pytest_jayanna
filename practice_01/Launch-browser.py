
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Google_Automation:

    def launch_the_application(self):

        global driver #making driver as global variable
        chrome_options=Options()
        chrome_options.add_experimental_option("detach",True)
        driver = webdriver.Chrome()  #instanciating Chrome driver inside driver variable
        driver.get("http://selenium.dev") # Using ".get" we can launch the URL.
        driver.maximize_window()

    def validate_selenium_homepag(self):

        # Validate the logo
        if driver.find_element(By.XPATH, "//span[@class='navbar-logo']").is_displayed():
            print ("The selenium logo is avalilable")
        else:
            print ("The slenium logo is not available")

    def close_the_application(self):

        driver.quit()  #Using ".quit" we can quit the driver instance.


obj = Google_Automation()
obj.launch_the_application()
obj.validate_selenium_homepag()
obj.close_the_application()