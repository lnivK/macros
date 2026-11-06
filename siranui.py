import cv2
import numpy as np
import pygetwindow as gw
import pyautogui
import time
import win32api, win32con
import keyboard
import subprocess
from tkinter import messagebox

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
def detect(window_title, bsc_path, threshold=0.8, delay=3):
    # Load the skill image
    skilimg = cv2.imread(bsc_path, cv2.IMREAD_UNCHANGED)
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
def cek(window_title,nama, threshold=0.9, delay=3):
    # Load the skill image
    mr = cv2.imread(nama, cv2.IMREAD_UNCHANGED)
    gray_skil = cv2.cvtColor(mr, cv2.COLOR_BGR2GRAY)

    # Find the specific window by its title
    target_window = gw.getWindowsWithTitle(window_title)
    if not target_window:
        print(f"Window with title '{window_title}' not found.")
        return False

    target_window = target_window[0]

    # Get the position and size of the target window
    left, top, width, height = target_window.left, target_window.top, target_window.width, target_window.height

    # Capture the screenshot of the specified region using pyautogui
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    mra = mr.shape[1]
    mrt = mr.shape[0]
    tode = cv2.TM_CCOEFF_NORMED
    hsl = cv2.matchTemplate(frame, mr, tode)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(hsl)

    if max_val >= threshold:
        ak = max_loc
        bk = (ak[0] + mra, ak[1] + mrt)
        cv2.rectangle(frame, ak, bk, color=(0, 243, 0), thickness=1, lineType=cv2.LINE_4)
        #cv2.imshow('hasil', frame)
        #cv2.waitKey()
        return True
    else:
        return False

    tw = gw.getWindowsWithTitle(window_title)
    
    if tw:
        tw = tw[0]
        
        w_l,w_t = tw.left,tw.top 
        xpsti, ypsti = w_l + x, w_t + y
        pyautogui.moveTo(xpsti,ypsti)
        pyautogui.mouseDown(button="left")
        pyautogui.mouseUp(button="left")
def ms(window_title, misi, threshold=0.9, delay=3):
    # Load the skill image
    skilimg = cv2.imread(misi, cv2.IMREAD_UNCHANGED)
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
        print('nice')
    # Display the esult
    return    
def kls(window_title, kelas, threshold=0.9, delay=3):
    # Load the skill image
    skilimg = cv2.imread(kelas, cv2.IMREAD_UNCHANGED)
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
def nxt(window_title, next, threshold=0.9, delay=3):
    # Load the skill image
    skilimg = cv2.imread(next, cv2.IMREAD_UNCHANGED)
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
def hntm(window_title, target, threshold=0.9, delay=3):
    # Load the skill image
    skilimg = cv2.imread(target, cv2.IMREAD_UNCHANGED)
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
def nxet(window_title, next1, threshold=0.9, delay=3):
    # Load the skill image
    skilimg = cv2.imread(next1, cv2.IMREAD_UNCHANGED)
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
def check_window(window_title):
    return gw.getWindowsWithTitle(window_title)
def reopen_ninja_legends():
    print("Relaunching Ninja Legends...")
    subprocess.Popen("C:\\Users\\kvin\\Downloads\\Ninja Legends v0.64\\PC\\Ninja Legends.exe")
    time.sleep(10)  # Wait for the application to open
def login(window_title, log, threshold=0.9, delay=3):
    # Load the skill image
    skilimg = cv2.imread(log, cv2.IMREAD_UNCHANGED)
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
    time.sleep(5)
    # Display the esult
    return    
def female(window_title, fem, threshold=0.9, delay=3):
    # Load the skill image
    skilimg = cv2.imread(fem, cv2.IMREAD_UNCHANGED)
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
    time.sleep(5)
    # Display the esult
    return    
def tutup(window_title, ttp, threshold=0.9, delay=3):
    # Load the skill image
    skilimg = cv2.imread(ttp, cv2.IMREAD_UNCHANGED)
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
    time.sleep(5)
    return    
def masuk(window_title, msk, threshold=0.9, delay=3):
    # Load the skill image
    skilimg = cv2.imread(msk, cv2.IMREAD_UNCHANGED)
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
    time.sleep(5)
    return   
# Example usage

window_title = "Ninja Legends"
skilimg_path = "./opencv/asset/skil.JPG"
bsc_path = "./opencv/asset/skil1.JPG"
clm_path = "./opencv/asset/claim.JPG"
nama = "./opencv/asset/nama.JPG"
misi = "./opencv/asset/FR.JPG"
kelas = "./opencv/asset/kelas.JPG"
next = "./opencv/asset/tmbl.JPG"
gelud = "./opencv/asset/gelud.JPG"
target = "./opencv/asset/misi.JPG"
next1 = "./opencv/asset/tmbl1.JPG"
log = "./opencv/asset/log.JPG"
fem = "./opencv/asset/fem.JPG"
ttp = "./opencv/asset/ttp.JPG"
msk = "./opencv/asset/msk.JPG"
messagebox.showinfo(title="BOT KVIN",message="kalau mau stop tahan Q saja ")
while True :
    if keyboard.is_pressed('q'): 
        messagebox.showinfo(title="BOT KVIN",message="BOT BERHENTI")
        break
    else :
        if not check_window(window_title):
            reopen_ninja_legends()
            login(window_title,log)
            female(window_title,fem)
            masuk(window_title,msk)
            tutup(window_title,ttp)
            continue
        
        time.sleep(1)
        # if cek(window_title,nama):
        ms(window_title,misi)  #vilage
        time.sleep(0.1)
        kls(window_title,kelas) #grade a
        time.sleep(0.1)
        nxt(window_title,next) #next
        #time.sleep(0.5)
        nxet(window_title,next1) #next
            #time.sleep(0.5)
        nxet(window_title,next1) #next
            #time.sleep(0.3)
        nxet(window_title,next1) #next
            #time.sleep(0.3)
        hntm(window_title,target) #MISI
        time.sleep(0.1)
        gld(window_title,gelud) #play
        time.sleep(3)
        if detect_and_click(window_title, skilimg_path) :
            time.sleep(1)
                #if pyautogui.pixel(300,491) [2] == 1:
        elif detect(window_title, bsc_path):
            time.sleep(0.1)
        elif claim(window_title, clm_path):
            time.sleep(0.1)
        else:
            pyautogui.moveTo(222,222)  
                #else:
                ##claim(window_title, clm_path)