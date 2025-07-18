import win32gui
import win32con
import time

def minimize_window_by_title(title_fragment):
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            if title_fragment.lower() in window_title.lower():
                win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    time.sleep(5)
    win32gui.EnumWindows(callback, None)