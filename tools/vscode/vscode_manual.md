# Visual Studio Code

**Table Of Contents**

- [Visual Studio Code](#visual-studio-code)
  - [インストール方法](#インストール方法)
  - [起動方法](#起動方法)
  - [画面構成](#画面構成)
  - [設定](#設定)
    - [設定ファイルの変更方法(JSON)](#設定ファイルの変更方法json)
    - [クリップボードの有効化](#クリップボードの有効化)
    - [\[Git Code Lens\]の無効化](#git-code-lensの無効化)
    - [Markdownのlintを無効にする](#markdownのlintを無効にする)
    - [Markdownのコードブロック中の$記号を有効にする](#markdownのコードブロック中の記号を有効にする)
    - [設定ファイルの変更方法(UI)](#設定ファイルの変更方法ui)
  - [検索 / find](#検索--find)
    - [検索例](#検索例)
    - [参考](#参考)
  - [ショートカット / Shortcut](#ショートカット--shortcut)
    - [ショートカット登録方法](#ショートカット登録方法)
    - [編集系](#編集系)
      - [検索系](#検索系)
    - [選択系](#選択系)
    - [表示系](#表示系)
    - [移動系](#移動系)
    - [設定系](#設定系)
  - [Markdown記法](#markdown記法)
  - [機能拡張 / Extension](#機能拡張--extension)
    - [共通 / Common](#共通--common)
    - [Git](#git)
    - [Programming](#programming)
    - [UML](#uml)
    - [ファイル形式変換](#ファイル形式変換)
    - [参考](#参考-1)

## インストール方法

1. [Download Visual Studio Code](https://code.visualstudio.com/Download)にアクセスする  

2. [.dev]をクリックし、パッケージをダウンロードする。  
   ダウンロード先は、HOMEのDownloadディレクトリとする。  

3. Downladディレクトリに移動し、パッケージをインストールする。  

   ```bash
   cd ~/Downloads  
  
   sudo dpkg -i code_1.74.3-1673284829_amd64.deb
   ```

## 起動方法

1. ターミナルを起動し、codeを実行する。  

## 画面構成

![画面構成](./images/2020-08-22-15-29-08.png)

- [User Interface](https://code.visualstudio.com/docs/getstarted/userinterface)
- [Visual Studio Codeの使い方、基本の「キ」 (2/6)](https://www.atmarkit.co.jp/ait/articles/1507/10/news028_2.html)

## 設定

### 設定ファイルの変更方法(JSON)

1. Vscode上で[Ctrl + Shift + P]を入力し、コマンドパレットを開く。  
   
1. コマンドパレットに[setting]と入力し、表示される[Preferences: Open User Settings(JSON)]を実行する。  

または、[settings.json](C:\Users\<your-account>\AppData\Roaming\Code\User\settings.json)を参照。

### クリップボードの有効化

vimでクリップボードが使用できるようにする設定は以下の通り。

1. Vscode上で[Ctrl + Shift + P]を入力し、コマンドパレットを開く。  
2. [Settings]の上部の検索ボックスで「clipboard」と入力する。
3. [vim.useSystemClipboard]を「true」に変更する。  

   ```{.shell}
   "vim.useSystemClipboard": false
   ```

### [Git Code Lens]の無効化

[参考例](https://atmarkit.itmedia.co.jp/ait/articles/2111/19/news034.html)

### Markdownのlintを無効にする

settings.jsonに以下を追加する。  

```bash
    "markdownlint.config": {
        "MD024": false,
    },
```

### Markdownのコードブロック中の$記号を有効にする

settings.jsonに以下を追加する。  

```bash
    "markdownlint.config": {
        "MD014": false
    },
```

### 設定ファイルの変更方法(UI)

1. Vscode上で[Ctrl + Shift + P]を入力し、コマンドパレットを開く。  
   
1. コマンドパレットに[setting]と入力し、表示される[Preferences: Open User Settings(UI)]を実行する。  

   ![](./images/2023-07-02-08-09-33.png)

1. 設定変更したい機能を検索欄に入力し、その機能項目をクリックする。  
   ![](./images/2023-07-02-08-11-38.png)

1. 機能項目の設定を行う。  
   ![](./images/2023-07-02-08-15-37.png)

## 検索 / find

### 検索例

- 指定ファイルのみで用語を検索  

| Box              | Search Example       |
| ---------------- | -------------------- |
| Search Box       | programming          |
| files to include | {**/*.md},{**/*.txt} |
| files to exclude |                      |

- ワークスペースの最上位のフォルダ下で用語を検索  

| Box              | Search Example |
| ---------------- | -------------- |
| Search Box       | programming    |
| files to include | ./example      |
| files to exclude |                |

- 指定フォルダ下の指定ファイルのみで用語を検索  

| Box              | Search Example        |
| ---------------- | --------------------- |
| Search Box       | programming           |
| files to include | {vscode/example/*.md} |
| files to exclude |                       |

### 参考

- [search-across-files](https://code.visualstudio.com/docs/editor/codebasics#_search-across-files)

## ショートカット / Shortcut

### ショートカット登録方法

1. Vscode上で[Ctrl + Shift + P]を入力し、コマンドパレットを開く。  

2. コマンドパレットに[shortcut]と入力し、表示される[Preferences: Open Keyboard Shortcuts]を選択し、[Enter]キーを押す。  
  ![](./images/2023-07-02-07-43-23.png)

3. 変更したいコマンドを検索欄に入力する。  
  ![](./images/2023-07-02-07-49-46.png)

1. [Change Keybinding]をクリックすeる。
   ![](./images/2023-07-02-07-52-52.png)

2. 任意のキーの組み合わせを入力し、[Enter]キーを押す。  
  ![](./images/2023-07-02-07-46-49.png)


### 編集系

#### 検索系

| ショートカットキー | 機能                             |
| ------------------ | -------------------------------- |
| Ctrl + F           | ファイル内で文字列を検索する。   |
| Ctrl + H           | ファイル内で文字列を置換する。   |
| Ctrl + Shift + F   | 複数ファイルで文字列を検索する。 |
| Ctrl + Shift + H   | 複数ファイルで文字列を置換する。 |
| Ctrl + p, @   | アウトラインの項目を検索する。 |

### 選択系

### 表示系

| ショートカットキー | 機能                             |
| ------------------ | -------------------------------- |
| Ctrl + k Ctrl + 0  | すべてのインデントを折りたたむ。 |
| Ctrl + k Ctrl + j  | すべてのインデントを展開する。   |
| Ctrl + k v         | プレビューを開く。               |

### 移動系

| ショートカットキー                        | 機能                   |
| ----------------------------------------- | ---------------------- |
| Ctrl + 数字                               | ペインを切り替える。   |
| Alt + 数字                                | ファイルを切り替える。 |
| Ctrl + Shift + \|　波括弧{}間を移動する。 |
| Ctrl + Shift + E| エクスプローラにフォーカスを移動する |

### 設定系

| ショートカットキー | 機能             |
| ------------------ | ---------------- |
| Ctrl + ,           | 設定画面を開く。 |

## Markdown記法

アンカーの作成方法

[Jump](#DEST1)

<p id="DEST1">Here</p>

## 機能拡張 / Extension

### 共通 / Common

1. [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)  
Markdownに関する多くの機能を使用することができる。  
機能の一覧を以下に示す。  

- キーボードショートカット（太字、イタリック、チェック）
- 数式の入力

1. [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)  
アイコンの表示によって、ファイルの種別を確認しやすくなる。

1. [Output Colorizer](https://marketplace.visualstudio.com/items?itemName=IBM.output-colorizer)  
出力結果を装飾により見やすくすることができる。

1. [Paste Image](https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image)  
Markdownのファイルに「Ctrl + Alt + V」で画像をペーストすることができる。  

1. [Partial Diff](https://marketplace.visualstudio.com/items?itemName=ryu1kn.partial-diff)  
ファイル内で選択した部分の差分を比較することができる。

1. [Markdown Table Prettifier](https://marketplace.visualstudio.com/items?itemName=darkriszty.markdown-table-prettify)  
Markdown形式で記述された表を整形することができる。  
Markdown All in Oneにも同様の機能が備わっている。多少フォーマット整形の仕方が異なるので、自身に最適なものをインストールするのがよい。 

1. [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense)  
パスの入力補完機能でパスを素早く入力することができる。

1. [Path Autocomplete](https://marketplace.visualstudio.com/items?itemName=ionutvmi.path-autocomplete)  
パスの入力補完機能でパスを素早く入力することができる。

1. [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer)
対応する括弧が分かるように色付けすることができる。

1. [Bookmarks](https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks)

1. [Remote SSH](https://code.visualstudio.com/docs/remote/ssh)
ローカルPCからリモートPCのファイルを開くことができる。  

### Git

1. [Git Lens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

1. [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory)  
Gitのコミット履歴を確認することができる。

### Programming

1. [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)  
Pythonのリントやデバッグ機能を使用することができる。

1. [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

1. [Anaconda](https://marketplace.visualstudio.com/items?itemName=ms-python.anaconda-extension-pack)

1. [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)  
C/C++のリントやデバッグ機能を使用することができる。

### UML

1. [Plant UML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)  
UMLをmarkdownで記述することができる。

### ファイル形式変換

1. [vscode-pandoc](https://marketplace.visualstudio.com/items?itemName=DougFinke.vscode-pandoc)  
UMLをmarkdownで記述することができる。

### 参考

- [Extensions for the Visual Studio family of products](https://marketplace.visualstudio.com/vscode)

- [VSCodeのオススメ拡張機能 24 選 (とTipsをいくつか)](https://qiita.com/sensuikan1973/items/74cf5383c02dbcd82234)  

- [今日からはじめるVisual Studio Code設定](https://qiita.com/shimoju/items/e31e5f4092953297f486)
