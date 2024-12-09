
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Saucelabpractice:
    def launch_the_application(self):

        global driver # making driver as global variable
        driver = webdriver.Chrome()  # instanciating Chrome driver inside driver variable
        driver.get("https://www.saucedemo.com/") # Using ".get" we can launch the URL.
        driver.maximize_window()
        time.sleep(5)

    def validate_saucelab_homepag(self):

        # Validate the logo
        if driver.find_element(By.XPATH, "//div[@class='login_logo']").is_displayed():
            print ("The saucelab logo is avalilable")
        else:
            print ("The saucelab logo is not available")

        time.sleep(2)

    def login(self):
        driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        driver.implicitly_wait(5)

        if driver.find_element(By.XPATH, "(//button[@type='button'])[1]").is_displayed():
            print("Login successfull")
        else:
            print("Login is unsuccessfull")

    def clicking_hamberger(self):
        driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()
        time.sleep(2)
    def clicking_logout(self):
        driver.find_element(By.XPATH, "//a[text()='Logout']").click()
        time.sleep(2)

        if driver.find_element(By.XPATH,"//input[@id='user-name']").is_displayed():
            print("logout is successfull")
    def close_the_application(self):
        driver.quit()  # Using ".quit" we can quit the driver instance.

obj=Saucelabpractice()
obj.launch_the_application()
obj.validate_saucelab_homepag()
obj.login()
obj.clicking_hamberger()
obj.clicking_logout()
obj.close_the_application()

