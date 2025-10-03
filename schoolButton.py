from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from webhook import *
import time

path = '/snap/bin/geckodriver'
service = Service(executable_path=path)
firefox_options = Options()

# try:
#     driver = webdriver.Firefox(service=service, options=firefox_options)
# except:
#     print("failed")

# def verifyIdentity():
#     verifyButton = '//div[contains(@role, "button")]'
#     findVerifyButton = driver.find_element(
#         By.XPATH,
#         verifyButton
#     )


##/checks is there is a code if not just prints that there is not one and moves on 

def checkCodeHandle(driver):
    microsoftAuthCode = '//div[contains(@tabindex, "0")]'
    passwordError     = '//div[contains(@id, "passwordError")]'
    try:
        findMicrosoftAuthCode = driver.find_element(
            By.XPATH,
            microsoftAuthCode
        )
        upass_auth_request_message(findMicrosoftAuthCode.text)
    except: 
        try:
            driver.find_element(
            By.XPATH,
            passwordError
            )
            ### if we find this element then we bad throw exception
            raise Exception("Authentication Password failed")
        except:
            print("Looks like cookies are found Going to request page")
            noAuthRequired()




### this function is currently not being used in upass file
def staySignedInButton(driver):
    bcitStaySignedInButton     = '//input[contains(@id, "idSIButton9")]'
    findBcitStaySignInButton   = driver.find_element(
        By.XPATH,
        bcitStaySignedInButton
    )

    time.sleep(2)
    findBcitStaySignInButton.click()