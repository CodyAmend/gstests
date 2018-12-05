#Vaishali Goel
import unittest
import time
from selenium import webdriver


class editVolunteerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\8210testingfolders\myvenv\Scripts\chromedriver.exe")

    def test_edit_volunteer(self):
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
        time.sleep(2)
        # Click Login button
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/div/form/input[2]").click()
        print("Logged In")
        assert "Logged In"
        time.sleep(2)
        # click management
        elem = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[6]/a").click()
        time.sleep(1)
        # Click Manage Volunteer
        elem = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/nav/div/div[2]/ul/li[6]/ul/li[2]/a").click()
        time.sleep(2)
        # Click Edit button
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[8]/a/i").click()
        time.sleep(1)

        elem = driver.find_element_by_id("id_last_name")
        elem.clear()
        elem.send_keys("Gupta")

        elem = driver.find_element_by_id("id_gender")
        #elem.clear()
        elem.send_keys("Female")

        elem = driver.find_element_by_id("id_birth_date_month")
        #elem.clear()
        elem.send_keys("May")
        elem = driver.find_element_by_id("id_birth_date_day")
       # elem.clear()
        elem.send_keys("12")
        elem = driver.find_element_by_id("id_birth_date_year")
        #elem.clear()
        elem.send_keys("1988")

        elem = driver.find_element_by_id("id_address")
        #elem.clear()
        elem.send_keys("12146 Stone dr.")

        elem = driver.find_element_by_id("id_city")
        #elem.clear()
        elem.send_keys("Omaha")

        elem = driver.find_element_by_id("id_zipcode")
        #elem.clear()
        elem.send_keys("67891")

        elem = driver.find_element_by_id("id_phone")
        #elem.clear()
        elem.send_keys("4025673456")

        # Click Update button
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/form/input[2]").click()
        time.sleep(2)
        print("Updated volunteer successfully")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
