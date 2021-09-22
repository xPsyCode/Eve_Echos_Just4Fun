import pygetwindow, time, cv2, pyautogui,random
from capture import WindowCapture


#Resize window for image detection
win = pygetwindow.getWindowsWithTitle("BlueStacks")[1]
win.size = (1396, 800)

win = WindowCapture("BlueStacks")
belt_list = [(1150, 100),(1150, 170),(1150, 240),(1150, 310)]
def img_dect(image:str):
    img = win.get_screenshot()
    temp = cv2.imread("temp/"+image+".png")
    res =cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_val, win.get_screen_position(max_loc)

def wait_appear(image:str):
    while True:
        val = img_dect(image)[0]
        if val >= 0.9:
            break
        else:
            time.sleep(2)

def wait_disappear(image:str):
    while True:
        val = img_dect(image)[0]
        if val < 0.85:
            break
        else:
            time.sleep(2)


while True:
    # Fly to mining locaction
    time.sleep(1)
    pyautogui.click(img_dect("nav_sym")[1])
    time.sleep(1)
    pyautogui.click((img_dect("mining_loc")[1][0]+250,img_dect("mining_loc")[1][1]+5))
    time.sleep(1)
    pyautogui.click(img_dect("submit")[1])

    # Wait for arrived
    wait_appear("loc_arrived")
    time.sleep(9)

    # Select belt
    pyautogui.click(img_dect("nav_list")[1])
    time.sleep(1)
    pyautogui.click(win.get_screen_position((1150, 30)))
    time.sleep(1)
    pyautogui.click(img_dect("belt")[1])
    time.sleep(1)
    pyautogui.click(win.get_screen_position(random.choice(belt_list)))
    time.sleep(1)
    pyautogui.click(img_dect("warp")[1])
    time.sleep(5)
    pyautogui.click(win.get_screen_position((1150, 30)))
    time.sleep(1)
    pyautogui.click(img_dect("asta")[1])
    wait_disappear("no_asta")
    time.sleep(3)

    # Select an asta
    pyautogui.click(img_dect("nav_list")[1])
    time.sleep(3)
    pyautogui.click(img_dect("nav_list")[1])
    time.sleep(1)
    x, y = img_dect("plag")[1]
    pyautogui.click((x,y),clicks=2)
    time.sleep(1)
    pyautogui.click((x,y+80),clicks=2)
    time.sleep(1)
    pyautogui.click((x,y+160),clicks=2)
    time.sleep(1)
    pyautogui.click((x,y+240),clicks=2)
    time.sleep(1)
    pyautogui.click((x,y))
    time.sleep(1)

    #Start mining
    pyautogui.click(img_dect("get_closer")[1])
    pyautogui.press("W")
    wait_appear("15km")
    pyautogui.click(img_dect("15km")[1])
    time.sleep(1)
    pyautogui.press("W")
    time.sleep(1)
    pyautogui.press("Q")
    pyautogui.press("E")
    pyautogui.click(win.get_screen_position((1000, 500)))
    i = 0
    while i < 1800:
        val = img_dect("finish")[0]
        if val >= 0.9:
            break
        else:
            time.sleep(1)
            i += 1

    # Fly home
    pyautogui.click(img_dect("nav_sym")[1])
    time.sleep(1)
    pyautogui.click((img_dect("homebase")[1][0]+250,img_dect("homebase")[1][1]+5))
    wait_appear("homebase_sym")
    time.sleep(5)
    # Clear payload
    pyautogui.click(win.get_screen_position((30, 110)))
    time.sleep(3)
    pyautogui.click(img_dect("payload")[1])
    time.sleep(1)
    pyautogui.click(win.get_screen_position((1050, 700)))
    time.sleep(1)
    pyautogui.click(win.get_screen_position((50, 150)))
    time.sleep(1)
    pyautogui.click(win.get_screen_position((300, 150)))
    time.sleep(1)
    pyautogui.click(win.get_screen_position((1250, 50)))