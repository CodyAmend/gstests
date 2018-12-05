#Cody Amend
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\8210testingfolders\myvenv\Scripts\chromedriver.exe")

    def test_blog(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://good-shepherd-food-pantry.herokuapp.com/")
        time.sleep(2)
        elem = driver.find_element_by_xpath('/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[5]/a').click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("cjenewein")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("development")
        time.sleep(2)
        elem = driver.find_element_by_xpath(
            "/html/body/section[1]/div/section/div/div/div/div[2]/div/div/form/input[2]").click()
        assert "Logged In"
        time.sleep(2)
        elem = driver.find_element_by_xpath(
            "/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[5]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("Clint")
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys("Eastwood")
        elem = driver.find_element_by_xpath(
            "/html/body/section[1]/div/section/div/div/div/div[2]/div/form/button").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath(
            "/html/body/section[1]/div/section/div/div/div/div[2]/div/form/input").click()
        time.sleep(4)
        elem = driver.find_element_by_xpath(
            "/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[9]/a").click()
        elem = driver.find_element_by_xpath(
            "/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[9]/ul/li[4]/a").click()
        assert "Logged Out"
        time.sleep(2)




        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()
