
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

class Test_qualitrix:

    def test_printlinks(self):
        global driver #making driver as global variable
        chrome_options=Options()
        chrome_options.add_experimental_option("detach",True)
        driver = webdriver.Chrome()  #instanciating Chrome driver inside driver variable
        driver.get("https://qualitrix.com") # Using ".get" we can launch the URL.
        driver.maximize_window()

        total_links_count = len(driver.find_elements(By.XPATH, "//a"))

        for i in range(1, total_links_count + 1):
            xpath = '(//a)[' + str(i) + ']'
            # print(xpath)

            link_name = driver.find_element(By.XPATH, xpath).text
            print("when the value of i is :" + str(i) + " " + "the value of the text is : " + link_name)

        driver.quit()
# pytest PT_scripts/Test_qualiutrix.py --html=PT_report/links.html----This is the cmd used to print links report



