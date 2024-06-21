# -*- coding: utf-8 -*-
import subprocess
import time
from datetime import datetime

conn_error_count = 0

def is_connected():
    """
    ネットワーク接続を確認する関数。
    GoogleのDNSサーバーにpingを送信し、応答があるかを確認します。
    """
    try:
        output = subprocess.check_output(["ping", "-n", "1", "192.168.13.1"], stderr=subprocess.STDOUT, universal_newlines=True)
        now = datetime.now()
        print(f"{now}: {output}")
        if "タイムアウト" in output or "到達できません" in output:
            with open("error.log", 'a', encoding='utf-8') as f:
                f.writelines(f"{now}: {output}\n")
            return False
        return True
    except subprocess.CalledProcessError:
        now = datetime.now()
        msg = f"プロセスエラー発生。"
        print(f"{now}: {msg}")
        with open("error.log", 'a', encoding='utf-8') as f:
            f.writelines(f"{now}: {msg}\n")
        return False

def connect_wifi(ssid, password):
    global conn_error_count
    """
    指定したSSIDとパスワードでWi-Fiに接続する関数。
    """
    try:
        subprocess.run(["netsh", "wlan", "connect", "name={}".format(ssid)], check=True)
        now = datetime.now()
        msg = f"Wi-Fi接続に成功しました。"
        print(f"{now}: {msg}")
        with open("error.log", 'a', encoding='utf-8') as f:
            f.writelines(f"{now}: {msg}\n")
    except:
        now = datetime.now()

        conn_error_count += 1
        print(f"{now}: error {conn_error_count}")

        msg = f"Wi-Fi接続に失敗しました"
        print(f"{now}: {msg}")
        with open("error.log", 'a', encoding='utf-8') as f:
            f.writelines(f"{now}: {msg}\n")

        if conn_error_count > 3:
            now = datetime.now()
            msg = "exit"
            print(f"{now}: {msg}")
            with open("error.log", 'a', encoding='utf-8') as f:
                f.writelines(f"{now}: {msg}\n")                    
                exit()
def main():
    ssid = ""  # 接続したいWi-FiのSSID
    password = "password"  # Wi-Fiのパスワード

    while True:
        if not is_connected():
            now = datetime.now()
            msg = "Wi-Fi接続が切断されました。再接続を試みます..."
            print(f"{now}: {msg}")
            with open("error.log", 'a', encoding='utf-8') as f:
                f.writelines(f"{now}: {msg}\n")
            connect_wifi(ssid, password)
        else:
            now = datetime.now()
            msg = "Wi-Fi接続が有効です。"
            print(f"{now}: {msg}")
        
        time.sleep(60)  # 60秒ごとに接続状態をチェック
if __name__ == "__main__":
    main()
