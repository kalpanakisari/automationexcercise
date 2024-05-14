import time
import pytest
from selenium.webdriver.common.by import By


from pageobjects.Register import Register_page
from utils.baseclass import BaseClass


@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_autoexc(self):
        # wait scenario
        time.sleep(2)

        print("product cart logic")
        rg = Register_page(self.driver)
        #lp.search_data_textBox().send_keys("@#$%") screenshot scenario
        rg.search_data_textBox().send_keys("ber")

        time.sleep(2)
        # results = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")
        count = len(lp.add_button_list())
        print(count)
        assert count > 0
        #add to cart buttons
        for result in rg.add_button_list():
            result.find_element(By.XPATH, "div/button").click()

        # cart image button code
        rg.cart_button_met().click()

        # proceed checkout button
        rg.proceed_button_met().click()

        time.sleep(5)

        # promo code textbox
        rg.promo_textbox_met().send_keys("rahulshettyacademy")

        # Apply button
        rg.apply_button_met().click()

        #assert 4==5

    #def test_google(self):
        #print('ji..')

