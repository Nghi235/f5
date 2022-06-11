import keyboard
import time
print('5 Giây Đếm Ngược')
time.sleep(1)
print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('Bắt Đầu')
time.sleep(1)
a=0
while True:
  keyboard.press_and_release("f5")
  a=a+1
  print(f"Số Lần F5 - {a}")
  time.sleep(0.05)


