# VNC

## VNCサーバー環境構築

以下は、TigerVNCをインストールして設定する基本的な手順の例です：

1. TigerVNCのインストール

```shell
sudo apt-get update
sudo apt install tightvncserver
```

1. デスクトップ環境のインストール

```shell
$ sudo apt install xfce4 xfce4-goodies
$ sudo apt install lxde
```

1. VNCパスワードの設定

   ```shell
   $ vncpasswd
   ```

1. Xリソースの設定

  この設定により、VNCセッションが開始されるときにユーザーが好むX設定が反映されます。たとえば、xtermのカーソルの色を変更したりすることができます。  

  ```shell
  $ touch $HOME/.Xresources
  ```

1. 初回VNCサーバーの起動

   ```shell
   $ vncserver
   ```

1. VNCサーバーの設定ファイルの編集（オプション）

   ~/.vnc/xstartupファイルを編集して、必要なデスクトップ環境を起動するように設定します。例えば、GNOMEデスクトップを使用する場合：

   ```shell
   #!/bin/sh
   xrdb $HOME/.Xresources
   startxfce4 &
   ```

1. VNCサーバーの再起動

   ```shell
   vncserver -kill :1
   vncserver :1 -geometry 1920x1080 -depth 24
   ```

## VNCクライアント環境構築

1. RealVncのインストールします。  

1. RealVncを起動し、[File] > [New Connection]をクリックします。  

1. [VNC Server]に「192.168.0.19:5901」を入力し、[OK]をクリックします。  

1. 作成されたVNC Viewerをダブルクリックし、パスワードを入力し、接続します。  
