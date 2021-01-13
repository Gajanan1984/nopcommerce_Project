from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='firefox':
        driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver-win64\\geckodriver.exe")
    elif browser=='ie':
        driver=webdriver.Ie()
    else:
        driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    return driver

def pytest_addoption(parser): # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
    return request.config.getoption("--browser")


######################   Pytest HTML Report     ########################

# It is hook for Adding Environment Info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Custmores'
    config._metadata['Tester'] = 'Gajanan'

# It is hook for Delete/Modify Environment Info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)





# @pytest.fixture(params=["chrome"],scope='class')
# def init_driver(request):
#     if request.param=="chrome":
#         web_driver=webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
#     elif request.param=="firefox":
#         web_driver=webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
#     request.cls.driver=web_driver
#     yield
#     web_driver.close()







