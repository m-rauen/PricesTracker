import time as t
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chromedriver_py import binary_path
from main import *
from src.paths import *

service_object = Service(binary_path)
browser = webdriver.Chrome(service=service_object)
wait = WebDriverWait(browser, 10)

def expedia_scrapper(departure, arrival, going_dt, returning_dt):
    #TODO: wait till search page load, then, scrape it 
        
    EXPEDIA_URL = 'https://www.expedia.com.br/passagens-aereas'
    
    browser.get(EXPEDIA_URL)

    departure_button = wait.until(EC.element_to_be_clickable((By.XPATH, EXPEDIA_DEPARTURE_BUTTON)))
    departure_button.click()
    flight_from = wait.until(EC.presence_of_element_located((By.XPATH, EXPEDIA_DEPARTURE_PATH)))
    flight_from.clear()
    flight_from.send_keys(departure)
    browser.implicitly_wait(20)
    flight_from.send_keys(Keys.ENTER)
    t.sleep(3)
    
    arrival_button = wait.until(EC.element_to_be_clickable((By.XPATH, EXPEDIA_ARRIVAL_BUTTON)))
    arrival_button.click()
    flight_to = wait.until(EC.presence_of_element_located((By.XPATH, EXPEDIA_ARRIVAL_PATH)))
    flight_to.clear()
    flight_to.send_keys(arrival)
    browser.implicitly_wait(20)
    flight_to.send_keys(Keys.ENTER)
    t.sleep(3)
    
    departure_date_button = wait.until(EC.presence_of_element_located((By.XPATH,EXPEDIA_DEPARTURE_DATE_BUTTON)))
    departure_date_button.click()
    departure_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='{}']".format(going_dt))))
    browser.execute_script("arguments[0].scrollIntoView()", departure_date)
    departure_date.click()
    t.sleep(3)
    
    arrival_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='{}']".format(returning_dt))))
    browser.execute_script("arguments[0].scrollIntoView()", arrival_date)
    arrival_date.click()
    t.sleep(3)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, EXPEDIA_CONFIRM_DATE_BUTTON))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, EXPEDIA_SEARCH_BUTTON))).click()
    
    
    
    
def decolar_scrapper(departure, arrival, going_dt, returning_dt):
    #TODO: 
    #TODO: 
    
    DECOLAR_URL = 'https://www.decolar.com/'
    
    departure_button = wait.until(EC.element_to_be_clickable((By.XPATH, DECOLAR_DEPARTURE_BUTTON)))
    departure_button.click()
    flight_to = wait.until(EC.presence_of_element_located((By.XPATH, DECOLAR_DEPARTURE_PATH)))
    flight_to.clear()
    flight_to.send_keys(departure)
    browser.implicitly_wait(20)
    flight_to.send_keys(Keys.ENTER)
    t.sleep(3)
    
    
    