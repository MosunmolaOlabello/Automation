from selenium.webdriver import Firefox
from Library import ConfigReader

def Start_Browser():
    global driver
    driver = Firefox()
    driver.get(ConfigReader.Browser("Details","Application_URL"))
    driver.maximize_window()
    return driver


def Start_Browser2():
    global driver
    driver = Firefox()
    driver.get(ConfigReader.Browser("Details2","Application_URL"))
    driver.maximize_window()
    return driver


def EndBrowser():
    driver.close()

