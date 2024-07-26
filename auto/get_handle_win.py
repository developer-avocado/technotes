import win32gui
import win32api
import win32con

def find_window(title=None, class_name=None):
    """ウィンドウハンドルを取得する"""
    return win32gui.FindWindow(class_name, title)

def find_child_window(parent_hwnd, title=None, class_name=None):
    """親ウィンドウ内の子ウィンドウハンドルを取得する"""
    return win32gui.FindWindowEx(parent_hwnd, 0, class_name, title)

def list_child_windows(parent_hwnd):
    """親ウィンドウ内の全子ウィンドウのハンドルをリスト化する"""
    child_windows = []
    
    def enum_child_windows(hwnd, lParam):
        child_windows.append(hwnd)
    
    win32gui.EnumChildWindows(parent_hwnd, enum_child_windows, None)
    return child_windows

def main():
    # ウィンドウタイトルを指定してウィンドウハンドルを取得
    window_title = "Untitled - Notepad"  # 対象のウィンドウタイトルに変更
    hwnd = find_window(title=window_title)
    
    if hwnd:
        print(f"Found window handle: {hwnd}")
        
        # 親ウィンドウ内の全子ウィンドウのハンドルをリスト化
        child_hwnds = list_child_windows(hwnd)
        print("Child window handles:")
        for child_hwnd in child_hwnds:
            print(f"Child window handle: {child_hwnd}")
            
            # 各子ウィンドウのタイトルを取得
            child_title = win32gui.GetWindowText(child_hwnd)
            print(f"  Title: {child_title}")
            
            # 各子ウィンドウのクラス名を取得
            child_class_name = win32gui.GetClassName(child_hwnd)
            print(f"  Class Name: {child_class_name}")
    else:
        print("Window not found")

if __name__ == "__main__":
    main()
