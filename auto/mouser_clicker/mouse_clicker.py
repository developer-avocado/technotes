import subprocess
import time
import cv2
import numpy as np
import common
from pathlib import Path
import pyautogui
import yaml

import win32gui
import win32con

def find_window_by_partial_title(partial_title):
    """タイトルの一部を含むウィンドウを検索する"""
    def enum_windows_proc(hwnd, titles):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            if partial_title in window_title:
                titles.append(hwnd)
        return True  # 続行する
    
    windows = []
    win32gui.EnumWindows(enum_windows_proc, windows)
    return windows

def move_window(hwnd, x, y, width, height):
    """ウィンドウを新しい位置に移動する"""
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, width, height, win32con.SWP_NOACTIVATE | win32con.SWP_NOZORDER)

f = open('params.yaml', 'r')
params = yaml.safe_load(f)
f.close()

# 設定項目
# 操作したいウィンドウの名前を設定
partial_title = params['window_title']
# 新しい位置とサイズを指定
new_x = params['new_x']
new_y = params['new_y']
new_width = params['new_width']
new_height = params['new_height']

hwnd_list = find_window_by_partial_title(partial_title)

if not hwnd_list:
    print("指定したタイトルを含むウィンドウが見つかりませんでした。")

for hwnd_main in hwnd_list:
    print(f"ウィンドウ HWND: {hwnd_main}")
    # ウィンドウの位置を変更する
    move_window(hwnd_main, new_x, new_y, new_width, new_height)
    win32gui.SetForegroundWindow(hwnd_main)

time.sleep(1)

#while True:
for i in range(0,1):
    f = open('params.yaml', 'r')
    params = yaml.safe_load(f)
    f.close()

    time.sleep(0.5)

    if type(params) != 'NoneType':
        state = params['state']

    if state == 'run':
        img = pyautogui.screenshot('screen.png')

        template_list = [p.name for p in Path('.').glob('./**/*.png') if p.name != ('screen.png')]
        print(template_list)
        
        screenshot = cv2.imread('screen.png')
        flag = False
        for t in template_list:
            template = cv2.imread(t)
            result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            print(f'template: {t}, max_val: {max_val}, max_loc: {max_loc}')

            height, width, _ = template.shape
            
            if max_val > 0.8:
                print(f'matched template!')
                result = pyautogui.click(max_loc[0] + width/2, max_loc[1] + height/2)
            time.sleep(1)
