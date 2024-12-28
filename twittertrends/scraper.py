from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.config import Config
from app import collection
import datetime
import uuid

class TwitterScraper:
    def __init__(self):
        self.proxy = f"http://{Config.PROXYMESH_USER}:{Config.PROXYMESH_PASS}@{Config.PROXYMESH_HOST}"
    
    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument(f'--proxy-server={self.proxy}')
        options.add_argument('--headless')  # Run in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        return webdriver.Chrome(options=options)
    
    def login_twitter(self, driver):
        driver.get('https://twitter.com/login')
        
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        email_field.send_keys(Config.TWITTER_EMAIL)
        
        next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
        next_button.click()
        
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(Config.TWITTER_PASSWORD)
        
        login_button = driver.find_element(By.XPATH, "//span[text()='Log in']")
        login_button.click()
    
    def get_trends(self):
        driver = self.setup_driver()
        try:
            self.login_twitter(driver)
            
            trends = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='trend']"))
            )
            
            trend_texts = [trend.text.split('\n')[0] for trend in trends[:5]]
            
            record = {
                "_id": str(uuid.uuid4()),
                "nameoftrend1": trend_texts[0],
                "nameoftrend2": trend_texts[1],
                "nameoftrend3": trend_texts[2],
                "nameoftrend4": trend_texts[3],
                "nameoftrend5": trend_texts[4],
                "timestamp": datetime.datetime.now(),
                "ip_address": self.proxy.split('@')[1]
            }

            collection.insert_one(record)
            return record
            
        finally:
            driver.quit()