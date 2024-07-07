@echo off
REM Pythonスクリプトのパス
set SCRIPT_PATH=path\to\your_script.py

:loop
REM Pythonスクリプトを実行し、エラーログを記録
python %SCRIPT_PATH% 2>> error.log

REM エラーが発生した場合、ログを記録して再起動
if %errorlevel% neq 0 (
    echo %date% %time% - Script stopped with error. Restarting... >> error.log
    timeout /t 5 /nobreak
    goto loop
)

REM 成功終了の場合
echo %date% %time% - Script finished successfully. >> error.log
