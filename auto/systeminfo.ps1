# 現在の日付と時刻を取得し、フォーマットを調整
$date = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"

# ファイル名を生成
$fileName = "systeminfo_$date.txt"

# systeminfoの出力をファイルに保存
systeminfo > $fileName

Write-Output "System information has been saved to $fileName"
