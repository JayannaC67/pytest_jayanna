from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


class Actions_class:

    def launch_the_application(self):
        global driver

        # Set Chrome options
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # Prevents browser from closing

        # Instantiate the WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)

        # Launch the URL
        driver.get("https://www.docker.com/")
        driver.maximize_window()

        products = driver.find_element(By.XPATH, "(//a[text() = 'Products'])[1]")
        developers = driver.find_element(By.XPATH, "(//a[text() = 'Developers'])[1]")
        hover = ActionChains(driver).move_to_element(products)
        hover.perform()
        time.sleep(5)

        if driver.find_element(By.XPATH,"(//span[text()='Containerize your applications'])[1]").is_displayed():
            print("mouseover performed")
        else:
            print("Mouseover not performed")

        #Alert(driver).accept()

        #hover = ActionChains(self.driver).move_to_element(developers)
        #hover.perform()
        #time.sleep(5)

        #To perform scrolling actions
        element =driver.find_element(By.XPATH,"(//span[@class='et_pb_image_wrap '])[8]")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(5)
        if driver.find_element(By.XPATH,"(//span[@class='et_pb_image_wrap '])[8]").is_displayed():
            print("scrolldown success1")
        else:
            print("srolldown fail")

        element_logo =driver.find_element(By.XPATH, "//a[text()='Learn more about Docker']")
        actions = ActionChains(driver)
        actions.move_to_element(element_logo).perform()

        #elements= driver.find_element(By.XPATH, "//a[text()='Learn more about Docker']")
        #elements.location_once_scrolled_into_view()
        time.sleep(2)
        if driver.find_element(By.XPATH,"//li[@class='logo']/a").is_displayed():
            print("Scrollup success")
        else:
            print("Scrollup fail")

        # How to perform Right click
        logo = driver.find_element(By.XPATH, "//li[@class='logo']/a")
        (ActionChains(driver).context_click(logo).perform())
        time.sleep(2)


        ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
        driver.quit()

'''
        #for the second window.
        driver.switch_to.window(window_after)
        window_after = driver.window_handles[1]
        #for the second window.
        driver.switch_to.window(window_after)

        original_window=driver.current_window_handle()
        print(original_window)

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                print(driver.current_url)
                print(driver.title)
                driver.find_element(By.XPATH,"(//a[text()='Sign In'])[1]").click()
                driver.close()
                time.sleep(2)
        driver.switch_to.window(original_window)
        print(driver.current_url)
        print(driver.title)

        # How to handle iFrame
        # First we need to switch to the frame
        # driver.switch_to.frame(0)  # this is called switching to the 1st iFrame using index
        # driver.switch_to.frame("frame id value")  # this is called switching to the 1st iFrame using frame id
        # driver.switch_to.frame("iframe name")  # this is called switching to the 1st iFrame using iFrame-name
        # Once we move to the iFram then we can interact with the elements is present/click/select/drop down
        # How to switch back to the original page
        # driver.switch_to.default_content()

        # Selenium mouse over understanding
'''



obj= Actions_class()
obj.launch_the_application()