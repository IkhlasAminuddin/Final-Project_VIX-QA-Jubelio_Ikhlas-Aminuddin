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
    
    def test_atur_stock(self):
        driver = self.browser
        driver.get(Data.BaseUrl)
        driver.find_element(By.NAME, element.email).send_keys(Data.Email)
        driver.find_element(By.NAME, element.password).send_keys(Data.Password)
        driver.find_element(By.CSS_SELECTOR, element.LogInButton).click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/nav[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/nav[1]/div[1]/div[1]/ul[1]/li[2]/ul[1]/li[2]/a[1]/span[1]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[1]/span[1]/div[1]/label[1]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[6]/div[1]/div[1]/span[1]/div[1]/label[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/span[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[11]/div[1]/input[1]").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div[class='pull-right drop-up'] span[class='ladda-label']").click()
        time.sleep(3)
#Validasi error message
        error_message_locator = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/li[1]")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element(error_message_locator, "Qty adjustment tidak boleh yang kosong"))

        # Validate the error message
        error_message = driver.find_element(*error_message_locator).text
        if "Qty adjustment tidak boleh yang kosong" in error_message:
            print("Error message is valid!")
        else:
            print("Error message is not valid!")


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()