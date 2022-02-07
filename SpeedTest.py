from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

DRIVER_PATH = "C:\Program Files\selenium_chromedriver_win32\chromedriver.exe"

class SpeedTest:

    def __init__(self):
        self.down = 0
        self.up = 0
        self.s = Service(DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get("https://www.speedtest.net")
        print("a1")

    def get_speed(self):
        go_speed = self.driver.find_element(By.CSS_SELECTOR, "a.js-start-test")
        go_speed.click()
        time.sleep(3)
        element = WebDriverWait(self.driver, 120).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')))
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        return [self.up, self.down]