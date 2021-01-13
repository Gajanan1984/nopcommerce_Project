from selenium import webdriver
import time
from utilities.readProperties import ReadConfig

class LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//input[@class='button-1 login-button']"
    button_logout_linktext="Logout"

    baseURL = ReadConfig.getApplicationURL()

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        time.sleep(2)
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.button_logout_linktext).click()

