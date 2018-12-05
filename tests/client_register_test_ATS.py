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
        elem = driver.find_element_by_xpath('/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[3]/a').click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("Lana")
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys("Lane")
        elem = driver.find_element_by_id("id_gender")
        elem.send_keys("Female")
        elem = driver.find_element_by_id("id_birth_date_month")
        elem.send_keys("November")
        elem = driver.find_element_by_id("id_birth_date_day")
        elem.send_keys("14")
        elem = driver.find_element_by_id("id_birth_date_year")
        elem.send_keys("1987")
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("123 N St.")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("68102")
        elem = driver.find_element_by_id("id_phone")
        elem.send_keys("4022221111")
        elem = driver.find_element_by_id("id_family_size")
        elem.send_keys("3")
        elem = driver.find_element_by_id("id_items_needed")
        elem.send_keys("Milk")
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/form/input[2]").click()
        time.sleep(2)

        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()
	