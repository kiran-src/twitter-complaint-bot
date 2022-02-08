from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

DRIVER_PATH = "C:\Program Files\selenium_chromedriver_win32\chromedriver.exe"
pause = 3

class Tweet:

    def __init__(self):
        self.down = 0
        self.up = 0
        self.s = Service(DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get("https://www.twitter.com")
        print("a1")

    def login(self, passw, email, user):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(pause)

        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.TAG_NAME, 'input')))
        print('u1')
        time.sleep(pause)
        user_i = self.driver.find_element(By.TAG_NAME, 'input')
        user_i.send_keys(user)
        print('u2')
        time.sleep(pause)
        user_i.send_keys(Keys.ENTER)
        print('u3')
        time.sleep(pause)
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.TAG_NAME, 'input')))
        print('e1')
        time.sleep(pause)
        user_i = self.driver.find_element(By.TAG_NAME, 'input')
        user_i.send_keys(email)
        print('e2')
        time.sleep(pause)
        user_i.send_keys(Keys.ENTER)
        print('e3')
        time.sleep(pause)
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.TAG_NAME, 'input')))
        print('p1')
        time.sleep(pause)
        pass_i = self.driver.find_element(By.TAG_NAME, 'input')
        pass_i.send_keys(passw)
        print('p2')
        time.sleep(pause)
        pass_i.send_keys(Keys.ENTER)
        print('p3')
        time.sleep(pause)
        # self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(email)

    def speed_tweet(self):
        pass