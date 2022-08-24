from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

""" class was created """
class main():

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Firefox()

    """ Method to Login into the given url with given credentials """
    """ NOTE you can the id and password as per your requirements """

    def open_webpage(self):
        self.driver.get(self.url)
        time.sleep(4)
        user_name = self.driver.find_element(by=By.XPATH , value="//input[@placeholder='Username']")
        user_name.send_keys("Admin")
        """Change ID HERE"""
        time.sleep(1)
        pass_word = self.driver.find_element(by=By.XPATH , value="//input[@name='password']")
        pass_word.send_keys("admin123")
        """Change PASSWORD HERE """
        time.sleep(1)
        self.driver.find_element(by=By.XPATH , value="//button[@type='submit']").click()

        x = self.driver.title
        assert x == "OrangeHRM"

        print("Login Success")


    """ Method to Create a New User by selecting Admin --> Add """

    def open_admin_add(self):
        self.open_webpage()

        time.sleep(2)

        """ Click on Admin """
        self.driver.find_element(by=By.XPATH , value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        time.sleep(3)

        """ Click on add """
        self.driver.find_element(by=By.XPATH , value="//button[normalize-space()='Add']").click()
        time.sleep(2)

        user_role = self.driver.find_element(by=By.XPATH , value="//div[contains(text(),'-- Select --')]")
        user_role.click()
        time.sleep(1)

        admin = self.driver.find_element(by=By.XPATH , value="//span[contains(text(),'Admin')]")
        admin.click()
        time.sleep(2)

        employee_name = self.driver.find_element(by=By.XPATH , value="//input[@placeholder='Type for hints...']")
        employee_name.send_keys("santosh")
        time.sleep(2)

        status_code = self.driver.find_element(by=By.XPATH , value="//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]")
        status_code.click()
        time.sleep(1)

        enabled_button = self.driver.find_element(by=By.XPATH , value="//span[normalize-space()='Enabled']")
        enabled_button.click()
        time.sleep(2)

        username = self.driver.find_element(by=By.XPATH , value="//div[@class='oxd-form-row']//div[@class='oxd-grid-2 orangehrm-full-width-grid']//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
        username.send_keys("santosh_kumar")
        time.sleep(2)

        password =  self.driver.find_element(by=By.XPATH , value="//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']")
        password.send_keys("Santosh@94")
        time.sleep(1)

        confirm_password = self.driver.find_element(by=By.XPATH , value="//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']")
        confirm_password.send_keys("Santosh@94")
        time.sleep(1)

        save_button = self.driver.find_element(by=By.XPATH , value="//button[normalize-space()='Save']")
        save_button.click()

        time.sleep(3)

        print("Create user Success")

        self.log_out()


    """ Method For Logout """
    
    def log_out(self):
        time.sleep(2)

        self.driver.find_element( by=By.XPATH , value="//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
        time.sleep(1)

        self.driver.find_element(by=By.XPATH , value="//a[normalize-space()='Logout']").click()

        time.sleep(2)

        self.driver.close()

        print("Logout Success")

s = main()

s.open_admin_add()

