from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import pytest

class Testherokoo:

    @pytest.mark.regression
    def test_001(self):
        global driver #making driver as global variable
        chrome_options=Options()
        chrome_options.add_experimental_option("detach",True)
        #driver = webdriver.Chrome()  #instanciating Chrome driver inside driver variable
        driver=webdriver.Edge()
        driver.get("https://the-internet.herokuapp.com/") # Using ".get" we can launch the URL.
        driver.maximize_window()
        driver.find_element(By.XPATH,"//a[text()='JavaScript Alerts']").click()
        driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
        alert=Alert(driver)
        print(alert.text)
        alert.accept()
        time.sleep(2)
        result=driver.find_element(By.XPATH,"//p[@id='result']").text
        if result=='You successfully clicked an alert':
            print("success")
        else:
            print("fail")

        driver.quit()



# pytest PT_scripts/Testalerts.py --html=PT_report/hero.html   ---cmd to run and create report file through terminal





