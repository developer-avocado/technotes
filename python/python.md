# Python

## 環境構築

### バージョン指定によるコマンド実行

指定したバージョンのPythonでコマンドを実行する。

```py
$ py -3.8 --version
Python 3.8.10
```

### モジュールの一括インストール

```py
$ pip install -r requirements.txt
```

```txt:requirements.txt
selenium
chromedriver-autoinstaller
```

### SSLエラー発生時のモジュールインストール

```py
pip install requests --trusted-host pypi.org --trusted-host files.pythonhosted.org
```

### 仮想環境の作成手順

1. 任意のディレクトリを作成する。  
2. 作成したディレクトリに移動し、仮想環境を作成する以下コマンドを実行する。  

   ```py
   $ python -m venv .venv
   ```

3. 仮想環境を有効にする。

   ```py
   $ .venv\Scripts\activate
   ```

### chromedriverのインストール

以下のエラーが発生した場合は、chromedriverのモジュールをダウンロードする必要がある。  

```py
Traceback (most recent call last):
  File "test.py", line 10, in <module>
    driver = webdriver.Chrome()
  File "F:\work\venv\.venv\lib\site-packages\selenium\webdriver\chrome\webdriver.py", line 73, in __init__
    self.service.start()
  File "F:\work\venv\.venv\lib\site-packages\selenium\webdriver\common\service.py", line 83, in start
    os.path.basename(self.path), self.start_error_message)
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
```

chromedriver-binaryのモジュールをインストールする。  

```py
$ pip install chromedriver-binary 
```

スクリプトに「import chromedriver_binary」を読み込む。  

```py
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()
driver.get("http://www.python.org")
```

スクリプトを実行したあと、以下のエラーメッセージが表示された場合は、現在のブラウザのバージョンに合うchromdriverをインストールする。  

```py
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 126
Current browser version is 124.0.6367.119 with binary path C:\Program Files\Google\Chrome\Application\chrome.exe
```

現在のブラウザのバージョンが「124.0.6367.119」のため、以下を実行する。

```py
$ pip install chromedriver-binary==124.0.6367.119
```

指定したバージョンがない場合は、以下のエラーが発生する。

```py
>pip install chromedriver-binary==124.0.6367.119
ERROR: Could not find a version that satisfies the requirement chromedriver-binary==124.0.6367.119 (from versions: 2.29.1, 2.31.1, ~中略~ 124.0.6356.2.0, 124.0.6358.0.0, 124.0.6360.0.0, 124.0.6362.0.0, 124.0.6364.0.0, 124.0.6366.2.0, 124.0.6367.2.0, 124.0.6367.8.0, 124.0.6367.29.0, 124.0.6367.49.0, 124.0.6367.60.0, 124.0.6367.78.0, 124.0.6367.91.0, 124.0.6367.155.0, 125.0.6369.0.0, 125.0.6371.0.0, 125.0.6373.0.0, 125.0.6375.0.0, 125.0.6377.0.0, ~中略~ 126.0.6465.2.0, 126.0.6467.2.0)
ERROR: No matching distribution found for chromedriver-binary==124.0.6367.119
WARNING: You are using pip version 21.3.1; however, version 24.0 is available.
You should consider upgrading via the 'f:\work\venv\.venv\scripts\python.exe -m pip install --upgrade pip' command.
```

その場合、指定したバージョンに近いバージョンをインストールする。

```py
$ pip install chromedriver-binary==124.0.6367.155.0
```
