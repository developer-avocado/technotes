# Arduino

## 参考情報

### [LESSON 1: 初心者のための始め方](https://docs.sunfounder.com/projects/elite-explorer-kit/ja/latest/video_lesson/lesson01.html)

## 環境構築

### VNCサーバーの起動

1. VNCサーバーを起動する。  

  ```
  $ vncserver :1 -geometry 1920x1080 -depth 24
  ```

2. クライアントPC(Win)でVNC Viewerを起動する。  

### Arduinoのインストール

1. Arduino IDEを任意のディレクトリにダウンロードする。  

  ```
  $ wget https://github.com/arduino/arduino-ide/releases/download/2.2.1/arduino-ide_2.2.1_Linux_64bit.zip
  ```

2. Arduino IDEを解凍する。  

  ```
  $ unzip arduino-ide_2.2.1_Linux_64bit.zip 
  ```

3. 解凍したArduinoを確認する。  

  ```
  $ ls arduino-ide_2.2.1_Linux_64bit -l
  total 207112
  -rwxr-xr-x 1 develop develop 166452616  8月 31  2023 arduino-ide
  -rw-r--r-- 1 develop develop    130438  8月 31  2023 chrome_100_percent.pak
  -rw-r--r-- 1 develop develop    181852  8月 31  2023 chrome_200_percent.pak
  -rwxr-xr-x 1 develop develop   1271152  8月 31  2023 chrome_crashpad_handler
  -rwxr-xr-x 1 develop develop     54000  8月 31  2023 chrome-sandbox
  -rw-r--r-- 1 develop develop  10541296  8月 31  2023 icudtl.dat
  -rwxr-xr-x 1 develop develop    250496  8月 31  2023 libEGL.so
  -rwxr-xr-x 1 develop develop   2855152  8月 31  2023 libffmpeg.so
  -rwxr-xr-x 1 develop develop   6536848  8月 31  2023 libGLESv2.so
  -rwxr-xr-x 1 develop develop   4497352  8月 31  2023 libvk_swiftshader.so
  -rwxr-xr-x 1 develop develop   6403496  8月 31  2023 libvulkan.so.1
  -rw-r--r-- 1 develop develop      1096  8月 31  2023 LICENSE.electron.txt
  -rw-r--r-- 1 develop develop   6762117  8月 31  2023 LICENSES.chromium.html
  drwxr-xr-x 2 develop develop      4096  8月 31  2023 locales
  drwxr-xr-x 3 develop develop      4096  8月 31  2023 resources
  -rw-r--r-- 1 develop develop   5458761  8月 31  2023 resources.pak
  -rw-r--r-- 1 develop develop    162352  8月 31  2023 snapshot_blob.bin
  -rw-r--r-- 1 develop develop    476792  8月 31  2023 v8_context_snapshot.bin
  -rw-r--r-- 1 develop develop       107  8月 31  2023 vk_swiftshader_icd.json
  ```

4. VNC Serverのディスプレイを環境変数に設定する。  

  ```
  $ export DISPLAY=:1
  ```

5. Arduino IDEを起動する。  

  ```
  $ ./arduino-ide
  ```

6. デバイスへのアクセスを許可する。  

  ```
  $ sudo usermod -a -G dialout <username>
  $ sudo chmod a+rw /dev/ttyACM0
  ```

  https://arduino-er.blogspot.com/2014/08/arduino-ide-error-avrdude-seropen-cant.html

