# Linux

## 環境設定

### ID/パスワード認証省略化

指定URLにアクセスしたとき、IDとパスワードの入力を不要とするために以下を設定する。  

'''sh:~/.netrc
machine gitlab.hogehoge.net
login sato.taro@piyopiyo.com
password ${PASSWORD}
'''

## 起動プロセス

以下にLinuxの起動プロセスを示す。  

1. マシンの BIOS またはブート ファームウェアがブート ローダーをロードして実行します。
2. ブートローダーはディスク上のカーネルイメージを見つけ、それをメモリにロードして起動します。
3. カーネルはデバイスとそのドライバーを初期化します。
4. カーネルはルート ファイルシステムをマウントします。
5. カーネルはプロセス ID 1 のinitというプログラムを起動します。この時点でユーザー空間が開始されます。
6. init は残りのシステムプロセスを開始させます。
7. ある時点で、init は、通常はブート シーケンスの最後または終わり近くで、ログインを可能にするプロセスを開始します。

## ルートファイルシステム

ルートファイルシステムは、システムが起動して動作するために必要なすべてのディレクトリとファイルを含むファイルシステムです。これには、以下のディレクトリが含まれます：

/bin: 基本的なユーザーコマンド（例：ls, cp, mv）
/sbin: システム管理用コマンド（例：fsck, reboot）
/lib: 基本的なライブラリ
/lib64: 64ビットシステム用の基本的なライブラリ
/etc: システムの設定ファイル
/dev: デバイスファイル
/mnt: 一時的なマウントポイント
/proc: 仮想ファイルシステム（プロセス情報）
/sys: 仮想ファイルシステム（システム情報）
/usr: ユーザーランドのプログラムとライブラリ
/var: 可変データ（ログファイル、スプールディレクトリなど）
/home: ユーザーのホームディレクトリ

/usr ディレクトリ
/usrディレクトリは、ユーザーが利用するプログラムやライブラリ、ドキュメントを格納する場所です。以下のサブディレクトリが含まれます：
/usr/bin: ユーザーが利用する実行可能ファイル（プログラム）
/usr/sbin: システム管理者が利用する実行可能ファイル
/usr/lib: ライブラリファイル
/usr/include: ヘッダーファイル
/usr/share: アーキテクチャに依存しない共有データ（ドキュメント、アイコンなど）
/usr/bin に格納されているプログラム
/usr/binには、多くのユーザーが利用する一般的なプログラムが格納されています。例えば：

テキストエディタ（例：nano, vim）
システムユーティリティ（例：grep, awk）
ネットワークツール（例：curl, wget）

### ルートファイルシステムに含まれることの確認方法

ルートファイルシステムに含まれるファイルやディレクトリは、通常、マウントされたルートファイルシステムのパスとして確認できます。以下のように確認します。

```bash
ls /
```

出力例：

```bash
bin   dev  home  lib64  mnt  root  sbin  sys  usr
boot  etc  lib   media  opt  run   srv   tmp  var
```

/usrディレクトリを確認する：

```bash
ls /usr
```

出力例：

```bash
bin  include  lib  local  sbin  share
```

## カーネルとルートファイルシステムの役割の違い

### カーネル

役割: ハードウェアとソフトウェアの橋渡しを行うオペレーティングシステムの中核部分。

主要な機能:
スケジューリング: プロセスの実行順序を管理し、CPUリソースを効率的に割り当てる。
プロセス管理: プロセスの作成、終了、状態管理を行う。
メモリ管理: 物理メモリと仮想メモリの管理を行う。
デバイス管理: デバイスドライバを通じてハードウェアリソースにアクセスする。
ファイルシステム管理: ファイルシステムを管理し、ファイルの読み書きを行う。
ネットワーク管理: ネットワークプロトコルの実装とデータ転送を行う。
セキュリティ管理: アクセス制御やユーザー認証を行う。

### ルートファイルシステム

役割: カーネルが動作するためのユーザーランドの環境を提供する。

主要な内容:
ユーザーランドツール: 基本的なコマンドやユーティリティ（例：ls, cp, grep）。
ライブラリ: プログラムが動作するために必要な共有ライブラリ（例：/lib, /usr/lib）。
設定ファイル: システムやアプリケーションの設定ファイル（例：/etc）。
ユーザープロセス: カーネルが起動した後に実行されるユーザーレベルのプロセスやデーモン。

### 具体例

#### カーネル機能

これらの機能はカーネルに含まれており、通常はファイルシステム上のファイルとしては直接見ることはできません。カーネルのコードはカーネルイメージ（例：bzImage）としてメモリにロードされ、実行時に動作します。

#### ルートファイルシステムの内容

ルートファイルシステムには、以下のようなディレクトリとファイルが含まれます。

/bin: 基本的なユーザープログラム（例：bash, ls, cp）。
/sbin: システム管理用プログラム（例：ifconfig, shutdown）。
/lib: 基本的な共有ライブラリ。
/etc: システムの設定ファイル（例：passwd, fstab）。
/usr: 追加のユーザープログラムやライブラリ。
/var: 可変データ（ログファイル、スプールディレクトリ）。

## トラブルシューティング
