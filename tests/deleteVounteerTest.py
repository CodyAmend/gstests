#Vaishali Goel
import unittest
import time
from selenium import webdriver


class deleteVolunteerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\8210testingfolders\myvenv\Scripts\chromedriver.exe")

    def test_delete_volunteer(self):
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
        # Click delete button
        elem = driver.find_element_by_xpath("/html/body/section[1]/div/section/div/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[9]/a/i").click()
        time.sleep(1)
        # Switching to alert
        alert = driver.switch_to.alert
        # Accepting alert
        alert.accept()
        time.sleep(2)
        print("deleted volunteer successfully")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
