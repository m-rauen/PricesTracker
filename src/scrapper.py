from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from main import *
from paths import *

#TODO: add departure and arrival date to Expedia
#TODO: add web scrapper for Decolar

service_object = Service(binary_path)
browser = webdriver.Chrome(service=service_object)

def expedia_scrapper(departure, arrival, going_dt, returning_dt):
    EXPEDIA_URL = 'https://www.expedia.com.br/'
    
    browser.get(EXPEDIA_URL)

    flight_from = browser.find_element_by_xpath(EXPEDIA_DEPARTURE_PATH)
    flight_from.clear()
    flight_from.send_keys(' ' + departure)
    first_item = browser.find_element_by_xpath("//a[@id='aria-option-0']")
    first_item.click()
    
    flight_to = browser.find_element_by_xpath(EXPEDIA_ARRIVAL_PATH)
    flight_to.clear()
    flight_to.send_keys(' ' + arrival)
    first_item = browser.find_element_by_xpath("//a[@id='aria-option-0']")
    first_item.click()
    
    departure_date = browser.find_element_by_xpath()
    
    arrival_date = browser.find_element_by_xpath()
    
    

def decolar_scrapper(origin, departure, going_dt, returning_dt):
    DECOLAR_URL = 'https://www.decolar.com/'
    