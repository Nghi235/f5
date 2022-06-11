import keyboard
import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://thagavpn.site/api/v1/client/subscribe?token=f2f9d18a394dd64bbdf2174b22708494')


while True:
  keyboard.press_and_release("f5")
  time.sleep(0.05)