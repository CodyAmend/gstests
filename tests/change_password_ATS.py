#Caroline Jenewein
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\8210testingfolders\myvenv\Scripts\chromedriver.exe")
    def test_changepassword(self):
        user = "cjenewein"
        pwd = "development"
        new_pwd = "instructor"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://good-shepherd-food-pantry.herokuapp.com/")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[5]/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[9]/a").click()
        driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[9]/ul/li[3]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_old_password")
        elem.send_keys(pwd)
        elem = driver.find_element_by_id("id_new_password1")
        elem.send_keys(new_pwd)
        elem = driver.find_element_by_id("id_new_password2")
        elem.send_keys(new_pwd)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "Changed password"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()