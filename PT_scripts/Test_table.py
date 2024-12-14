
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
import time
from Locators import Table
from Page_objects.qualitrix_page_object import Qualitrix_page_object

@pytest.mark.usefixtures("browser_crbt")
class Test_table:
    global driver
    @pytest.mark.endtoend
    def test_launch_the_application(self, readJson):
        homepage = Qualitrix_page_object(self.driver)
        homepage.launchh_the_app(readJson["url_practiceautomation"])
        # login into the app

    def get_bookdetail(self, Bname, coln):
        self.book=Bname
        self.column=coln


getname=Test_table()
getname.selenium()