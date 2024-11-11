from Base import InitiateBrowser
from Library import ConfigReader
from selenium.webdriver.common.by import By

class Login:
    def __init__(self,obj):
        global driver
        driver = obj

    def enter_email_name(self,email):
        driver.find_element(By.NAME,ConfigReader.Element("Elements","email_name")).send_keys(email)

    def enter_password_name(self,password):
        driver.find_element(By.NAME,ConfigReader.Element("Elements", "password_name")).send_keys(password)

    def enter_new_password_name(self,newpassword):
        driver.find_element(By.NAME,ConfigReader.Element("Elements","new_password")).send_keys(newpassword)

    def enter_confirm_password_name(self,confirmpassword):
        driver.find_element(By.NAME,ConfigReader.Element("Elements","confirm_password")).send_keys(confirmpassword)