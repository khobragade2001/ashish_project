# import time
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select

class test_registration:
    def test_login(self):
        d = webdriver.Chrome()
        d.maximize_window()
        x = By.XPATH
        ## go to url
        d.get("https://demo.nopcommerce.com/login").click()
        d.find_element(x, "//button[normalize-space()='Register']").click()
        time.sleep(2)



