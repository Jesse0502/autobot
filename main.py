import pyautogui as pa
import time

print("Activating autobot...")
time.sleep(5)
while True:
  pa.moveTo(239, 139, 0.7, pa.easeInOutQuad)
  pa.scroll(-100)
  time.sleep(0.5)
  pa.click()

  pa.moveTo(1012, 175, 1, pa.easeInOutQuad)

  pa.click()

  for i in range(50):
    if not (1012, 175) == pa.position():
      quit()
    pa.scroll(-80)
    time.sleep(0.2)
    
