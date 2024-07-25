import pynput.mouse as mouse
import tkinter as tk
from tkinter import simpledialog
import yaml
import threading
import keyboard

# クリック位置と名前のペアを記録する辞書
click_positions = {}

def get_name(x, y):
    # GUIダイアログで名前を取得
    root = tk.Tk()
    root.withdraw()  # GUIウィンドウを非表示にする
    name = simpledialog.askstring("Input", f"Enter a name for the position ({x}, {y}):")
    root.destroy()  # ダイアログを閉じる
    return name

def on_click(x, y, button, pressed):
    if pressed:
        # 名前を取得するためのスレッドを開始
        threading.Thread(target=lambda: record_position(x, y)).start()

def record_position(x, y):
    name = get_name(x, y)
    if name:
        click_positions[name] = (x, y)
        print(f"Position ({x}, {y}) recorded with name '{name}'")

def save_to_yaml(data, filename):
    with open(filename, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"Data saved to {filename}")

# マウスリスナーの開始
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

print("Listening for mouse clicks... Press 'q' to stop.")

# 'q'キーの待機
try:
    while True:
        if keyboard.is_pressed('q'):
            break
finally:
    # リスナーを停止し、データを保存
    mouse_listener.stop()
    save_to_yaml(click_positions, 'click_positions.yaml')
