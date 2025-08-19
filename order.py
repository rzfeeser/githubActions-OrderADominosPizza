#!/usr/bin/python3
"""Author RZFeeser for youtube.com/@CodeWithFeeser
  
   NOTE: This workflow ACTUALLY ORDERS A PIZZA FROM DOMINOS. In no way you should be using this script maliciously, only deliciously. For safety, I have the final order click commented out of `order.py`. Unless you intend or purhcasing a pizza, do not uncomment this last line. Ultimately, I wrote it as a tool for teaching how one could use GitHub Actions to do just about anything (like order a pizza), as well as creating a fun oppertunity to teach about Selenium testing. 

   Objective:
   Place an order for a Domino's Pizza using Selenium & Firefox. I'd like to adapt this into a GitHub workflow, so that anyone can order from Domino's using GitHub.

   Remarks:
   - I've been running this exercise for a few years. The Domino's Web API has been surprisingly stable (i.e. I have
   not needed to update any x-paths).
   - Camelot, 'tis a silly place.

   Environmental Variables
   CITY - City to order pizza from
   STATE - Two letter state abbreviation
   LAST_NAME - 
   FIRST_NAME -
   EMAIL -
   PHONE -

   At this time I have Hardcoded:
   Carryout & Cheese, but there is not anything that isn't easily converted to ENV inputs.

   GitHub:

   z@iris7.com
   """


# standard library
import os
import time

# 3rd party libraries
# python -m pip install selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# capture environmental vars that control how the script runs
for var in ["CITY", "STATE", "LAST_NAME", "FIRST_NAME", "EMAIL", "PHONE"]:
    if var in os.environ:
        globals()[var] = os.environ[var]

# example...
#if os.environ['CITY']:
#    CITY = os.environ['CITY']

def main():
    """interaction with Selenium and Firefox"""

    try:
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
        # Open Firefox to Dominos.com
        #driver = webdriver.Firefox()
        driver.get("https://www.dominos.com/en/")
        time.sleep(5)

        elem = driver.find_element(By.XPATH, "/html/body/div[1]/main/section/div/div/a[2]")
        elem.click()
        time.sleep(5)

        # Select Find Store
        elem = driver.find_element(By.XPATH, "//*[@id='City']")
        #elem = driver.find_element(By.XPATH, "//*[contains(text(), 'City')]")

        # The city and state should be updated with envs
        elem.send_keys(CITY)
        elem = driver.find_element(By.XPATH, "//*[@id='Region']")
        elem.send_keys(STATE)
        elem = driver.find_element(By.XPATH, "/html/body/div[1]/main/section/article/div/div[2]/div[2]/form/div/button")
        elem.click()
        time.sleep(5)

        #click on CarryOut - //*[@id="Service_Method_Carryout"]
        elem = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/a")
        elem.click()
        time.sleep(5)

        #click on Curbside Delivery <- if you choose pay by cash this is not an option
        #    elem = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div/div[2]/div[27]/div[3]/div/div[2]/div[1]/a/span[1]")
        #    elem.click()
        #    time.sleep(5)

        #click on Pizza Builder
        elem = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div[2]/div[6]/a")
        elem.click()
        time.sleep(5)

        #Add to Order
        elem = driver.find_element(By.XPATH,"/html/body/div[5]/div/section/div/div/ol/li[8]/aside/section/div/div[3]/button")
        elem.click()
        time.sleep(3)

        #Cheese it up... no
        elem = driver.find_element(By.XPATH,"/html/body/div[5]/div/section/div/div/div/div/button[1]")
        elem.click()
        time.sleep(5)

        #Checkout
        driver.get('https://www.dominos.com/en/pages/order/payment')
        time.sleep(5)

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
        for number in PHONE: # for some reason numbers don't always copy and paste correctly
            elem.send_keys(number) # this seems to be a decent fix
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

    # regardless if things worked or failed, grab a screenshot
    finally:
        time.sleep(5)
        driver.save_screenshot("screenshot.png")

# call main
if __name__ == "__main__":
    main()
