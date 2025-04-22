from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
import time
from random import randint;

username = "myusername@username.com"
password = "ImaZ567*P67"

url_source = "https://mysourceurl.com"
url_destin = "https://mywebhookreceive.com"

headers_destin = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                  'Content-Type': 'application/json', 
                 }

service = Service()
options = webdriver.ChromeOptions()
driver  = webdriver.Chrome(service=service, options=options)

def getUrl(driver, url_source):
    try:
        driver.get(url_source)
        time.sleep(5)
    except:
        print("URL SOURCE not found!")

    try:
        driver.find_element(By.LINK_TEXT, "Premium")
        btnAccount = driver.find_element(By.ID, "AccountDropdown")
        btnAccount.click()
        btnLogin = driver.find_element(By.LINK_TEXT, "Login")
        btnLogin.click()
        time.sleep(1)

        form = driver.find_element(By.TAG_NAME, "form")
        form.find_element(By.ID, "user_name").send_keys(username)
        form.find_element(By.ID, "user_password").send_keys(password)
        form.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)

    except NoSuchElementException:
        print("Is Logged")
    
    try:
        panels = driver.find_elements(By.CLASS_NAME, 'signal-card')
        payload = []
        for panel in panels:
            try:
                symbol = panel.find_element(By.TAG_NAME, 'a').text
                signalRows = panel.find_elements(By.CLASS_NAME, 'signal-row')
                timeAgo = signalRows[0].find_element(By.CLASS_NAME, 'signal-value').text
                timeFrom = signalRows[1].find_element(By.CLASS_NAME, 'signal-value').text
                timeTill = signalRows[2].find_element(By.CLASS_NAME, 'signal-value').text
                signalStatus = signalRows[3].text
                dealPrice = signalRows[4].find_element(By.CLASS_NAME, 'signal-value').text
                profit = signalRows[5].find_element(By.CLASS_NAME, 'signal-value').text
                loss = signalRows[6].find_element(By.CLASS_NAME, 'signal-value').text

                symbol = symbol.replace("/", "")
                timeFrom = timeFrom.split(" ")[1]
                timeTill = timeTill.split(" ")[1]  

                payload.append({
                    'symbol'      : symbol,
                    'timeAgo'     : timeAgo,
                    'timeFrom'    : timeFrom,
                    'timeTill'    : timeTill,
                    'signalStatus': signalStatus,
                    'dealPrice'   : dealPrice,
                    'profit'      : profit,
                    'loss'        : loss
                })

            except NoSuchElementException:
                print("Currency info not loaded!")

        try:
            requests.post(url_destin, json=payload, headers=headers_destin)     
        except:
            print("Currency data can t sended!")

    except NoSuchElementException:
        print("No find data in source!")

    time.sleep(randint(10, 60))
    getUrl(driver, url_source)

getUrl(driver, url_source)
