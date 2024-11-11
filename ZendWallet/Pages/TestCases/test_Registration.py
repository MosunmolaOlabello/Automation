from selenium.webdriver import Firefox
from Base import InitiateBrowser
from Pages import RegistrationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

def test_TC_Reg_001():
    driver = Firefox()
    driver.get("https://www.zendwallet.com/")
    act = ActionChains(driver)
    act.click(driver.find_element(By.XPATH,"//button[text()='Create Account']")).perform()

def test_TC_Reg_002():
    driver = InitiateBrowser.Start_Browser()
    register = RegistrationPage.Registration(driver)
    register.enter_email_name("ayobamiolabello@gmail.com")
    register.enter_firstname_name("Mosunmola")
    register.enter_lastname_name("Olabello")
    register.enter_username_name("Mosbel")
    register.enter_password_name("Mosunbaby&9")
    obj = Select(driver.find_element(By.NAME,"country"))
    obj.select_by_visible_text("Nigeria")
    register.enter_referral_code("299288")
    driver.find_element(By.XPATH, "//span[@class='chakra-checkbox__control css-1gtsxek']").click()

def test_TC_Reg_003():
    driver = InitiateBrowser.Start_Browser()
    register = RegistrationPage.Registration(driver)
    register.enter_email_name("olabellomosunmola@gmail.com")
    register.enter_firstname_name("Mosunmola")
    register.enter_lastname_name("Olabello")
    register.enter_username_name("Mosbel")
    register.enter_password_name("Mosunbaby&9")
    obj = Select(driver.find_element(By.NAME, "country"))
    obj.select_by_visible_text("Nigeria")
    driver.find_element(By.XPATH, "//span[@class='chakra-checkbox__control css-1gtsxek']").click()
    driver.find_element(By.XPATH,"//button[text()='Create Account']").click()

def test_TC_Reg_004():
    driver = InitiateBrowser.Start_Browser()
    register = RegistrationPage.Registration(driver)
    register.enter_email_name("olabellomosunmola")
    register.enter_username_name("joy")

def test_TC_Reg_005():
    driver = InitiateBrowser.Start_Browser()
    register = RegistrationPage.Registration(driver)
    register.enter_password_name("Mosun")
    register.enter_username_name("joy")

def test_TC_Reg_006():
    driver = InitiateBrowser.Start_Browser()
    driver.find_element(By.XPATH,"//button[text()= 'Create Account']").click()

def test_TC_Reg_007():
    driver = InitiateBrowser.Start_Browser()
    driver.find_element(By.XPATH, "//span[@class='chakra-checkbox__control css-1gtsxek']").click()
    driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

def test_TC_Reg_008():
    driver = InitiateBrowser.Start_Browser()
    register = RegistrationPage.Registration(driver)
    register.enter_email_name("ayobamiolabello@gmail.com")
    register.enter_firstname_name("Mosunmola")
    register.enter_lastname_name("Olabello")
    register.enter_username_name("Aybel")
    register.enter_password_name("Mosunbaby&9")
    obj = Select(driver.find_element(By.NAME, "country"))
    obj.select_by_visible_text("Nigeria")
    driver.find_element(By.XPATH, "//span[@class='chakra-checkbox__control css-1gtsxek']").click()
    driver.find_element(By.XPATH,"//button[text()='Create Account']").click()

def test_TC_Reg_009():
    driver = InitiateBrowser.Start_Browser()
    driver.find_element(By.XPATH,"//span[text()='Login']").click()