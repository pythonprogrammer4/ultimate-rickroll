from selenium import webdriver
import keyboard
import time
import Tkinter as tk
from youtube_video_play_pause_bot import *
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
    if driver.current_url != 'https://www.youtube.com/watch?v=a3Z7zEc7AXQ':#If the rickroll was closed or the victim went to another tab
        driver.close()
        youtube.open('https://www.youtube.com/watch?v=a3Z7zEc7AXQ')
    if yt_video_is_paused(driver):
        youtube.play_pause_video()
