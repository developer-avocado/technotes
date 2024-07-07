import win32com.client
import win32gui
import time
import threading

mail_subject = '題目'
mail_Body = '本文'
mail_to ='recipient@example.com'

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

# スレッドを作成
thread = threading.Thread(target=find_mail_window)

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

# 少し待ってOutlookウィンドウを取得
time.sleep(2)


