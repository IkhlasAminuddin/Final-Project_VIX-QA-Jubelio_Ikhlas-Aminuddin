import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject import Data
from PageObject.locator import element


class Sampletest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_success_login(self):
        driver = self.browser
        driver.get(Data.BaseUrl)
        driver.find_element(By.NAME, element.email).send_keys(Data.Email)
        driver.find_element(By.NAME, element.password).send_keys(Data.Password)
        driver.find_element(By.CSS_SELECTOR, element.LogInButton).click()
        time.sleep(4)
#Validasi        
        currentUrl = driver.current_url
        self.assertIn (currentUrl, Data.BaseUrl + "/home/getting-started")

    def test_failed_login_wrong_password(self):
        driver = self.browser
        driver.get(Data.BaseUrl)
        driver.find_element(By.NAME, element.email).send_keys(Data.Email)
        driver.find_element(By.NAME, element.password).send_keys(Data.PassSalah)
        driver.find_element(By.CSS_SELECTOR, element.LogInButton).click()
        time.sleep(4)
#Validasi Password atau email anda salah
        error_message_locator = (By.XPATH, "//div[@id='root']//div[@role='alert']/li")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element(error_message_locator, "Password atau email anda salah"))

        error_message = driver.find_element(*error_message_locator).text
        if "Password atau email anda salah" in error_message:
            print("Error message is valid!")
        else:
            print("Error message is not valid!")

    
    def test_failed_login_blankfield(self):
        driver = self.browser
        driver.get(Data.BaseUrl)
        driver.find_element(By.NAME, element.email).send_keys("")
        driver.find_element(By.NAME, element.password).send_keys("")
        driver.find_element(By.CSS_SELECTOR, element.LogInButton).click()
        time.sleep(4)
#Validasi : Email harus diisi. Password harus diisi.

    def test_failed_login_nonvalidemail(self):
        driver = self.browser
        driver.get(Data.BaseUrl)
        driver.find_element(By.NAME, element.email).send_keys(Data.nonvalidemail)
        driver.find_element(By.NAME, element.password).send_keys(Data.Password)
        driver.find_element(By.CSS_SELECTOR, element.LogInButton).click()
        time.sleep(4)
#Validasi : Format email tidak valid
        error_message_locator = (By.XPATH, "//div[@id='root']//div[@role='alert']/li")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element(error_message_locator, "Format Email tidak valid"))

        # Validate the error message
        error_message = driver.find_element(*error_message_locator).text
        if "Format Email tidak valid" in error_message:
            print("Error message is valid!")
        else:
            print("Error message is not valid!")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()