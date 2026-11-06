from pyautogui import *
import pyautogui
import numpy as np 
import time
import random
import win32api, win32con
import tkinter as tk
from tkinter import messagebox
import subprocess
import cv2
import pygetwindow as gw

def claim(window_title, clm_path, threshold=0.8, delay=3):
    # Load the skill image
    skilimg = cv2.imread(clm_path, cv2.IMREAD_UNCHANGED)
    gray_skil = cv2.cvtColor(skilimg, cv2.COLOR_BGR2GRAY)

    # Find the specific window by its title
    target_window = gw.getWindowsWithTitle(window_title)
    if not target_window:
        print(f"Window with title '{window_title}' not found.")
        return

    target_window = target_window[0]

    # Get the position and size of the target window
    left, top, width, height = target_window.left, target_window.top, target_window.width, target_window.height

    # Capture the screenshot of the specified region using pyautogui
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(gray_frame, gray_skil, cv2.TM_CCOEFF_NORMED)

    # Set a threshold to determine matches
    loc = np.where(result >= threshold)

    # Draw rectangles around the detected matches
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + skilimg.shape[1], pt[1] + skilimg.shape[0]), (0, 255, 0), 2)

        # Introduce a delay before clicking
        #time.sleep()

        # Click at the center of the detected object
        object_center = ((pt[0] + pt[0] + skilimg.shape[1]) // 2, (pt[1] + pt[1] + skilimg.shape[0]) // 2)
        pyautogui.click(left + object_center[0], top + object_center[1])

    # Display the esult
    return    
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def gld(window_title, gelud, threshold=0.8, delay=3):
    # Load the skill image
    skilimg = cv2.imread(gelud, cv2.IMREAD_UNCHANGED)
    gray_skil = cv2.cvtColor(skilimg, cv2.COLOR_BGR2GRAY)

    # Find the specific window by its title
    target_window = gw.getWindowsWithTitle(window_title)
    if not target_window:
        print(f"Window with title '{window_title}' not found.")
        return

    target_window = target_window[0]

    # Get the position and size of the target window
    left, top, width, height = target_window.left, target_window.top, target_window.width, target_window.height

    # Capture the screenshot of the specified region using pyautogui
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(gray_frame, gray_skil, cv2.TM_CCOEFF_NORMED)

    # Set a threshold to determine matches
    loc = np.where(result >= threshold)

    # Draw rectangles around the detected matches
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + skilimg.shape[1], pt[1] + skilimg.shape[0]), (0, 255, 0), 2)

        # Introduce a delay before clicking
        #time.sleep()

        # Click at the center of the detected object
        object_center = ((pt[0] + pt[0] + skilimg.shape[1]) // 2, (pt[1] + pt[1] + skilimg.shape[0]) // 2)
        pyautogui.click(left + object_center[0], top + object_center[1])

    # Display the esult
    return    
def detect_and_click(window_title, skilimg_path, threshold=0.8, delay=3):
    # Load the skill image
    skilimg = cv2.imread(skilimg_path, cv2.IMREAD_UNCHANGED)
    gray_skil = cv2.cvtColor(skilimg, cv2.COLOR_BGR2GRAY)

    # Find the specific window by its title
    target_window = gw.getWindowsWithTitle(window_title)
    if not target_window:
        print(f"Window with title '{window_title}' not found.")
        return

    target_window = target_window[0]

    # Get the position and size of the target window
    left, top, width, height = target_window.left, target_window.top, target_window.width, target_window.height

    # Capture the screenshot of the specified region using pyautogui
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(gray_frame, gray_skil, cv2.TM_CCOEFF_NORMED)

    # Set a threshold to determine matches
    loc = np.where(result >= threshold)

    # Draw rectangles around the detected matches
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + skilimg.shape[1], pt[1] + skilimg.shape[0]), (0, 255, 0), 2)

        # Introduce a delay before clicking
        #time.sleep(delay)

        # Click at the center of the detected object
        object_center = ((pt[0] + pt[0] + skilimg.shape[1]) // 2, (pt[1] + pt[1] + skilimg.shape[0]) // 2)
        pyautogui.click(left + object_center[0], top + object_center[1])

    # Display the esult
    return


window_title='Ninja Legends'
clm_path = r'E:\latian\game\opencv\asset\x.JPG'
gelud = r'E:\latian\game\opencv\asset\daily\f.JPG'
skilimg_path = r'E:\latian\game\opencv\asset\skil.JPG'

messagebox.showinfo(title="BOT KVIN",message="PASTIKAN DI DESA DAN TUNGGU HINGGA KELAR")
time.sleep(1)
click(288,345)    #vilage
time.sleep(0.1)
click(879,193) #dailly
time.sleep(0.1)
click(546,175) #MISI1
time.sleep(3)
gld(window_title,gelud) #play
time.sleep(3)
#if all(value == 0 for value in pyautogui.pixel(518, 361)):
    #subprocess.run(['python',r'E:\latian\game\botchat\bot1.py'])
if all(value != 0 for value in pyautogui.pixel(518, 361)):   
    detect_and_click(window_title, skilimg_path)   #skill
    time.sleep(5)
    click(692,536)  #done
    time.sleep(1)
    click(288,345)    #vilage
    time.sleep(0.1)
    click(879,193) #dailly
    time.sleep(0.1)
    click(472,279) #MISI2
    time.sleep(3)
    gld(window_title,gelud)
    time.sleep(3)
    detect_and_click(window_title, skilimg_path)
    time.sleep(5)
    click(692,536)
    time.sleep(1)
    click(288,345)    #vilage
    time.sleep(0.1)
    click(879,193) #dailly
    time.sleep(0.1)
    click(534,384) #MISI3
    time.sleep(3)
    gld(window_title,gelud)
    time.sleep(3)
    detect_and_click(window_title, skilimg_path)
    time.sleep(5)
    click(692,536)
    time.sleep(1)
    click(288,345)    #vilage
    time.sleep(0.1)
    click(879,193) #dailly
    time.sleep(0.1)
    click(507,497) #MISI4
    time.sleep(3)
    gld(window_title,gelud)
    time.sleep(3)
    detect_and_click(window_title, skilimg_path)
    time.sleep(5)
    click(692,536)
    time.sleep(1)
    #page 2
    click(288,345)    #vilage
    time.sleep(0.1)
    click(879,193) #dailly
    time.sleep(0.1)
    click(621,588) #next
    click(546,175) #MISI1
    time.sleep(3)
    gld(window_title,gelud)
    time.sleep(3)
    detect_and_click(window_title, skilimg_path)
    time.sleep(5)
    click(692,536)
    time.sleep(1)
    click(288,345)    #vilage
    time.sleep(0.1)
    click(879,193) #dailly
    time.sleep(0.1)
    click(621,588) #next
    click(507,497) #MISI4
    time.sleep(3)
    gld(window_title,gelud)
    time.sleep(3)
    detect_and_click(window_title, skilimg_path)
    time.sleep(5)
    click(692,536)
    time.sleep(1)
    click(288,345)    #vilage
    time.sleep(0.1)
    click(879,193) #dailly
    time.sleep(0.1)
    click(621,588) #next
    click(472,279) #MISI2
    time.sleep(3)
    gld(window_title,gelud)
    time.sleep(3)
    detect_and_click(window_title, skilimg_path)
    time.sleep(5)
    click(692,536)
    time.sleep(1)
    click(288,345)    #vilage
    time.sleep(0.1)
    click(879,193) #dailly
    time.sleep(0.1)
    click(621,588) #next
    click(534,384) #MISI3
    time.sleep(3)
    gld(window_title,gelud)
    time.sleep(3)
    detect_and_click(window_title, skilimg_path)
    time.sleep(5)
    click(692,536)
    time.sleep(1)
