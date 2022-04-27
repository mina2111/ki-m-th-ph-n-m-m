from selenium import webdriver
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from POMProjectDemo.Pages.loginPage import LoginPage
from POMProjectDemo.Pages.homePage import HomePage

class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\PC\\OneDrive\\Documents\\chromedriver_win32\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def test_01_login_valid(self):
        driver = self.driver
        driver.get("https://social-network-awesome.herokuapp.com/auth/login")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()


        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)

    @classmethod
    def test_02_login_invalid_username(self):
        driver = self.driver
        driver.get("http://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        message = driver.find_element_by_xpath(By.XPATH,"").text
        self.assertEqual(message, "Invalid credentials")


        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main()













