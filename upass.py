from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import os
from dotenv import load_dotenv
from schoolButton import *
import time

url = 'https://upassbc.translink.ca/'
path = '/snap/bin/geckodriver'
service = Service(executable_path=path)
firefox_options = Options()
load_dotenv()
#Below is for headless running end product I will activate this.
firefox_options.add_argument("--headless")

instock = False

try:
    driver = webdriver.Firefox(service=service, options=firefox_options)
    print("running search now")
    driver.get(url)

    time.sleep(3)

    #Buttons for Upass site itself
    selectSchoolButton  = '//select[contains(@class, "select-css")]'  
    postSecondaryButton = f'//option[contains(@value, "{os.getenv("SCHOOL_VALUE")}")]'
    nextPageButton      = '//input[contains(@id, "goButton")]'

    findPostSecondaryElement = driver.find_element(
        By.XPATH,
        postSecondaryButton)
    
    findSchoolButton = driver.find_element(
        By.XPATH, 
        selectSchoolButton
    )

    findNextPageButton = driver.find_element(
        By.XPATH,
        nextPageButton
    )

    selectPostSecondaryElement = Select(findSchoolButton)    

    selectPostSecondaryElement.select_by_value(os
                     .getenv("SCHOOL_VALUE"))
    
    selectNextPageButtonElement = findNextPageButton.click()

    ## This has to be below cause we need to wait to look for thsi till after the redirect
    ## I assume I could turn this into another file or function which I might do later
    time.sleep(3)
    ## Bcit login page
    bcitLoginInputField = '//input[contains(@type, "email")]'
    bcitNextButton      = '//input[contains(@type, "submit")]'
    bcitPasswordField   = '//input[contains(@type, "password")]'

    findBcitLoginField    = driver.find_element(
        By.XPATH,
        bcitLoginInputField
    )
    findBcitNextButton    = driver.find_element(
        By.XPATH,
        bcitNextButton
    )
    findBcitPasswordField = driver.find_element(
        By.XPATH,
        bcitPasswordField
    )

    inputBcitEmailIntoField    = findBcitLoginField.send_keys(os.getenv("SCHOOL_EMAIL"))
    clickBcitNextButton        = findBcitNextButton.click()
    inputBcitPasswordIntoField = findBcitPasswordField.send_keys(os.getenv("SCHOOL_PASSWORD")) 
    
    ## if you do not wait tried to find element too soon 
    ## and crashes depending on internet connection change this
    time.sleep(2)

    ## Bcit login Page
    bcitSignInButton      = '//input[contains(@id, "idSIButton9")]'
    findBcitSignInButton  = driver.find_element(
        By.XPATH,
        bcitSignInButton
    )
    clickBcitSignInButton = findBcitSignInButton.click()

    ## if you do not wait tried to find element too soon 
    ## and crashes depending on internet connection change this
    time.sleep(2)

    ## Microsoft Auth code section.
    checkCodeHandle(driver)

    print("Page Auth Yes button")

    try:
        current_url = driver.current_url
        WebDriverWait(driver, 60).until(
            expected_conditions.url_contains("login")
        )
        bcitStaySignedInButton     = '//input[contains(@id, "idSIButton9")]'
        findBcitStaySignInButton   = driver.find_element(
            By.XPATH,
            bcitStaySignedInButton
        )

        time.sleep(2)
        findBcitStaySignInButton.click()
    except:
        print("Timed out took too long or couldn't find button")



    try:
        upassRequestButton = '//input[contains(@id, "requestButton")]'
        findUpassRequestButton = driver.find_element(
            By.XPATH,
            upassRequestButton
        )
        findUpassRequestButton.click()

    except:
        monthAlreadyRequested()


finally:
    print("Done the whole thing")
    if driver:
        try:
            driver.quit()
            print("Driver has been quit")
        except Exception as e:
            print("Could not close window properly")

    
