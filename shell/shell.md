# How to use shell

## 基本 / Basic

### ユーザ権限 / User Permission

Linuxには以下の様に3種類のユーザが存在する。

- 管理者(アドミニストレータ)
- システムユーザ
- 一般ユーザ

管理者は、Linuxでな何でもできるユーザ。すべてのコマンドの実行、デバイスへのアクセス、どのファイルでも閲覧/編集/削除ができる。
一般ユーザは許可されたアクションしかできない。
システムユーザは、管理者でもなく、一般ユーザでもないユーザ。WEBサーバやSMPT等のサーバソフトウェアを動作させるために利用されるユーザ。
どのユーザなのかは、シェルとコマンドから判断できる。
以下の例は、一般ユーザのユーザ名がryousuke、管理者のユーザ名がroot、ホスト名がaxlという環境でログインした場合の表示例。

```{.shell}
# 一般ユーザ
$ ryosuke@Caxl:~＄
```

```{.shell}
# 管理者
$ root@Caxl:~#  
```

これらは、｢ユーザ名＠ホスト名ディレクトリ名プロンプト」を意味する文字を表示して、ユーザの入力を待っている。プロンプトは一般ユーザでは「$」、管理者は「#」になっている。
必要に迫られて管理者権限を利用したい場合は、実行ユーザを切り替えてコマンドを実行するsudoやsuを使用する。Ubuntuなど、そもそもrootユーザを使わせないポリシーのディストリビューションもある。これらのディストリビューションではsudoを実行することをすすめている。

### コマンドの記述 / How to Write Command

コマンド記述例を以下に示す。

```{.shell}
$ ls -alt /var/log
```

ここでは、lsはコマンド、-altはオプション、/var/logは引数を表す。

```{.shell}
$ openssl x509 -in cert.pem -noout -text
```

ここでは、opennsslはコマンド、x509は内部コマンド、-inはオプション、cert.pemは引数、-nooutはオプション、-textはオプションを表す。このような内部コマンドや複数のオプションとそれに対応する引数を渡せることもある。

### オプション

オプションはそのコマンドの動作を変えるための指令。
オプションには、ショートオプションとロングオプションがある。
lsコマンドを例にとると、-aがショートオプションで、--allがロングオプション。どちらを利用しても動作は同じ。ショートオプションは、「-a」と「-l」を合わせて「-al」と記述できるが、ロングオプションはそれぞれで入力する必要がある。

### 引数

引数はそのコマンドの操作対象などを指定する。
lsコマンドでは、「ls /bin」のように、引数として、/binを指定すると、/binディレクトリやファイルの情報を表示できる。

### アクセス権

複数ユーザで利用できるUNIX環境では、ファイルやディレクトリへのアクセス権限が設定されている。アクセス権限の対象は、ファイルの所有者/所属グループ/その他ユーザがあり、それぞれに読み込み/書き込み/実行の3つの権限が設定できる。コマンドの場合は、読み込み/実行がユーザに許されていないとユーザーはコマンドを実行できない。

アクセス権の例を以下に示す。

```{.shell}
$ -rwxr-xr-x 1 root root 133792  1月 18  2018 /bin/ls
```

-rwxr-xr-xの意味は以下の通り。
-: ファイルの種類を表す。「-」はファイル、「d」はディレクトリ、「l」はシンボリックリンク
rwx: 所有者に対するアクセス権限。読み込み/書き込み/実行が可能。
r-x: 所有グループに対するアクセス権限。読み込み/実行が可能。
r-x: その他のユーザに対するアクセス権限。読み込み/実行が可能。

root rootの意味は以下の通り。
root: 所有者が所属するグループを表す
root: 所有者が所属するグループを表す。

ユーザ/グループに関する詳細は、[Linuxのユーザーとグループって何だろう？](https://atmarkit.itmedia.co.jp/ait/articles/1706/02/news014.html)を参照。

ユーザーの情報は、「/etc/passwd」ファイルに保存されている。
書式は、「ユーザー名:パスワード:ユーザーID:グループID:その他の情報:ホームディレクトリ:シェル」

```{.shell}
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
~ 中略 ~
gnome-initial-setup:x:120:65534::/run/gnome-initial-setup/:/bin/false
gdm:x:121:125:Gnome Display Manager:/var/lib/gdm3:/bin/false
dev:x:1000:1000:dev,,,:/home/dev:/bin/bash
sshd:x:122:65534::/run/sshd:/usr/sbin/nologin
```

グループの情報は、「/etc/group」ファイルに保存されている。
書式は、「グループ名:パスワード:グループID:ユーザーリスト」

```{.shell}
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
~中略~
pulse-access:x:124:
gdm:x:125:
dev:x:1000:
```

ユーザは複数のグループに所属することができる。この中で、ログイン時のグループを「プライマリーグループ」、それ以外のグループを「セカンダリーグループ」と呼ぶ。
例えば、「staff」というユーザがファイルを作成した場合、ファイルの所有者はstaff、所有グループはプライマリーグループとなる。
なお、ファイルやディレクトリの属性として保存されるのは、「ユーザID」と「グループID」。「ls -l」などで所有者を確認する際には、「/etc/passwd」と「/etc/passwd」が参照される。

### 標準入力/標準出力/標準エラー出力

UNIXコマンドの出力を別コマンドの入力にしたり、ファイルに出力したりできる。  
UNIXコマンドは実行されるとプロセスとなり、3つの入出力チャンネルを持つ。  

- 標準入力: プロセスへの入力となるチャンネル
- 標準出力: プロセスの結果を出力するチャンネル
- 標準エラー出力: エラーメッセージを出力するチャンネル

特に指定しない限り、標準入力はキーボード、標準出力/標準エラー出力はディスプレイが利用される。

## 頻出コマンド例

### ファイルへの書き込み操作も特権ユーザーとして実行する

```{.shell}
sudo sh -c 'find ./ -type f > a.txt'
```

### コマンドを探す / Find out Commands

```{.shell}
$ whatis -w "*user*"
```

### コマンドの使い方を調べる / Find out How to Use Commands

```{.shell}
$ man ls
```

```{.shell}
$ ls --help
```

```{.shell}
$ git add --help
```

### ファイルを検索する / Find for Files

```{.shell}
$ find ./ -type f print0 | xargs -0 ls -altr --time-style="+%Y%m%d_%H%M%S" | sort -k6
```

```{.shell}
$ find ./ -type f -name "*.py" -or -name "*.md" ! -path "./test_exclude_01/*" ! -path "./test_exclude_02/*" -print0 | xargs -0 ls -altr --time-style="+%Y%m%d_%H%M%S" | sort -k 6 2>/dev/null
```

```{.shell}
$ find ./ -type f -print0 | xargs -0 ls -alt | awk '{print $5" "$9}' | sort -nk1
```

### 特定のディレクトリを除外し、ファイルを検索する

```{.shell}
find /path/to/search -type d -name 'exclude_dir' -prune -o -type f -print
```

### 指定日時以降のファイルを検索する

```{.shell}
find ./ -type f -newermt "2023-06-18 13:30" print0 | xargs -0 ls -altr --time-style="+%Y%m%d_%H%M%S" | sort -k6
```

### 実行権限が付与されていないファイルを検索する

### 指定文字列で検索した行の前後の内容も取得する

```{.shell}
$ grep -10 test
```

### xargsで任意の位置にパラメータを渡す

```{.shell}
$ find ./ -name "*.png" | xargs -I{} mv {} img
```

```{.shell}
$ echo "one two three" | xargs command arg1 arg2 arg3
```

```{.shell}
$ echo "one two three" | xargs -I{} command {} arg1 arg2 arg3
```

```{.shell}
$ echo "one two three" | xargs -I{} command arg1 {} arg2 arg3
```

### xargsで引数を一つずつ渡す

```{.shell}
$ echo "apple banana orange" | xargs -n 1 echo
```

### xargsで複数のコマンドを実行する

```{.shell}
$ find . -name "*.txt" | xargs -I{} sh -c 'echo {}; cat {}'
```

### 特定のファイルを検索し、そのファイルが格納されているディレクトリに移動する

```{.shell}
cd $(dirname $(find ./ -name "robot.md"))
```

```{.shell}
cd $(dirname $(find / -name "target_file.txt" -print -quit 2>/dev/null))
```

### 特定のファイルを検索し、そのファイルが格納されているディレクトリに移動する

```{.shell}
#!/bin/bash

# 検索するファイル名を指定
file_name="target_file.txt"

# 検索を開始するディレクトリを指定
search_dir="/"

# ファイルを検索し、そのディレクトリに移動する
file_path=$(find $search_dir -name $file_name)
if [ -n "$file_path" ]; then
    cd $(dirname $file_path)
    echo "Found $file_name in $PWD"
else
    echo "File not found: $file_name"
fi
```

### 特定のファイル名の拡張子を変更する

```{.shell}
find /path/to/directory -type f -name "*.txt" -exec sh -c 'mv "$0" "${0%.txt}.md"' {} \;
```

### プロセスのバッチ処理

```{.shell}
$ ps aux | grep "python" | awk '{print $2}' | xargs kill
```

### シェルスクリプトをバイナリに変換

シェルスクリプトをバイナリのようにどこでも実行可能にするには、シェルスクリプトをバイナリに変換する必要があります。この場合、バイナリに変換するためにはいくつかのツールがありますが、ここでは shc (Shell Script Compiler) を使用する方法を紹介します。

shc は、シェルスクリプトをバイナリに変換するコンパイラです。shc を使用すると、シェルスクリプトをバイナリに変換して、どこでも実行可能な形式にすることができます。

shc を使用する手順は以下の通りです。

shc をインストールする。
shc は、一般的な Linux ディストリビューションのパッケージマネージャーからインストールできます。例えば、Debian/Ubuntu の場合は以下のようにしてインストールできます。

```{.shell}
$ sudo apt-get install shc
```

シェルスクリプトをバイナリに変換する。
変換するシェルスクリプトが example.sh の場合は、以下のようにしてバイナリに変換します。

```{.shell}
$ shc -f example.sh
```

このコマンドを実行すると、カレントディレクトリに example.sh.x というバイナリファイルが生成されます。

バイナリファイルを実行する。
生成されたバイナリファイルは、シェルスクリプトと同じように実行可能です。例えば、以下のようにして実行できます。

```{.shell}
$ ./example.sh.x
```

以上の手順で、シェルスクリプトをバイナリに変換して、どこでも実行可能な形式にすることができます。ただし、注意点として、バイナリに変換することでシェルスクリプトの中身が暗号化されるわけではないため、セキュリティ上の注意が必要です。

### パスの末尾のフォルダやファイルを取り除く

```{.shell}
#!/bin/bash

test="/path/to/some/folder/doc"

content="${test}"
echo -n '${test}: '
echo "$content"

content="${test%/*}"
echo -n '${test%/*}: '
echo "$content" 

content="${test%/folder*}"
echo -n '${test%/folder*}: '
echo "$content" 

content=${test%/*/*/*}
echo -n '${test%/*/*/*}: '
echo "$content" 
```

実行ログ:

```{.shell}
${test}: /path/to/some/folder/doc
${test%/*}: /path/to/some/folder
${test%/folder*}: /path/to/some
${test%/*/*/*}: /path/to
```

### フォルダ名やファイル名を一括置換する

```{.shell}
#!/bin/bash

target_dir="/home/develop/work/tech"
find_name="img"
replace_name="images"
file_type="d"

found_items="$(find $target_dir -type $file_type -name $find_name)"
echo "found items: $found_items"

for item in $found_items; do
 mv $item "${item%/*}/${replace_name}"
done

replaced_items="$(find $target_dir -type $file_type -name $replace_name)"
echo "replaced items: $replaced_items"
```

### 特定の日付形式の一部を正規表現で置換する

特定の形式だけを対象とする場合、Vimの正規表現を使ってより詳細なパターンを指定できます。以下のようにコマンドを書くと、2023/08/07 といった形式のみが置換されます。

```{.shell}
:%s/\(\d\{4}\)\/\(\d\{2}\)\/\(\d\{2}\)/\1-\2-\3/g
このコマンドは以下のように動作します：
```

\(\d\{4}\), \(\d\{2}\), \(\d\{2}\)： \d は数字にマッチし、\{n\} は直前の文字がn回繰り返すことにマッチします。() で囲むことで、マッチした部分を後で参照できるようにしています。
\/: スラッシュ（/）にマッチするためのエスケープ。
\1-\2-\3: 置換後の形式。\1, \2, \3 はそれぞれ最初、2番目、3番目の () でマッチした内容になります。
このようにすると、指定した形式の日付だけが置換されます。

## コマンド編

### エディタ / ページャ

### ファイル/ディレクトリ管理

#### realpath

realpath コマンドは、シンボリックリンクを含むファイルやディレクトリの絶対パスを取得するために使用されます。オプションを指定せずに実行すると、カレントディレクトリからの相対パスが表示されます。

realpath ファイルパス
例

ファイル "test.txt" の絶対パスを取得

```shell
realpath test.txt
```

シンボリックリンクの場合

シンボリックリンクの場合は、リンク先のファイルやディレクトリの絶対パスが表示されます。

シンボリックリンク "link" の絶対パスを取得

```shell
realpath link
```

オプション

-s: シンボリックリンクのパスを表示します。
-f: 存在しないファイルのパスも処理します。

#### xargs

Ref:
<https://daeudaeu.com/pipe-xargs/>
<http://192.168.0.8/drive/book/%e3%83%91%e3%82%a4%e3%83%97%20%20%20%e3%81%ab%e3%81%a4%e3%81%84%e3%81%a6%e8%a7%a3%e8%aa%ac%ef%bc%88%20%20%20%e3%81%a8%20%20%20xargs%20%e3%81%ae%e9%81%95%e3%81%84%e3%82%82%e7%90%86%e8%a7%a3%e3%81%a7%e3%81%8d%e3%82%8b%ef%bc%81%ef%bc%89%20%20%20%e3%81%a0%e3%81%88%e3%81%86%e3%83%9b%e3%83%bc%e3%83%a0%e3%83%9a%e3%83%bc%e3%82%b8.pdf>

xargs command builds and executes commands from standard input, STDIN ( Chapter 15). It is a great command to use at the end of a pipe, building and executing commands from each STDIN item produced.

xargs command is actually killing off each process via its PID using the absolute directory reference of the kill command and sudo :
(xargsコマンドは、killコマンドsudoの絶対ディレクトリ参照を使用して、PIDを介して各プロセスを実際に強制終了しています。)

```{.shell}
# -d: 区切り文字の指定
$ command_3="xargs -d \\n /usr/bin/sudo /bin/kill -9"
```

xargsコマンドを使用して、引数を任意の場所に渡す方法はいくつかあります。以下にいくつかの例を示します。

引数をコマンドの最後の引数として渡す：

```{.shell}
$ echo "one two three" | xargs command arg1 arg2 arg3
```

上記の例では、echoコマンドが文字列"one two three"を出力し、xargsコマンドが出力された文字列をcommandと共に使用される引数として渡します。この場合、xargsは自動的に文字列をスペースで区切って複数の引数として解釈します。

引数をコマンドの最初の引数として渡す：

```{.shell}
$ echo "one two three" | xargs -I{} command {} arg1 arg2 arg3
```

この例では、-Iオプションを使用して、xargsが各入力行の文字列を置換する場所を指定します。上記の例では、{}が文字列に置き換えられます。次に、コマンドを指定し、最初の引数として文字列を渡します。

引数をコマンドの中間の引数として渡す：

```{.shell}
$ echo "one two three" | xargs -I{} command arg1 {} arg2 arg3
```

上記の例では、{}をcommandコマンドの引数のどこにでも置くことができます。この場合、arg1が最初の引数、arg2とarg3が最後の引数として渡され、{}は真ん中の引数として渡されます。

これらは、xargsコマンドを使用して引数を任意の場所に渡すための一般的な方法のいくつかです。ただし、実際には使用するコマンドによって、最適な引数の渡し方が異なる場合があります。

### パッケージ管理

#### apt update

**sudo apt update** コマンドは、Debian系Linuxディストリビューションで使用されるパッケージ管理ツール `apt` (Advanced Package Tool) のコマンドの一つです。このコマンドは、以下の2つの主要な作業を実行します。

1. リポジトリの更新

- `/etc/apt/sources.list` や `/etc/apt/sources.list.d/` ディレクトリに記載されているAPTリポジトリから、**最新のパッケージ情報**をダウンロードします。
- 具体的には、各リポジトリのパッケージリスト (Packages.gz) と、パッケージの詳細情報 (Release.gz) をダウンロードします。
- (<http://archive.ubuntu.com/ubuntu/dists/jammy/main/binary-amd64/Packages.gz>)
- ダウンロードした情報に基づいて、**利用可能なパッケージの一覧** と、**各パッケージの最新バージョン** を更新します。

1. パッケージリストの更新

- ダウンロードしたパッケージ情報に基づいて、`/var/lib/apt/lists/` ディレクトリ内の**パッケージリストを更新**します。
- (/var/lib/apt/lists/archive.ubuntu.com_ubuntu_dists_jammy_main_binary-amd64_Packages.lz4)
- このパッケージリストには、利用可能なすべてのパッケージ名、バージョン、依存関係、ダウンロードソースなどが含まれています。
- パッケージリストを更新することで、システムが**新しいパッケージ**や**既存パッケージの新しいバージョン**を認識できるようになります。

[補足]

- `sudo apt update` コマンドを実行する前に、**インターネット接続** が確立されていることを確認する必要があります。
- このコマンドは、**root権限** で実行する必要があります。そのため、通常は `sudo` コマンドを前に付けて実行します。
- オプションを指定することで、**特定のリポジトリのみを更新**したり、**ダウンロードの進行状況を表示**したりすることができます。
- `sudo apt update` コマンドは、**パッケージのインストール** や **アップグレード** を行う前に必ず実行する必要があります。
- 最新のパッケージ情報だけでなく、**セキュリティアップデート情報** もダウンロードされます。

[例]

```bash
sudo apt update
```

このコマンドを実行すると、`/etc/apt/sources.list` や `/etc/apt/sources.list.d/` ディレクトリに記載されているすべてのリポジトリが更新されます。

[詳細情報]

- APT リポジトリ: [無効な URL を削除しました]
- apt update マニュアル: [無効な URL を削除しました]

[参考情報]

- 【備忘録】apt-get updateって何やってるの？ #Linux - Qiita: [https://qiita.com/pensuke628/items/1555cad4904327117982](https://qiita.com/pensuke628/items/1555cad4904327117982)
- 第677回 aptで使うsources.listのオプションいろいろ | gihyo.jp: [https://gihyo.jp/admin/serial/01/ubuntu-recipe/0677](https://gihyo.jp/admin/serial/01/ubuntu-recipe/0677)
- APT の設定 (/etc/apt/sources.list) をちゃんと理解する - くじらにっき++: [https://kujira16.hateblo.jp/entry/2019/10/14/190008](https://kujira16.hateblo.jp/entry/2019/10/14/190008)

[注意事項]

- `/etc/apt/sources.list` を編集する前に、必ず**バックアップ**を取ってください。
- リポジトリを追加する場合は、**信頼できるソース**からのみ行ってください。
- 不明な点がある場合は、**システム管理者に相談**してください。

#### snap

snapコマンドは、LinuxシステムでSnapパッケージを管理するためのコマンドラインユーティリティです。SnapはCanonical社によって開発されたソフトウェアデプロイメントとパッケージ管理のシステムです。Snapを使うことで、アプリケーションとその依存関係を1つのパッケージ（Snapパッケージと呼ばれる）にまとめて配布、インストール、更新、削除することができます。

Snapパッケージは、多くのLinuxディストリビューションで利用でき、一般的に以下のような特徴を持っています：

依存関係の解決: Snapパッケージは、アプリケーションとその依存するライブラリやリソースを一緒に格納するため、依存関係の問題が少なくなります。

セキュリティ: Snapアプリケーションはサンドボックス化されているため、システム全体への影響が低減します。

自動更新: Snapパッケージは自動的に更新されることが多く、ユーザーが手動でアップデートする必要はありません。

一般的なsnapコマンドの使用例は以下の通りです：

ソフトウェアをインストールする： sudo snap install [package_name]
インストール済みのソフトウェアを一覧表示する： snap list
ソフトウェアをアンインストールする： sudo snap remove [package_name]
ソフトウェアを更新する： sudo snap refresh [package_name]
これらのコマンドによって、Linuxシステム上でソフトウェアのライフサイクルを簡単に管理できます。

### ユーザ管理

### テキスト処理

#### od

odコマンドは、Octal Dumpの略でファイルを8進数でダンプするコマンドです。
具体的には、od コマンドは、以下の用途で使用されます。
ファイルの内容を16進数または8進数で表示する
ファイルの特定の部分をバイナリデータとして表示する
ファイルのバイナリデータを編集する
ファイルの構造を分析する

```{.shell}
# echo "hello, World" | od
0000000 062550 066154 026157 053440 071157 062154 000012
0000015
```

オプション-tで16進数でダンプすることも可能です。  

```{.shell}
$ echo "hello, World" | od -t x1
0000000 68 65 6c 6c 6f 2c 20 57 6f 72 6c 64 0a
0000015
```

#### Sed

Sed is a command which can be replaced or deleted the characters.

```{.shell}
$ cat ./hoge.txt | sed -e 's/xxx/XXX/g' > .hoge-new.txt
```

#### tr

trコマンドは、TRanslateの略で文字列の変換、置換、削除を行うためのコマンドです。  
主な機能として以下があります。

- 特定の文字を別の文字に置き換える
- 不要な文字を削除する
- 連続する文字を１つにまとめる
- 大文字を小文字に変換する、またはその逆を行う。

基本的な使い方
tr [オプション] 変換対象文字列 変換後文字列

例

小文字のaをすべて大文字のAに変換する

```sh
tr a A ファイル名
```

### プロセス管理 / Process Management

#### pstree

プロセスツリーを表示する。
display a tree of processes.

```{.shell}
$ pstree
systemd─┬─ModemManager───2*[{ModemManager}]
        ├─NetworkManager───2*[{NetworkManager}]
        ├─3*[VBoxClient───VBoxClient───2*[{VBoxClient}]]
        ├─VBoxClient───VBoxClient───3*[{VBoxClient}]
        ├─VBoxService───8*[{VBoxService}]
        ├─accounts-daemon───2*[{accounts-daemon}]
        ├─acpid
        ├─apache2───2*[apache2───26*[{apache2}]]
        ├─avahi-daemon───avahi-daemon
        ├─colord───2*[{colord}]
        ├─cron
        ├─cups-browsed───2*[{cups-browsed}]
        ├─cupsd
        ├─dbus-daemon
        ├─gdm3─┬─gdm-session-wor─┬─gdm-x-session─┬─Xorg───{Xorg}
        │      │                 │               ├─gnome-session-b─┬─ssh-agent
        │      │                 │               │                 └─2*[{gnome-+
        │      │                 │               └─2*[{gdm-x-session}]
        │      │                 └─2*[{gdm-session-wor}]
        │      └─2*[{gdm3}]
        ~
```

#### awk

文字列を扱うのに非常に便利なプログラミング言語。  
テキストファイル、特に空白やタブ、カンマ等で区切られたファイルの処理を念頭に置いた仕様となっている。  
同様に文字列を処理できるsedが特殊な文法であるのに対して、awkはC言語ライクで人が分かりやすい文法になっている。

参考文献:
[初心者のためのawkコマンド](https://tech-blog.rakus.co.jp/entry/20210120/awk)

```data.txt
$ cat data.txt
1 a o
2 b p
3 c q
4 d r
5 e s
```

$0ですべての行と列を表示する。  

```{.shell}
$ awk '{print $0}' data.txt
1 a o
2 b p
3 c q
4 d r
5 e s
```

$1で１列目を表示する。  

```{.shell}
$ awk '{print $1}' data.txt
1
2
3
4
5
```

$2で2列目を表示する。  

```{.shell}
$ awk '{print $2}' data.txt
a
b
c
d
e
```

$1,$3で1列目と3列目を表示する。

```{.shell}
$ awk '{print $1 $3}' data.txt
1o
2p
3q
4r
5s
```

パイプで入力することも可能。  

```{.shell}
$ echo 'a b c d' | awk '{print $1}'
a
```

正規表現を用いた文字列処理。

```{.shell}
# 書式: 
awk '/正規表現/ {アクション}' [入力ファイルのパス]
```

```{.shell}
$ awk '/3/ { print $2 }' data.txt
c
```

#### ps

ps aux:
  a: すべてのプロセスを表示する
  u: ユーザを表示する
  x: 制御端末の無いプロセスを表示する
>>>>>>> 64f859549148040f996750ccc8e83b44ddef6f10

```{.shell}
$ ps aux | head -n 5
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.1 169520 11480 ?        Ss   Feb23   0:03 /sbin/init splash
root           2  0.0  0.0      0     0 ?        S    Feb23   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   Feb23   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   Feb23   0:00 [rcu_par_gp]
~
develop    15321  0.0  0.0  12004  5220 pts/4    Ss   Feb25   0:00 bash
root       15351  0.0  0.0  13052  4692 pts/4    S+   Feb25   0:00 sudo tcpdump 
tcpdump    15352  0.0  0.0  12960  8056 pts/4    S+   Feb25   0:02 tcpdump -tn -
~
```

yoctoプロジェクトでpsコマンドを実行した結果:
Result of executing ps command in yocto project:

```{.shell}
# ps | head -n 5
  PID USER       VSZ STAT COMMAND
    1 root      2288 S    init [5]
    2 root         0 SW   [kthreadd]
    3 root         0 IW<  [rcu_gp]
    4 root         0 IW<  [rcu_par_gp]
root@qemux86-64:/usr/bin# 
```

### システム管理 / System Management

#### su

別のユーザになるコマンド。「su」は「substitute user」の略で、root以外のユーザーになることも可能。ただし、そのためにはroot権限が必要なので、suコマンドでいったんrootユーザーになり、「su ユーザー名」で他のユーザーになる、という手順が必要。
ログインしたのと同じように設定ファイルなどを読み込みたい場合は、「su -」「su - ユーザー名」のように「-」を付けて実行する。

#### lsb_release

OSのバージョン等のOSに関する情報を表示する。

```{.shell}
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.5 LTS
Release:        18.04
Codename:       bionic
```

#### systemctl

systemctl list-units --type=service --all --no-pager コマンドを分解して、各部分の意味を説明します。

systemctl: systemctl は、systemd システムとサービスマネージャーの主要なコントロールツールです。システムのサービスやその他のリソースの状態の確認、開始、停止、再起動などの操作を行う際に使用します。

list-units: このサブコマンドは、systemd が管理する "units"（サービス、ソケット、デバイスなどのリソース）のリストを表示するためのものです。

--type=service: このオプションを使用すると、特定のタイプのユニットのみを表示します。この場合、service と指定されているので、サービスユニットのみが表示されます。

--all: 通常、list-units はアクティブなユニットのみを表示します。しかし、--all オプションを使用することで、アクティブでないユニットも含めて全てのユニットを表示します。

--no-pager: 通常、長い出力結果はページャー（例：less や more）を通じて表示され、ユーザーはページごとに内容を確認できます。--no-pager オプションを使用すると、ページャーをバイパスして結果を直接コンソールに出力します。これは大量の情報を一度にスクロールせずに確認したい場合や、スクリプト内でこのコマンドを使用する場合などに便利です。

要約すると、systemctl list-units --type=service --all --no-pager コマンドは、「systemd が管理する全てのサービスユニット（アクティブなものも非アクティブなものも）を、ページャーを使用せずに一覧表示する」という操作を行います。

#### systemd

systemdは、Linuxオペレーティングシステムのための初期化システムとシステム管理デーモンです。これは、システム起動時のタスクを実行したり、後で必要とされるサービスを起動・監視する役割を果たします。systemdは、多くの現代のLinuxディストリビューションでSysV initやUpstartの代わりとして採用されています。

systemdの主な特徴と利点は以下の通りです：

ユニット: systemdは「ユニット」という概念を持っています。これはサービス、ソケット、デバイス、マウントポイントなど、様々なリソースを抽象化したものです。これにより、異なるリソースを同じ構文やセマンティクスで管理することができます。

並列処理: systemdは、起動プロセスを効率的に並列化して実行します。これにより、システムの起動時間が短縮されることが多いです。

依存関係の管理: ユニット間の依存関係を明確に指定できるため、必要なサービスやリソースが適切な順序で起動・停止されます。

統合的なログシステム: systemdはjournaldというログシステムを持っています。これにより、システム全体のログを一元的に管理することができます。

Cgroupsとの統合: systemdはLinuxのcgroupsと統合しており、サービスのリソースの利用を制限したり、監視することができます。

状態の追跡: systemdはサービスの状態（実行中、停止中、エラーなど）を追跡し、それに基づいて他のタスクやサービスの動作を決定します。

以上のように、systemdはLinuxシステムの初期化とサービスの管理を効率的に行うための強力なツールセットを提供します。一部のユーザーや開発者からは、その設計や機能の包括的な性質について批判も受けていますが、多くの主要なLinuxディストリビューションで標準として採用されているのは事実です。

### ユーティリティ / Utility

### デバイス / Device

### ネットワーク / Network

#### netstat

通信状況やルーティングテーブルを表示する。

書式: netstat [オプション]
オプション:
-r, --route: ルーティングテーブル情報を表示する。

実行例:

```{.shell}
$ netstat -r
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
default         _gateway        0.0.0.0         UG        0 0          0 enp0s3
link-local      0.0.0.0         255.255.0.0     U         0 0          0 enp0s3
192.168.0.0     0.0.0.0         255.255.255.0   U         0 0          0 enp0s3
```

見方: [ルーティングテーブルの状態の表示](https://docs.oracle.com/cd/E19620-01/805-5857/troubleshoot6-19973/index.html)

Destination: 宛先のネットワーク
Gateway: パケットを転送するルータ
Genmask: サブネットマスク
Flags:
  U: 送信経路がup状態
  G: 送信経路がゲートウェアへのもの
  H: 完全指定のホストアドレス
MSS Window:
irtt: ?
Iface: 送信経路で使用されているネットワークインターフェス

### セキュリティ / Security

### データベース / Database

### 仮想化

### カーネル

### 印刷

### その他

#### man

Linuxにおいて、コマンドが標準入力を受け取るかどうかは、そのコマンドのマニュアルページに記載されています。マニュアルページには、コマンドの詳細な使い方やオプションについて記述されています。

コマンドのマニュアルページを表示するには、ターミナルで man コマンドを使用します。例えば、cat コマンドのマニュアルページを表示する場合、以下のように入力します。

```{.shell}
man cat
```

マニュアルページが表示されたら、ページをスクロールして "DESCRIPTION" セクションを探し、コマンドが標準入力を受け取るかどうかを確認することができます。標準入力を受け取る場合、マニュアルページには通常、どのように標準入力を処理するかについての説明が含まれています。

catでは以下の通り、DESCIPTIONとEXAMPLESに標準入力に関して記載があります。

- DESCRIPTION: With no FILE, or when FILE is -, read standard input.
- EXAMPLES: cat    Copy standard input to standard output.

```{.shell}
CAT(1)                                         User Commands                                         CAT(1)

NAME
       cat - concatenate files and print on the standard output

SYNOPSIS
       cat [OPTION]... [FILE]...

DESCRIPTION
       Concatenate FILE(s) to standard output.

       With no FILE, or when FILE is -, read standard input.

EXAMPLES
       cat f - g
              Output f's contents, then standard input, then g's contents.

       cat    Copy standard input to standard output.
```

#### hackbench

Hackbench 50 processes 1000 の詳細解説
Hackbench 50 processes 1000 コマンドは、Linuxシステムのパフォーマンスを評価するためのベンチマークツールである Hackbench を使用して、50個のプロセスを同時に1000回実行 することを意味します。

このコマンドを実行すると、以下のことが起こります。

Hackbench ツールが起動します。
50個のプロセス が同時に作成されます。
各プロセスは、指定されたタスクを実行します。
各プロセスは、1000回 タスクを実行します。
すべてのプロセスが完了すると、Hackbench ツールはベンチマーク結果を出力します。
ループ回数 1000 は、各プロセスが実行するタスクの回数を指します。つまり、このコマンドでは、各プロセスは 1000回 以下のタスクを実行します。

具体的なタスクの内容は、Hackbench の設定によって異なりますが、一般的には以下のいずれかです。

CPUベンチマーク: 浮点演算、整数演算、メモリアクセスなどの処理速度を測定します。
I/Oベンチマーク: ファイルの読み書き、ネットワーク通信などの速度を測定します。
システムコールベンチマーク: システムコールと呼ばれるOSの機能呼び出しにかかる時間を測定します。
Hackbench 50 processes 1000 コマンドを実行することで、以下の情報を取得することができます。

システム全体の処理能力: 50個のプロセスを同時に実行することで、システム全体の処理能力を評価することができます。
個々のプロセスの処理能力: 各プロセスの実行時間やCPU使用率を測定することで、個々のプロセスの処理能力を評価することができます。
ボトルネック: システム全体のボトルネックや個々のプロセスのボトルネックを特定することができます。
このコマンドは、以下の目的で使用されます。

システムの性能評価: システムの性能を評価し、問題点を特定するために使用されます。
システムのチューニング: システムのチューニングを行い、性能を向上させるために使用されます。
ハードウェアの比較: 異なるハードウェアの性能を比較するために使用されます。
注意事項

Hackbench 50 processes 1000 コマンドを実行すると、システムに大きな負荷がかかります。そのため、実行前にシステムの状態を確認し、十分な空きメモリとCPUリソースがあることを確認してください。
このコマンドは、root権限で実行する必要があります。
このコマンドを実行するには、Hackbench ツールがインストールされている必要があります。
参考資料

Hackbench 公式ドキュメント [無効な URL を削除しました]
Linux パフォーマンスベンチマーク [無効な URL を削除しました]
