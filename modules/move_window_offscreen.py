import time
import win32gui

def move_window_offscreen(title_fragment):
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            if title_fragment.lower() in window_title.lower():
                win32gui.MoveWindow(hwnd, -2000, -2000, 800, 600, True)
    time.sleep(6)
    win32gui.EnumWindows(callback, None)