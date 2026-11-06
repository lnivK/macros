from pyautogui import *
import pyautogui
import keyboard
import time
import win32api, win32con
import tkinter as tk
from tkinter import messagebox

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
messagebox.showinfo(title="BOT KVIN1",message="kalau mau stop tahan Z saja ")
while True :
    if keyboard.is_pressed('z'): 
        messagebox.showinfo(title="BOT KVIN1", message="BOT SELESAI BOSS")
        break
    else :
        time.sleep(1)
    if pyautogui.pixel(1401,620) [1] != 72:
        messagebox.showinfo(title="BOT KVIN1", message="YANG BENER BOSS")
        break
    if pyautogui.pixel(1401,620) [1] == 72:
        click(1471,779)  #vilage
        time.sleep(0.1)
        click(1869,904) #grade B
        time.sleep(0.1)
        click(1541,813) #misike
        time.sleep(0.1)
        click(1995,921) #PLAY
        time.sleep(3)
        if pyautogui.pixel(1624,885) [0] != 98:
            messagebox.showinfo(title="BOT KVIN1",message="LOADING ERROR BOSS")
            break
        if pyautogui.pixel(1624,885) [0] == 98:
            click(1624,885) #skilbox2
            time.sleep(4)
            click(1581,888)  #skilbox3
            time.sleep(6)
            if pyautogui.pixel(1436,799) [2] != 1:
                time.sleep(3)
                click(1723,900)  #claim
                time.sleep(1)
            if pyautogui.pixel(1436,799) [2] == 1:
                time.sleep(3)
                click(2105,885)  #centang
                time.sleep(1)
                click(1723,900)
                time.sleep(1)
                
    