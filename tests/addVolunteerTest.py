#Vaishali Goel
import unittest
import time
from selenium import webdriver


class addVolunteerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\8210testingfolders\myvenv\Scripts\chromedriver.exe")

    def test_add_volunteer(self):
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
        assert "Logged In"
        time.sleep(2)
        #click management
        elem = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[6]/a").click()
        time.sleep(1)
        # Click Manage Volunteer
        elem = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[6]/ul/li[2]/a").click()
        time.sleep(2)
        # Click Add Volunteer button
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/a/span/i").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("Vaish0061")

        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("Vaishali")

        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys("Goel")

        elem = driver.find_element_by_id("id_email")
        elem.send_keys("vgoel@unomaha.edu")

        elem = driver.find_element_by_id("id_password1")
        elem.send_keys("test0061")

        elem = driver.find_element_by_id("id_password2")
        elem.send_keys("test0061")

        # Click Add button on Add volunteer
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/form/input[2]").click()
        time.sleep(2)
        print("Added volunteer successfully")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
