import webbrowser
import time
import pyautogui

for i in range(50):
    webbrowser.open('https://poll.fm/10666451')
    time.sleep(0.05)
    pyautogui.moveTo(426,550)
    time.sleep(0.05)
    pyautogui.click()
    time.sleep(0.05)
    pyautogui.moveTo(971,600)
    pyautogui.click()