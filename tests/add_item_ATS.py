#Scott Poulin
import unittest
import time
from selenium import webdriver

class GS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\8210testingfolders\myvenv\Scripts\chromedriver.exe")

    def test_additem(self):
        item = 'Peanut Butter'
        desc = 'Peter Pan'
        quantity = '1'
        user = 'cjenewein'
        password = 'development'
        driver = self.driver
        driver.maximize_window()
        driver.get("https://good-shepherd-food-pantry.herokuapp.com/")
        # driver.get("http://127.0.0.1:8000")
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div/p[2]/a[1]").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(password)
        driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/div/form/input[2]").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[6]/a").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/div[2]/a/span/i").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_item_name")
        elem.send_keys(item)
        elem = driver.find_element_by_id("id_description")
        elem.send_keys(desc)
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys(quantity)
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/form/input[2]").click()
        time.sleep(5)
        assert "Created Item"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()