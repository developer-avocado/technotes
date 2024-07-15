import subprocess
import sys
from datetime import datetime
import time

# 現在の日付と時刻を取得し、ファイル名に使える形式に整形する
now = datetime.now()
date_str = now.strftime("%Y-%m-%d_%H-%M-%S")

# ファイル名を生成する
systeminfo_file_name = f"systeminfo_{date_str}.txt"

# コードページをUTF-8に変更してsysteminfoを実行し、出力をUTF-8でファイルに保存する
try:
    # コードページをUTF-8に変更する
    subprocess.run(["C:\\Windows\\System32\\chcp.com", "65001"])

    time.sleep(3)

    # systeminfoの出力をUTF-8でファイルに保存する
    with open(systeminfo_file_name, "w", encoding="utf-8") as file:
        subprocess.run(["systeminfo"], stdout=file, check=True, text=True)

    print(f"System information has been saved to {systeminfo_file_name}")

finally:
    # 変更したコードページを元に戻す
    subprocess.run(["C:\\Windows\\System32\\chcp.com", "932"])

    time.sleep(3)
