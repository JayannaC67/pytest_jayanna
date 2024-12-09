from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Heroko_automation:


    def launch_the_application(self):
        global driver  # making driver as global variable
        driver = webdriver.Chrome()  # instanciating Chrome driver inside driver variable
        driver.get("https://the-internet.herokuapp.com/")  # Using ".get" we can launch the URL.
        driver.maximize_window()
        time.sleep(10)

    def validate_how_to_select_dropdown(self):

        driver.find_element(By.XPATH, "//a[text()='Dropdown']").click()
        driver.implicitly_wait(5)
        select = Select(driver.find_element(By.XPATH, "//select[@id='dropdown']"))

        select.select_by_visible_text("Option 1")
        time.sleep(2)

        select.select_by_visible_text("Option 2")
        time.sleep(2)

        select.select_by_index(1)
        time.sleep(2)

        select.select_by_index(2)
        time.sleep(2)

    def handling_checkboxzes(self):
        driver.find_element(By.XPATH,"//a[text()='Checkboxes']").click()
        driver.implicitly_wait(5)
        checkbox1=driver.find_element(By.XPATH,"(//input[@type='checkbox'])[1]").is_selected()
        checkbox2=driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").is_selected()
        print(checkbox1)
        print(checkbox2)
        if checkbox1==False:
            print("Checkbox is not checked")
        else:
            print("checkbox2 is checked")

        checkbox1 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
        checkbox1 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").is_selected()
        checkbox2 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").is_selected()
        print(checkbox1)
        print(checkbox2)
        if checkbox1 == False:
            print("Checkbox is not checked")
        else:
            print("checkbox2 is checked")

        checkbox1 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
        checkbox1 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").is_selected()
        checkbox2 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").is_selected()
        print(checkbox1)
        print(checkbox2)
        if checkbox1 == False:
            print("Checkbox is not checked")
        else:
            print("checkbox2 is checked")


    def close_the_application(self):
        driver.quit()  # Using ".quit" we can quit the driver instance.

obj= Heroko_automation()
obj.launch_the_application()
#obj.validate_how_to_select_dropdown()
obj.handling_checkboxzes()
obj.close_the_application()


