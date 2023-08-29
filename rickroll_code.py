import webbrowser
from selenium import webdriver
import keyboard
import time
import Tkinter as tk
driver = webdriver.Chrome()
root = tk.Tk()
def on_closing():#Make program unclosable, except with task manager
    pass
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
def yt_video_is_paused(driver):
    start_current_time = driver.find_element_by_class_name("ytp-time-current").text
    time.sleep(1)
    end_current_time = driver.find_element_by_class_name("ytp-time-current").text
    return start_current_time == end_current_time
while True:
    if driver.current_url != 'https://www.youtube.com/watch?v=a3Z7zEc7AXQ':
        driver.close()
        webbrowser.open('https://www.youtube.com/watch?v=a3Z7zEc7AXQ')
        t = time.time()#Reset timer for rickroll watching
    if yt_video_is_paused(driver):
        keyboard.press('space')#Keep playing rickroll if paused
        t += 1
    if time.time()-t > 210: #End loop once rickroll has been watched
        break
