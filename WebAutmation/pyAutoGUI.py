import pyautogui
width, height = pyautogui.size()
for i in range(2):
      pyautogui.moveTo(100, 100, duration=0.25)
      pyautogui.click(100, 100)
      print(pyautogui.position())
      pyautogui.moveTo(200, 100, duration=0.25)
      pyautogui.click(200, 100, button="right")
      print(pyautogui.position())
      pyautogui.moveTo(200, 200, duration=0.25)
      pyautogui.doubleClick(200, 200)
      print(pyautogui.position())
      pyautogui.moveTo(100, 200, duration=0.25)
      print(pyautogui.position())
