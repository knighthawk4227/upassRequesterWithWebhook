from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select

path = '/snap/bin/geckodriver'
service = Service(executable_path=path)
firefox_options = Options()

try:
    driver = webdriver.Firefox(service=service, options=firefox_options)
except:
    print("failed")

def verifyIdentity():
    verifyButton = '//div[contains(@role, "button")]'
    findVerifyButton = driver.find_element(
        By.XPATH,
        verifyButton
    )
    