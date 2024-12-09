
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
import time

@pytest.mark.usefixtures("browser_crbt")
class Test_Saucelabscenario:
    global driver
    @pytest.mark.endtoend
    def test_launch_the_application(self, readJson):
        self.driver.get(readJson['Test_automation'])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # login into the app