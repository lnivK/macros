from pyautogui import *
import pyautogui
import keyboard
import time
import win32api, win32con
import tkinter as tk
from tkinter import messagebox
import subprocess

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
messagebox.showinfo(title="BOT KVIN",message="kalau mau stop tahan Q saja ")
while True :
    if keyboard.is_pressed('q'): 
        messagebox.showinfo(title="BOT KVIN",message="BOT BERHENTI")
        break
    else :
        time.sleep(1)
    if pyautogui.pixel(179,88) [1] != 72:
        subprocess.run(['python',r'E:\latian\game\botchat\bot.py'])
        break
    if pyautogui.pixel(179,88) [1] == 72:
        click(248,334)  #vilage
        time.sleep(0.1)
        click(898,356) #grade a
        time.sleep(0.1)
        click(631,288) #MISI
        time.sleep(0.1)
        click(1013,589)
        time.sleep(3)
        if pyautogui.pixel(822,299) [0] != 112:
            subprocess.run(['python',r'E:\latian\game\botchat\bot.py'])
            break
        if pyautogui.pixel(822,299) [0] == 112:
            click(625,301)    #talentvampir
            time.sleep(13)
            click(671,472)    #basicattack1
            time.sleep(8)
            click(671,472)    #basicattack2
            time.sleep(8)
            click(671,472)    #basicattack3
            time.sleep(6)
            if pyautogui.pixel(745,689) [0] != 0:
                time.sleep(3)
                click(692,536)
                time.sleep(1)
            if pyautogui.pixel(745,689) [0] == 0:
                time.sleep(3)
                click(1216,532)
                time.sleep(1)
                click(692,536)
                time.sleep(1)
                
    
        
    