#Caroline Jenewein
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\8210testingfolders\myvenv\Scripts\chromedriver.exe")

    def test_resetpassword(self):
        email = "cjenewein@unomaha.edu"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://good-shepherd-food-pantry.herokuapp.com/")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[5]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/div/p/a").click()
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(email)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        driver = self.driver
        driver.get("https://mailtrap.io/")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/header/div/div[2]/div/a[1]").click()
        elem = driver.find_element_by_id("user_email")
        elem.send_keys("cjenewein@unomaha.edu")
        elem = driver.find_element_by_id("user_password")
        elem.send_keys("development")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr/td[1]/div[1]/strong/a/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div/ul/li[1]").click()
        time.sleep(1)
        driver.get("https://good-shepherd-food-pantry.herokuapp.com/accounts/reset/Mg/test")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/p[2]/a").click()
        time.sleep(2)
        assert "Reset password"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()