#import sys
#rom pathlib import Path
#sys.path.append(str(Path(__file__).parent.parent))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
import time



@pytest.mark.usefixtures("browser_crbt")
class TestDemo_Selenium():

    @pytest.mark.smoke
    def test_docker_HomePage_Scenarios(self):

        self.driver.get("https://www.docker.com/")
        self.driver.implicitly_wait(20)


        if self.driver.find_element(By.XPATH, "//li[@class='logo']").is_displayed():
            print("Logo is present....")
        else:
            print("Logo is not present....")

    @pytest.mark.smoke
    def test_docker_HomePage_Scenarios1(self):

        self.driver.get("https://www.docker.com/")
        self.driver.implicitly_wait(20)
        if self.driver.find_element(By.XPATH, "//li[@class='logo']").is_displayed():
            print("Logo is present....")
        else:
            print("Logo is not present....")

    @pytest.mark.smoke
    def test_docker_HomePage_Scenarios3(self):
        self.driver.get("https://www.docker.com/")
        if self.driver.find_element(By.XPATH, "//li[@class='logo']").is_displayed():
            print("Logo is present....")
        else:
            print("Logo is not present....")

    @pytest.mark.smoke
    def test_launch_the_application(self):

        self.driver.get("https://www.saucedemo.com/")  # Using ".get" we can launch the URL.
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # login into the app
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.implicitly_wait(5)

        if self.driver.find_element(By.XPATH, "(//button[@type='button'])[1]").is_displayed():
            print("Login successfull")
        else:
            print("Login is unsuccessfull")

        self.driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()
        time.sleep(2)
        if self.driver.find_element(By.XPATH, "//input[@id='user-name']").is_displayed():
            print("logout is successfull")



    # pytest PT_scripts/ --html=PT_report/hero1234.html --browser=edge -k regression  --to run ant scripts from test
