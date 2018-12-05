#Kelley Jensen
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class deleteClientTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\8210testingfolders\myvenv\Scripts\chromedriver.exe")

    def test_blog(self):
        user = "instructor"
        pwd = "development"
        driver = self.driver
        driver.maximize_window()
        #Go to website
        driver.get("https://good-shepherd-food-pantry.herokuapp.com/")
        time.sleep(2)
        #Click login button
        elem = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[5]/a").click()
        #Log in with username & password
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(2)
        # Click Management
        elem = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[6]/a").click()
        time.sleep(1)
        # Click Manage Client
        elem = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[6]/ul/li[3]/a").click()
        time.sleep(2)
        #Click delete button
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/div[3]/table/tbody/tr[6]/td[12]/a/i").click()
        time.sleep(2)
        # Are you sure window
        alert = driver.switch_to.alert
        #Yes
        alert.accept()
        time.sleep(5)

        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()
