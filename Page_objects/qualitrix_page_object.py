from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.color import Color
from selenium.webdriver.chrome.options import Options
import pytest
import time
from Locators import Qualitrix_home
from Locators.Qualitrix_home import company_tab
from Page_objects import common
from Locators import Table
from selenium.webdriver.common.action_chains import ActionChains

class Qualitrix_page_object:

    def __init__(self, driver):
        self.driver = driver

    def launch_the_app(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        print("Qualitrix Application is launched Successfully ... ..... PASS")

    def Validate_header_menu(self):
        assert len(self.driver.find_elements(By.XPATH, Qualitrix_home.Qualitrix_logo())) == 1
        assert self.driver.find_element(By.XPATH, Qualitrix_home.Qualitrix_logo()).is_displayed() == True
        print ("Qualitrix logo is present")

    def closing_browser(self):
        self.driver.quit()


    def launch_saucelab(self, url):
        self.driver.get(url)
        time.sleep(2)
        print("saucelab launched")

    def login_cred(self, readJson):
        self.driver.find_element(By.XPATH, Qualitrix_home.saucelab_username()).send_keys("standard_user")
        time.sleep(1)
        self.driver.find_element(By.XPATH, Qualitrix_home.saucelab_pwd()).send_keys("secret_sauce")
        time.sleep(1)
        self.driver.find_element(By.XPATH, Qualitrix_home.saucelab_login()).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Qualitrix_home.sauce_homepage()).is_displayed()
        print("Login successfull")


    def validate_buttoncolor(self):
        #validate getaquote button text color and background color
        Get_quote=self.driver.find_element(By.XPATH,Qualitrix_home.Get_a_quote())
        Get_a_quote_color=Get_quote.value_of_css_property("color")
        Get_quote_bgcolor = Get_quote.value_of_css_property("background-color")

       # print("Get a quote button text is" + Get_a_quote_color)
       # print("Getaquote buttonbgcolor is" + Get_quote_bgcolor)

        #print(Color.from_string(Get_a_quote_color).hex)
        #print(Color.from_string(Get_quote_bgcolor).hex)

        print("Get a quote button text is" + common.color_picker(Color.from_string(Get_a_quote_color).hex))
        print("Getaquote buttonbgcolor is" + common.color_picker(Color.from_string(Get_quote_bgcolor).hex))



        padding=Get_quote.value_of_css_property("padding")
        print(padding)
        text_align = Get_quote.value_of_css_property("text-align")
        print(text_align)


        # company tab
        company=self.driver.find_element(By.XPATH, Qualitrix_home.company_tab())
        padding = company.value_of_css_property("padding")
        print(padding)
        font_size = company.value_of_css_property("font-size")
        print(font_size)

        print("Company cladding detail is:" + common.company("padding"))
        print("Company cladding detail is:" + common.company("font-size"))

        assert font_size==common.company("font-size")



    def launchh_the_app(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        print("practice automation Application is launched Successfully ... ..... PASS")









