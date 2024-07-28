import tkinter as tk
from tkinter import messagebox

def show_dialog(msg):
    # Tkinterのルートウィンドウを作成
    root = tk.Tk()
    root.withdraw()  # メインウィンドウを表示しない

    # メッセージボックスを表示
    messagebox.showinfo("Title", msg)

# ダイアログを表示
show_dialog("これはダイアログです。")