#Kelley Jensen
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class editClientTest(unittest.TestCase):

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
        #Click edit button
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/div[3]/table/tbody/tr[2]/td[11]/a/i").click()
        time.sleep(2)
        #Edit client info
        elem = driver.find_element_by_id("id_last_name")
        elem.clear()
        elem.send_keys("Rodriguez")
        elem = driver.find_element_by_id("id_address")
        elem.clear()
        elem.send_keys("4435 Pine St.")
        elem = driver.find_element_by_id("id_zipcode")
        elem.clear()
        elem.send_keys("68122")
        elem = driver.find_element_by_id("id_phone")
        elem.clear()
        elem.send_keys("4021598753")
        time.sleep(2)
        #Click update button
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/form/input[2]").click()
        time.sleep(2)


        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()

