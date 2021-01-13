import pytest
from selenium import  webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time

class Test_001_Login():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserename()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homPageTitle(self,setup):
        self.logger.info("*******************Test_001_Login*****************")
        self.logger.info("******************Verify Home Page Title*****************")
        self.driver=setup
        # self.driver=init_driver
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
           assert True
           self.driver.close()
           self.logger.info("*******************Home page Title test is Passed*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homPageTitle.png")
            self.driver.close()
            self.logger.error("*******************Home page Title test is failed*****************")
            assert False

    def test_login(self,setup):
        self.logger.info("*******************Verifying Login Test*****************")
        self.driver=setup
        # self.driver=init_driver
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        time.sleep(2)
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*******************Login test is Passed*****************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("*******************Login test is failed*****************")
            assert False

