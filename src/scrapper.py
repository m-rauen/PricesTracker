import time as t
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select 
from chromedriver_py import binary_path
from main import *
from src.paths import *

service_object = Service(binary_path)
browser = webdriver.Chrome(service=service_object)
wait = WebDriverWait(browser, 10)

def expedia_scrapper(departure, arrival, going_dt, returning_dt):
    #TODO: select specific date from calendar input
    
    EXPEDIA_URL = 'https://www.expedia.com.br/passagens-aereas'
    
    browser.get(EXPEDIA_URL)

    departure_button = wait.until(EC.presence_of_element_located((By.XPATH, EXPEDIA_DEPARTURE_BUTTON)))
    departure_button.click()
    flight_from = wait.until(EC.presence_of_element_located((By.XPATH, EXPEDIA_DEPARTURE_PATH)))
    flight_from.clear()
    flight_from.send_keys(departure)
    browser.implicitly_wait(20)
    flight_from.send_keys(Keys.ENTER)
    
    arrival_button = wait.until(EC.presence_of_element_located((By.XPATH,    EXPEDIA_ARRIVAL_BUTTON)))
    arrival_button.click()
    flight_to = wait.until(EC.presence_of_element_located((By.XPATH, EXPEDIA_ARRIVAL_PATH)))
    flight_to.clear()
    flight_to.send_keys(arrival)
    browser.implicitly_wait(20)
    flight_to.send_keys(Keys.ENTER)
    
    departure_date_button = browser.find_element(by=By.XPATH, value=EXPEDIA_DEPARTURE_DATE_BUTTON)
    departure_date_button.click()
    departure_date = browser.find_element(by=By.XPATH, value=EXPEDIA_ARRIVAL_DATE_PATH)
    departure_date.click()
    departure_month = browser.find_element(by=By.CSS_SELECTOR, value="#wizard-flight-tab-roundtrip .datepicker-cal-month:nth-child(1) > select")
    departure_year = browser.find_element(by=By.CSS_SELECTOR, value="#wizard-flight-tab-roundtrip .datepicker-cal-year:nth-child(1) > select")
    departure_month.send_keys(going_dt.month)
    departure_year.send_keys(going_dt.year)
    
    
def decolar_scrapper(origin, departure, going_dt, returning_dt):
    #TODO: add web scrapper for Decolar
    DECOLAR_URL = 'https://www.decolar.com/'
    