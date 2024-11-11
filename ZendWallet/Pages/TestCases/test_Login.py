from selenium.webdriver import Firefox
from Pages import LoginPage
from Base import InitiateBrowser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_TC_Log_001():
    driver = Firefox()
    driver.get("https://www.zendwallet.com/")
    obj = ActionChains(driver)
    obj.click(driver.find_element(By.XPATH,"//button[text()='Login']")).perform()
    assert driver.current_url == "https://www.zendwallet.com/"


def test_TC_Log_002():
    driver = InitiateBrowser.Start_Browser2()
    Login = LoginPage.Login(driver)
    Login.enter_email_name("Ayobamiolabello@gmail.com")
    Login.enter_password_name("Mosunbaby&9")


def test_TC_Log_003():
    driver = InitiateBrowser.Start_Browser2()
    Login = LoginPage.Login(driver)
    Login.enter_email_name("olabellomosunmola@gmail.com")
    Login.enter_password_name("Mosunbaby&9")
    driver.find_element(By.XPATH,"//button[text()='Login']").click()



def test_TC_Log_005():
    driver = InitiateBrowser.Start_Browser2()
    Login = LoginPage.Login(driver)
    Login.enter_email_name("OlaBellomOsunMola@gmAil.com")
    Login.enter_password_name("Mosunbaby&9")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()


def test_TC_Log_006():
    driver = InitiateBrowser.Start_Browser2()
    Login = LoginPage.Login(driver)
    Login.enter_email_name("olabellomosunmola@gmail.com")
    Login.enter_password_name("Mosunbaby&2")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()


def test_TC_Log_007():
    driver = InitiateBrowser.Start_Browser2()
    Login = LoginPage.Login(driver)
    Login.enter_email_name("ayobamiolabello@gmail.com")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()


def test_TC_Log_008():
    driver = InitiateBrowser.Start_Browser2()
    Login = LoginPage.Login(driver)
    Login.enter_password_name("Mosunbaby&2")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()


def test_TC_Log_009():
    driver = InitiateBrowser.Start_Browser2()
    Login = LoginPage.Login(driver)
    Login.enter_email_name("olabelomosunm@gmail.com")
    Login.enter_password_name("Mosunbaby&2")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()