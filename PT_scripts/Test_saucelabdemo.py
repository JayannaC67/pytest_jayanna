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
        self.driver.get(readJson['url_saucelab'])
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # login into the app
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(readJson['username'])
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(readJson['password'])
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.implicitly_wait(5)

        if self.driver.find_element(By.XPATH, "(//button[@type='button'])[1]").is_displayed():
            print("Login successfull")
        else:
            print("Login is unsuccessfull")

        get_url=self.driver.current_url
        print(get_url)
        if get_url=="https://www.saucedemo.com/inventory.html":
            print("Valid Url")
        else:
            print("invalid url")

        get_title=self.driver.title
        print(get_title)
        if get_title=="Swag Labs":

            print("Title is valid")
        else:
            print("Invalid title")

    #def test_add_to_cart(self,readJson):
        Item_1=readJson['Item_1']
        Item_2 = readJson['Item_2']
        Item_3 = readJson['Item_3']
        self.driver.find_element(By.XPATH,"//div[text()='"+Item_1+"']/../../../div[2]//button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[text()='" + Item_2+ "']/../../../div[2]//button").click()
        time.sleep(2)

        #validate whether item is added to cart
        Item_count=self.driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']").text
        time.sleep(2)
        print(Item_count)

        if int(Item_count)==2:
            print("Items added")
        else:
            print("Items not added")

#Validation for 2 remove buttons
        removebutton_count=len(self.driver.find_elements(By.XPATH,"//button[text()='Remove']"))
        print(removebutton_count)

        if removebutton_count==2:
            print("value is correct")
        else:
            print("value is incorrect")

    #click on cart Icon

        self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
        time.sleep(2)
        if self.driver.find_element(By.XPATH,"//button[text()='Checkout']").is_displayed():
            print("cart is open")

    #to validate the items added in cart

    #to click on remove button

        self.driver.find_element(By.XPATH,"(//button[text()='Remove'])[1]").click()
        time.sleep(1)
        cart_count = len(self.driver.find_elements(By.XPATH, "//button[text()='Remove']"))
        print(cart_count)

        if cart_count == 1:
            print("Item removed")
        else:
            print("Item is not removed")
#clicking on continue shopping button

        self.driver.find_element(By.XPATH,"//button[@id='continue-shopping']").click()

#adding 2 more items to cart

        self.driver.find_element(By.XPATH, "//div[text()='" + Item_1 + "']/../../../div[2]//button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[text()='" + Item_3 + "']/../../../div[2]//button").click()
        time.sleep(1)

        # validate whether item is added to cart
        Item_count = self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
        time.sleep(2)
        print(Item_count)

        if int(Item_count) == 3:
            print("Items added")
        else:
            print("Items not added")

#click on cart Icon

        self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
        time.sleep(1)
        if self.driver.find_element(By.XPATH,"//button[text()='Checkout']").is_displayed():
            print("cart is open")
        else:
            print("cart is not opened")

#to click on checkout
        self.driver.find_element(By.XPATH,"//button[text()='Checkout']").click()
        time.sleep(1)
        if self.driver.find_element(By.XPATH,"//span[text()='Checkout: Your Information']").is_displayed():
            print("checkout page is open")
        else:
            print("checkout page is not opened")

    #to validate total price

        self.driver.find_element(By.XPATH,"//input[@id='first-name']").send_keys(readJson['First_name'])
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys(readJson['Last_name'])
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys(readJson['Zip_code'])
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(1)

        if self.driver.find_element(By.XPATH,"//span[text()='Checkout: Overview']").is_displayed():
            print("Payment page displayed")
        else:
            print("payment page not displayed")

#To validate total price


#To click on Finish button
        self.driver.find_element(By.XPATH, "//button[@id='finish']").click()
        time.sleep(2)

#to validate thank you text
        Thnkyou_text=self.driver.find_element(By.XPATH, "//h2[text()='Thank you for your order!']").text
        print(Thnkyou_text)
        if self.driver.find_element(By.XPATH,"//h2[text()='Thank you for your order!']").is_displayed():
            print("order confirmed")
        else:
            print("order is not confirmed")

#to navigate back to home page

        self.driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
        time.sleep(1)

        if self.driver.find_element(By.XPATH, "(//button[@type='button'])[1]").is_displayed():
            print("we are in homepage")
        else:
            print("we are not in homepage")

    #8th & 15 th steps incomplete
'''
1. Login to Saucelab Demo
2. Validate URL
3. Validate Page Title
4. Add any 2 items to cart
5. Validate count 2 in carts
6. Validate there are total 2 remove button
7. Click on Cart icon
8. Validate same items are added here
9. Click any remove button
10. Validate now cart count is 1
11. Click on Continue shopping
12. Add 2 more items.
13. Click on Cart icon
14. Click on Checkout
15. Validate total Price = Items Price + TAX
16. Click on Finish
17. Validate Thanks txt
18. Click on Back to Home

'''


























