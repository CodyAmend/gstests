#Vaishali Goel
import unittest
import time
from selenium import webdriver


class reportTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\8210testingfolders\myvenv\Scripts\chromedriver.exe")

    def test_report(self):
        user = "instructor"
        pwd = "development"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://good-shepherd-food-pantry.herokuapp.com/accounts/login/")
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(1)
        # Click Login button
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/div/form/input[2]").click()
        print("Logged In")
        time.sleep(2)
        #click reports menu
        elem = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[7]/a").click()
        time.sleep(1)
        # Click Generate reports
        elem = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[7]/ul/li/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/form/div/div[1]/input")
        elem.send_keys("2018-11-27 00:00:00")

        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/form/div/div[2]/input")
        elem.send_keys("2018-12-03 12:59:59")

        # Click on Get data button
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/form/div/div[3]/button").click()
        time.sleep(2)
        print("Report generated successfully")

        # Click on Get export to csv button
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/form/div/div[4]/input").click()
        time.sleep(2)
        print("CSV generated successfully")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
