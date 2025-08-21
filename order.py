#!/usr/bin/python3
"""Author RZFeeser for youtube.com/@CodeWithFeeser
  
   NOTE: This workflow ACTUALLY ORDERS A PIZZA FROM DOMINOS. In no way you should be using this script maliciously, only deliciously. For safety, I have the final order click commented out of `order.py`. Unless you intend or purhcasing a pizza, do not uncomment this last line. Ultimately, I wrote it as a tool for teaching how one could use GitHub Actions to do just about anything (like order a pizza), as well as creating a fun oppertunity to teach about Selenium testing. 

   Objective:
   Place an order for a Domino's Pizza using Selenium & Firefox. I'd like to adapt this into a GitHub workflow, so that anyone can order from Domino's using GitHub.

   Remarks:
   - Domino's seems to be slowly testing the roll out of a new site. The script essentially has two versions of itself, one for the old version of the website, and one for the newer version of the website. There is no need to do anything, the script will auto detect which version of the site is being used.
   - The script will select the top most location for your City and State
   - Camelot, 'tis a silly place.

   Environmental Variables:
   CITY - City to order pizza from
   STATE - Two letter state abbreviation
   LAST_NAME - Last name for your order
   FIRST_NAME - First name for your order
   EMAIL - Email address for your order
   PHONE - Phone number for your order

   At this time I have Hardcoded:
   Carryout & Cheese, but there is not anything that isn't easily converted to ENV inputs.

   GitHub:
   https://github.com/rzfeeser/githubActions-OrderADominosPizza/

   z@iris7.com
   """


# standard library
import os
import time

# 3rd party libraries
# python -m pip install selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# capture environmental vars that control how the script runs
for var in ["CITY", "STATE", "LAST_NAME", "FIRST_NAME", "EMAIL", "PHONE"]:
    if var in os.environ:
        globals()[var] = os.environ[var]

# example...
#if os.environ['CITY']:
#    CITY = os.environ['CITY']


# Domino's seems to be testing a new version of their website
# so we need to determine which version they are using, OLD or NEW
def new_website(driver):
    """returns True if NEW and False if OLD"""
    try:
        # try to find a link on the OLD website
        driver.find_element(By.XPATH, "/html/body/div[1]/main/section/div/div/a[2]")
    except NoSuchElementException:
        return True  # This is NEW website (the OLD link does not exist)
    return False      # This is an OLD website (the OLD link does exist)



def main():
    """interaction with Selenium and Firefox"""

    # we want to 'try' the following and if it works or fails, we 'finally' need a screenshot
    try:
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
        # Open Firefox to Dominos.com
        #driver = webdriver.Firefox()
        driver.get("https://www.dominos.com/en/")
        time.sleep(5)

        # if the OLD website loads
        if not new_website(driver):
            ## Begin Carryout
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/main/section/div/div/a[2]")
            elem.click()
            time.sleep(5)
            ## Enter Data for Find Store
            elem = driver.find_element(By.XPATH, "//*[@id='City']")
            elem.send_keys(CITY)     # The CITY is updated with an ENV
            time.sleep(2)
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/main/section/article/div/div[2]/div[2]/form/fieldset/div[2]/div[2]/select")
            elem.send_keys(STATE)  # The STATE is updated with an ENV
            time.sleep(2)
            ## Click Find a Store
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/main/section/article/div/div[2]/div[2]/form/div/button")
            elem.click()
            time.sleep(5)

            ## Click on Pizza builder
            elem = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div[6]/a")
            elem.click()
            time.sleep(5)

            ## Add to order
            elem = driver.find_element(By.XPATH,
                                       "/html/body/div[5]/div/section/div/div/ol/li[8]/aside/section/div/div[3]/button")
            elem.click()
            time.sleep(5)

            ## Extra Cheese Popup (NO)
            elem = driver.find_element(By.XPATH, "/html/body/div[5]/div/section/div/div/div/div/button[1]")
            elem.click()
            time.sleep(5)

            driver.get('https://www.dominos.com/en/pages/order/payment')
            time.sleep(6)

            # Choose first name
            elem = driver.find_element(By.XPATH, "//*[@id='First_Name']")
            elem.send_keys(FIRST_NAME)
            time.sleep(1)

            # Choose last name
            elem = driver.find_element(By.XPATH, "//*[@id='Last_Name']")
            elem.send_keys(LAST_NAME)
            time.sleep(1)

            # Choose email address
            elem = driver.find_element(By.XPATH, "//*[@id='Email']")
            elem.send_keys(EMAIL)
            time.sleep(1)

            # Set callback phone
            elem = driver.find_element(By.XPATH, "//*[@id='Callback_Phone']")
            for number in PHONE:  # for some reason numbers don't always copy and paste correctly
                elem.send_keys(number)  # this seems to be a decent fix
                time.sleep(1)

            # opt out of offers
            elem = driver.find_element(By.XPATH, "//*[@id='EmailOptIn']")
            elem.click()

            # Opt out of Pizza Rewards
            elem = driver.find_element(By.XPATH, "//*[@id='Loyalty_Enrollment_No']")
            elem.click()

            # pay cash at the store
            elem = driver.find_element(By.XPATH, "//*[@id='Cash']")
            elem.click()

            # Click the button "PLACE YOUR ORDER"
            # You must uncomment this line for the order to be placed on the OLD website
            # Be delcious, not malicious!
            elem = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/form/div[9]/div/div/div[5]/button")
            elem.click()
        else:
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/section/header/div/div[1]/div/p/a[2]")
            elem.click()
            time.sleep(5)
          
            #elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div/form/fieldset/div[1]/div[3]/div[1]/div/input")
            #elem.send_keys(CITY)     # The CITY is updated with an ENV
            #elem = driver.find_element(By.XPATH, "//*[@id='headlessui-combobox-input-:r9:']")
            ## Send the STATE to the input box
            #elem.send_keys(STATE)   # The STATE is updated with an ENV
            
            elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div/form/fieldset/div[1]/div[1]/div/div/input")
            ## Send the STATE to the input box
            elem.send_keys('17003')   # The STATE is updated with an ENV          
            elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div/form/fieldset/div[2]/button")
            ## Click the button
            elem.click()
            time.sleep(5)
            elem = driver.find_element(By.XPATH,
                                       "/html/body/div[6]/div/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div/div/section/ul/li[1]/div")
            elem.click()
            elem.click()
            time.sleep(5)
            elem = driver.find_element(By.XPATH,
                                       "/html/body/div[6]/div/div/div/div[2]/div/div[1]/div[2]/div/div[1]/article/form/div[2]/button")
            ## Click the button to confirm carry-out
            elem.click()
            time.sleep(5)

            elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/section/div[2]/div/div[2]/article/ul/li[1]")

            ## Click on Pizza Builder
            elem.click()
            elem.click()
            time.sleep(5)

            ## Add to Order
            elem = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/section/main/section/div[1]/header[1]/div/section/div[1]/div[2]/button/span[2]")
            ## Add to Order / Cart
            elem.click()
            time.sleep(3)

            ## PopUp - Cheese it up... Neeeewp
            elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/button[1]")

            elem.click()
            time.sleep(5)

            driver.get('https://www.dominos.com/checkout')
            time.sleep(6)

            # Choose first name
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/section/div[1]/div/form/section/section[1]/fieldset[1]/div[1]/div[1]/div/input")
            elem.send_keys(FIRST_NAME)
            time.sleep(1)

            # Choose last name
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/section/div[1]/div/form/section/section[1]/fieldset[1]/div[2]/div[1]/div/input")
            elem.send_keys(LAST_NAME)
            time.sleep(1)

            # Choose email address
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/section/div[1]/div/form/section/section[1]/fieldset[1]/div[3]/div[1]/div/input")
            elem.send_keys(EMAIL)
            time.sleep(1)

            # Set callback phone
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/section/div[1]/div/form/section/section[1]/fieldset[1]/div[4]/div[1]/div/input")
            for number in PHONE: # for some reason numbers don't always copy and paste correctly
                elem.send_keys(number) # this seems to be a decent fix
                time.sleep(1)

            # opt out of offers - finding it difficult to find this click...
            #elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/section/div[1]/div/form/section/section[1]/fieldset[1]/button/div/span")
            #elem.click()

            # Opt out of Pizza Rewards
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/section/div[1]/div/form/section/section[1]/fieldset[2]/div[2]/label")
            driver.execute_script("arguments[0].scrollIntoView(true);", elem)
            elem.click()

            # pay cash at the store
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/section/div[1]/div/form/section/section[1]/fieldset[3]/fieldset/div[3]/label")
            driver.execute_script("arguments[0].scrollIntoView(true);", elem)
            elem.click()

            # Click the button "PLACE YOUR ORDER"
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/section/div[1]/div/form/section/section[2]/div/section/div/button")
            elem.click()
            time.sleep(10)


    # regardless if things worked or failed, grab a screenshot
    finally:
        driver.save_screenshot("screenshot.png")

# call main
if __name__ == "__main__":
    main()
