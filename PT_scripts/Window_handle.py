from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
import time

@pytest.mark.usefixtures("browser_crbt")
class Test_windowhandle:

    def test_window_handle(self,readJson):
        self.driver.get(readJson['url_Practicepage'])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        #original_window = self.driver.current_window_handle

        # Store the ID of the original window
        original_window = self.driver.current_window_handle
        print(original_window)

        # Click the link which opens  a new window
        self.driver.find_element(By.XPATH, "//button[text()='Open Window']").click()
        time.sleep(1)

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                print(self.driver.current_url)
                print(self.driver.title)
                self.driver.close()
                time.sleep(2)

        self.driver.switch_to.window(original_window)
        print(self.driver.current_url)
        print(self.driver.title)

    # Handling multiple tabs in a single window
    def test_tab_handle(self, readJson):
        self.driver.get(readJson['url_Practicepage'])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        original_tab = self.driver.current_window_handle

        # Store the ID of the original window
        original_tab = self.driver.current_window_handle

        # Click the link which opens in a new window
        self.driver.find_element(By.XPATH, "//a[text()='Open Tab']").click()
        time.sleep(1)

        for tab_handle in self.driver.window_handles:
            if tab_handle != original_tab:
                self.driver.switch_to.window(tab_handle)
                print(self.driver.current_url)
                print(self.driver.title)
                self.driver.close()
                time.sleep(2)

        self.driver.switch_to.window(original_tab)
        print(self.driver.current_url)
        print(self.driver.title)





