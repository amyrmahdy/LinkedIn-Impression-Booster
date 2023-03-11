import time
import random
from selenium import webdriver

def playing(url,views,seconds):
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    driver = webdriver.Chrome(options=option, executable_path = "./chromedriver")
    driver.get(url)
    for _ in range(views):
        try:
            #REFRESH
            driver.get(url)
            time.sleep(seconds + random.randint(0,5))
        except:
            print("error")
    driver.quit()

