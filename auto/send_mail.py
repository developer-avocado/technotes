import win32com.client
import win32gui
import win32con
import time
import threading
import sys

mail_subject = sys.argv[1]
mail_Body = sys.argv[2]
mail_to = sys.argv[3]

def find_mail_window():
    time.sleep(3)
    def callback(hwnd, mail_window):
        title = win32gui.GetWindowText(hwnd)
        global mail_subject
        if mail_subject in title:
            mail_window.append(hwnd)
        return True
    
    mail_window = []
    win32gui.EnumWindows(callback, mail_window)

    if mail_window:
        for hwnd in mail_window:
            # ウィンドウを最前面に表示
            win32gui.SetForegroundWindow(hwnd)
    else:
        print("Outlook window not found.")

def move_mail_window_to_top():
    time.sleep(5)
    
    # すべてのウィンドウを列挙する
    def callback(hwnd, hwnds):
        if mail_subject.lower() in win32gui.GetWindowText(hwnd).lower():
            hwnds.append(hwnd)
        return True
    
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)

    if hwnds:
        # 最初に見つかったウィンドウを最前面に表示する
        hwnd = hwnds[0]
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # ウィンドウを元のサイズと位置に戻す
        win32gui.SetForegroundWindow(hwnd)              # ウィンドウを最前面に移動する
    else:
        print(f"タイトルに '{mail_subject}' を含むウィンドウが見つかりませんでした。")

# スレッドを作成
thread = threading.Thread(target=move_mail_window_to_top)

# スレッドを開始
thread.start()

# Outlookアプリケーションを起動
outlook = win32com.client.Dispatch("Outlook.Application")

# 新しいメールアイテムを作成
mail = outlook.CreateItem(0)
mail.Subject = mail_subject
mail.Body = mail_Body
mail.To = mail_to
mail.display(True)

# メールを送信
#mail.Send()

print("Email sent successfully.")


