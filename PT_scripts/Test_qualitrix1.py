from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time

class Testqualitrix:

    def test_001(self):
        global driver #making driver as global variable
        chrome_options=Options()
        chrome_options.add_experimental_option("detach",True)
        driver = webdriver.Chrome()  #instanciating Chrome driver inside driver variable
        driver.get("http://qualitrix.com") # Using ".get" we can launch the URL.
        driver.maximize_window()
        driver.quit()

    def test_002(self):
        global driver  # making driver as global variable
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome()  # instanciating Chrome driver inside driver variable
        driver.get("http://facebook.com")  # Using ".get" we can launch the URL.
        driver.maximize_window()


        driver.quit()

