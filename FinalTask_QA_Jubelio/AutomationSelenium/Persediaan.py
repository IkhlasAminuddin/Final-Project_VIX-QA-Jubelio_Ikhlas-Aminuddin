import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from PageObject import Data
from PageObject.locator import element

class Sampletest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_check_stock_iphone11(self): #Checking Stock Purple-11 Apple Iphone
        driver = self.browser
        driver.get(Data.BaseUrl)
        driver.find_element(By.NAME, element.email).send_keys(Data.Email)
        driver.find_element(By.NAME, element.password).send_keys(Data.Password)
        driver.find_element(By.CSS_SELECTOR, element.LogInButton).click()
        time.sleep(5)
        driver.find_element(By.XPATH, element.barang).click()
        time.sleep(3)
        driver.find_element(By.XPATH, element.persediaan).click()
        time.sleep(3)
        driver.find_element(By.XPATH, element.purple11).click()
        time.sleep(2)
#Validasi message popup
        message_locator = (By.XPATH, element.msgpurple11)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.text_to_be_present_in_element(message_locator, "Kronologi Barang: Purple-11 - Apple Iphone 11"))
        message = driver.find_element(*message_locator).text
        if "Kronologi Barang: Purple-11 - Apple Iphone 11" in message:
            print("message is valid!")
        else:
            print("message is not valid!")
#==========================================================================================================================#

    def test_check_stock_RMCHOIJH(self): #Checking Stock RM CHO IJH
        driver = self.browser
        driver.get(Data.BaseUrl)
        driver.find_element(By.NAME, element.email).send_keys(Data.Email)
        driver.find_element(By.NAME, element.password).send_keys(Data.Password)
        driver.find_element(By.CSS_SELECTOR, element.LogInButton).click()
        time.sleep(5)
        driver.find_element(By.XPATH, element.barang).click()
        time.sleep(3)
        driver.find_element(By.XPATH, element.persediaan).click()
        time.sleep(3)
        driver.find_element(By.XPATH, element.RMCHOIJH).click()
        time.sleep(2)
#Validasi message popup
        message_locator = (By.XPATH, element.msgRMCHOIJH)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.text_to_be_present_in_element(message_locator, "Kronologi Barang: RM-CHO-IJH - 10.4 10W40 -"))
        message = driver.find_element(*message_locator).text
        if "Kronologi Barang: RM-CHO-IJH - 10.4 10W40 -" in message:
            print("message is valid!")
        else:
            print("message is not valid!")
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()