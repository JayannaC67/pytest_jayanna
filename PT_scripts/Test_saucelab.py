from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pytest

'''

@pytest.fixture(scope="function")
def browser_fun(request):
    print("initiating chrome driver")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()  # instanciating Chrome driver inside driver variable
    driver.maximize_window()
    request.instance.driver = driver
    driver.maximize_window()

    yield driver

    driver.quit()
'''


@pytest.mark.usefixtures("browser_fun")
class Test_Saucelab_testing:

    def test_launch_the_application(self):

        self.driver.get("https://www.saucedemo.com/") # Using ".get" we can launch the URL.
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
        if self.driver.find_element(By.XPATH,"//input[@id='user-name']").is_displayed():
            print("logout is successfull")



