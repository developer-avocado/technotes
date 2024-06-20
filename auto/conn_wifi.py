# -*- coding: utf-8 -*-
import subprocess
import time

def is_connected():
    """
    ネットワーク接続を確認する関数。
    GoogleのDNSサーバーにpingを送信し、応答があるかを確認します。
    """
    try:
        output = subprocess.check_output(["ping", "-n", "1", "192.168.13.1"], stderr=subprocess.STDOUT, universal_newlines=True)
        if "タイムアウト" in output or "到達できませんでした" in output:
            print(output)
            return False
        return True
    except subprocess.CalledProcessError:
        print(f"ProcessError")
        return False

def connect_wifi(ssid, password):
    """
    指定したSSIDとパスワードでWi-Fiに接続する関数。
    """
    try:
        subprocess.run(["netsh", "wlan", "connect", "name={}".format(ssid)], check=True)
    except subprocess.CalledProcessError as e:
        print("Wi-Fi接続に失敗しました: ", e)

def main():
    ssid = "ssid"  # 接続したいWi-FiのSSID
    password = "password"  # Wi-Fiのパスワード

    while True:
        if not is_connected():
            print("Wi-Fi接続が切断されました。再接続を試みます...")
            connect_wifi(ssid, password)
        else:
            print("Wi-Fi接続が有効です。")
        
        time.sleep(60)  # 60秒ごとに接続状態をチェック

if __name__ == "__main__":
    main()
