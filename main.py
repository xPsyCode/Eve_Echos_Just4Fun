import win32gui
from capture import WindowCapture
import cv2
import pyautogui
import time

win = WindowCapture("BlueStacks")

def template_matching(image:str):
    img = win.get_screenshot()
    temp = cv2.imread(image)
    res =cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_val, max_loc

# pyautogui.click(win.get_screen_position(template_matching("temp/nav.png")[1]))
# time.sleep(1)
# loc = template_matching("temp/mining1.png")[1]
# pyautogui.click(win.get_screen_position((loc[0]+300, loc[1]+ 10)))
# time.sleep(1)
# loc = template_matching("temp/submit_Btn.png")[1]
# pyautogui.click(win.get_screen_position((loc[0]+50,loc[1]+20)))
# time.sleep(15)
# while True:
#     val = template_matching("temp/endpoint_mining.png")[0]
#     if(val >= 0.9):
#             break
#     time.sleep(1)
# time.sleep(3)
# pyautogui.click(win.get_screen_position(template_matching("temp/menu_btn.png")[1]))
# time.sleep(1)
# pyautogui.click(win.get_screen_position((1600,50)))
# time.sleep(1)
# pyautogui.click(win.get_screen_position(template_matching("temp/belt.png")[1]))
# time.sleep(1)
# pyautogui.click(win.get_screen_position((1600,100)))
# time.sleep(1)
# pyautogui.click(win.get_screen_position(template_matching("temp/warpen.png")[1]))
# time.sleep(5)
# pyautogui.click(win.get_screen_position((1600,50)))
# time.sleep(1)
# pyautogui.click(win.get_screen_position(template_matching("temp/asta.png")[1]))
# time.sleep(3)
# while True:
#     val = template_matching("temp/waiting.png")[0]
#     if(val < 0.9):
#             break
#     time.sleep(1)
# time.sleep(8)
# loc = template_matching("temp/plag.png")[1]
# pyautogui.click(win.get_screen_position((loc[0]+20,loc[1]+10)))
# pyautogui.click(win.get_screen_position((loc[0]+20,loc[1]+10)))
# time.sleep(1)
# pyautogui.click(win.get_screen_position((loc[0]+20,loc[1]+100)))
# pyautogui.click(win.get_screen_position((loc[0]+20,loc[1]+100)))
# time.sleep(1)
# pyautogui.click(win.get_screen_position((loc[0]+20,loc[1]+250)))
# pyautogui.click(win.get_screen_position((loc[0]+20,loc[1]+250)))
# time.sleep(1)
# pyautogui.click(win.get_screen_position((loc[0]+20,loc[1]+10)))
# time.sleep(1)
# pyautogui.click(win.get_screen_position(template_matching("temp/getclose.png")[1]))

# while True:
#     val = template_matching("temp/15km.png")[0]
#     if(val >= 0.9):
#         break
#     time.sleep(1)
# pyautogui.click(win.get_screen_position(template_matching("temp/15km.png")[1]))
# time.sleep(1)
# pyautogui.press('q')
# time.sleep(1)
# pyautogui.press('space')
# time.sleep(1)
# pyautogui.click(win.get_screen_position((800,300)))

# while True:
#     val = template_matching("temp/finish.png")[0]
#     if(val >= 0.9):
#         break
#     time.sleep(1)

# pyautogui.click(win.get_screen_position(template_matching("temp/nav.png")[1]))
# time.sleep(1)
# loc = template_matching("temp/homebase.png")[1]
# pyautogui.click(win.get_screen_position((loc[0]+300, loc[1]+ 10)))
while True:
    val = template_matching("temp/moonStation.png")[1]
    if(val >= 0.9):
        pyautogui.click(win.get_screen_position(template_matching("temp/finish.png")[1]))
        time.sleep(1)
        pyautogui.click(win.get_screen_position(template_matching("temp/store.png")[1]))
        time.sleep(1)
