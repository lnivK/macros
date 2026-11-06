from pyautogui import *
import pyautogui
import keyboard
import time
import win32api, win32con
import tkinter as tk
from tkinter import messagebox
import subprocess

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def perform_action():
    click(248, 334)  # village
    time.sleep(0.1)
    click(1098, 453)  # grade B
    time.sleep(0.1)
    click(507, 497)  # MISI
    time.sleep(0.1)
    click(1013, 589)
    time.sleep(3)

    if pyautogui.pixel(494, 556)[0] != 98:
        subprocess.run(['python', r'E:\latian\game\botchat\bot.py'])
        return False

    if pyautogui.pixel(494, 556)[0] == 98:
        click(494, 556)
        time.sleep(6)

        if pyautogui.pixel(745, 689)[0] != 0:
            time.sleep(3)
            click(692, 536)
            time.sleep(1)

        if pyautogui.pixel(745, 689)[0] == 0:
            time.sleep(3)
            click(1216, 532)
            time.sleep(1)
            click(692, 536)
            time.sleep(1)

    return True

messagebox.showinfo(title="BOT KVIN", message="Press Q to stop the script")
stop_execution = False

while not stop_execution:
    if keyboard.is_pressed('q'):
        messagebox.showinfo(title="BOT KVIN", message="Script terminated by user")
        break
    
    time.sleep(1)

    if pyautogui.pixel(179, 88)[1] == 72:
        stop_execution = not perform_action()
