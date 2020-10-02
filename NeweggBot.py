from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import keys
import time


def xPathConfig(xpath):
    time.sleep(.5)
    return driver.find_element_by_xpath(xpath).click()

def TypeConfig(xpath,msg):
    return driver.find_element_by_xpath(xpath).send_keys(msg)

def preOrderScript():
    time.sleep(1)
    addToCart           = xPathConfig('//*[@id="landingpage-cart"]/div/div[2]/button')
    removeProtection    = xPathConfig('//*[@id="custom"]/div/div[3]/div/div/div/button[1]')
    time.sleep(.5)
    viewCart            = xPathConfig('//*[@id="bodyArea"]/section/div/div/div[1]/div/div[3]/div[3]/div/button[2]')
    try:
        print("Looking")
        waiter              =WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,'centerPopup-body'))
        )
        print("Found")
        time.sleep(5)
        # highlightPopup      = xPathConfig('//*[@id="centerPopup632800"]/div')
        removePopup         = xPathConfig('//*[@id="centerPopup582275"]/div/div[2]/div/div/div[3]/button')
    except:
        print("Was not found")
        

if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')

    driver.get(keys['product_url'])
    preOrderScript()
    