import win32gui
import win32con
import win32api
import win32ui
from time import sleep
#0x50
hwnd = 0x00040756
# win = win32ui.CreateWindowFromHandle(hwnd)
# win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x50, 0)
# sleep(0.5)
# win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x50, 0)

def get_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds

#hwnd = get_inner_windows(hwnd)['plrNativeInputWindowClass']
win = win32ui.CreateWindowFromHandle(hwnd)
win32gui.SetForegroundWindow(hwnd)


