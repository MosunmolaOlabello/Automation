from Base import InitiateBrowser
from Library import ConfigReader
from selenium.webdriver.common.by import By


class Registration:
    def __init__(self,obj):
        global driver
        driver = obj

    def enter_email_name(self,email):
        driver.find_element(By.NAME,ConfigReader.Element("Elements","email_name")).send_keys(email)

    def enter_firstname_name(self,firstname):
        driver.find_element(By.NAME,ConfigReader.Element("Elements","firstname_name")).send_keys(firstname)

    def enter_lastname_name(self,lastname):
        driver.find_element(By.NAME,ConfigReader.Element("Elements","lastname_name")).send_keys(lastname)

    def enter_username_name(self,username):
        driver.find_element(By.NAME,ConfigReader.Element("Elements","username_name")).send_keys(username)

    def enter_password_name(self,password):
        driver.find_element(By.NAME,ConfigReader.Element("Elements","password_name")).send_keys(password)

    def enter_referral_code(self,referralcode):
        driver.find_element(By.NAME,ConfigReader.Element("Elements","referral_code")).send_keys(referralcode)

