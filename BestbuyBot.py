from selenium import webdriver
from config import bbKey
import time


def xPathConfig(xpath):
    time.sleep(5)
    return driver.find_element_by_xpath(xpath).click()

def TypeConfig(xpath,msg):
    return driver.find_element_by_xpath(xpath).send_keys(msg)

def preOrderScript():
    selectCountry   = xPathConfig('/html/body/div[2]/div/div/div/div[1]/div[2]/a[2]')
    addtoCart       = xPathConfig('//*[@id="fulfillment-add-to-cart-button-bc7ac10d-6086-426f-bc62-0043f5594258"]/div/div/button')
    time.sleep(2)
    gotoCart        = xPathConfig('//*[@id="shop-attach-modal-106f459b-5105-4f27-9859-9e8a4886d498-modal"]/div/div[2]/div/div/div/div/div[1]/button[2]')
    checkout        = xPathConfig('//*[@id="cartApp"]/div[2]/div[1]/div/div/span/div/div[1]/section[2]/div/div/div[3]/div[1]/div[1]/button')
    guestCheckout   = xPathConfig('/html/body/div[1]/div/section/main/div[4]/div/div[2]/button')

    firstName       = TypeConfig('//*[@id="consolidatedAddresses.ui_address_2.firstName"]',bbKey['FN'])
    lastName        = TypeConfig('//*[@id="consolidatedAddresses.ui_address_2.lastName"]',bbKey['LN'])
    strAddress      = TypeConfig('//*[@id="consolidatedAddresses.ui_address_2.street"]',bbKey['STRADD'])
    city            = TypeConfig('//*[@id="consolidatedAddresses.ui_address_2.city"]',bbKey['CT'])
    selectState     = TypeConfig('//*[@id="consolidatedAddresses.ui_address_2.street"]',bbKey['ST'])
    zipCode         = TypeConfig('//*[@id="consolidatedAddresses.ui_address_2.zipcode"]',bbKey['ZC'])
    emailAdd        = TypeConfig('//*[@id="user.emailAddress"]',bbKey['EMAIL'])
    phoneNum        = TypeConfig('//*[@id="user.phone"]',bbKey['PN'])

    continuePayment = xPathConfig('//*[@id="checkoutApp"]/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button')



if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')

    driver.get(bbKey['product_url'])
    preOrderScript()