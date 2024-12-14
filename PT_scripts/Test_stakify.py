import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
from Page_objects.Stackify_page_objects import Stakifyy_page_object


@pytest.mark.usefixtures("browser_crbt")
class Test_Stakify_e2e:

    def test_homepage_validation(self, readJson):
        homepage = Stakifyy_page_object(self.driver)  # Activating the driver which we have created in supporting file (qualitrix_page_object.py).
        homepage.launch_the_app(readJson['stakify_url'])
        homepage.validate_headermenu()
        homepage.test_mouseoveraction()
        homepage.test_languages()
        homepage.test_click_ruby()
        homepage.test_validate_checkboxes()
        homepage.click_reviewdoclink()
        homepage.test_validating_buttons()
        homepage.test_schedule_demo()
        homepage.test_fillthe_details(readJson)



