import ctypes
from ctypes import wintypes

# 必要な Windows API 関数を定義
FindWindow = ctypes.windll.user32.FindWindowW
FindWindowEx = ctypes.windll.user32.FindWindowExW
EnumChildWindows = ctypes.windll.user32.EnumChildWindows
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
SendMessage = ctypes.windll.user32.SendMessageW

# 関数の引数と戻り値の型を設定
FindWindow.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR]
FindWindow.restype = wintypes.HWND
FindWindowEx.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.LPCWSTR, wintypes.LPCWSTR]
FindWindowEx.restype = wintypes.HWND
EnumChildWindows.argtypes = [wintypes.HWND, ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM), wintypes.LPARAM]
EnumChildWindows.restype = wintypes.BOOL
GetWindowTextLength.argtypes = [wintypes.HWND]
GetWindowText.argtypes = [wintypes.HWND, wintypes.LPWSTR, wintypes.INT]
SendMessage.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
SendMessage.restype = wintypes.LPARAM

# 定数定義
BM_CLICK = 0x00F5

# コールバック関数の定義
def enum_child_windows_proc(hwnd, lparam):
    length = GetWindowTextLength(hwnd)
    buffer = ctypes.create_unicode_buffer(length + 1)
    GetWindowText(hwnd, buffer, length + 1)
    #if buffer.value == "接続(N)":
    #    print(f"ボタンのハンドル: {hwnd}")
    #SendMessage(hwnd, BM_CLICK, 0, 0)
    return True

# コールバック関数の型を定義
WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
enum_proc = WNDENUMPROC(enum_child_windows_proc)

# 親ウィンドウのタイトルを指定
parent_window_title = "リモート デスクトップ接続"

# 親ウィンドウのハンドルを取得
parent_hwnd = FindWindow(None, parent_window_title)

if parent_hwnd:
    print(f"親ウィンドウのハンドル: {parent_hwnd}")
    
    # 子ウィンドウを列挙してボタンを探し、クリック
    EnumChildWindows(parent_hwnd, enum_proc, 0)
else:
    print("親ウィンドウが見つかりませんでした。")
