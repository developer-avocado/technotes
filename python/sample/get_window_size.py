import pygetwindow as gw
import pyautogui
import time

def get_window_info_at_click():
    print("クリックしてウィンドウを選択してください...")
    
    # 一時的にマウスのクリックを待つ
    time.sleep(1)  # 5秒の待機時間（ユーザーがクリックするための時間）
    
    # 現在アクティブなウィンドウを取得
    active_window = gw.getActiveWindow()
    
    if active_window:
        # ウィンドウの位置とサイズを取得
        x, y = active_window.left, active_window.top
        width, height = active_window.width, active_window.height
        
        print(f"ウィンドウの位置: x = {x}, y = {y}")
        print(f"ウィンドウのサイズ: 幅 = {width}, 高さ = {height}")
    else:
        print("アクティブなウィンドウが見つかりません。")

# 関数を実行
get_window_info_at_click()
