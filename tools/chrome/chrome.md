# Goolge Chrome Manual

## 環境構築

1. Googleダウンロードページにアクセスします。

   - [Google Chrome Linux](https://www.google.com/chrome/?platform=linux)

2. [Download Chrome]をクリックします。

3. [64 bit .deb (For Debian/Ubuntu)]を選択し、[Accept and Install]をクリックします。

4. ダウンロードしたファイルを実行します。

   ```bash
   sudo sh -c 'ls | grep chrome | xargs -I{} dpkg -i {}'
   ```

## 拡張機能

- [Vimium](https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb)
- [Awesomescreenshot](https://chrome.google.com/webstore/detail/awesome-screenshot-and-sc/nlipoenfbbikpbjkfpfillcgkoblgpmj)
- [DeepL Translate](https://chrome.google.com/webstore/detail/deepl-translate-beta-vers/cofdbpoegempjloogbagkncekinflcnj)
- [Google Translate](https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb)
- [Weblio extension](https://chrome.google.com/webstore/detail/weblio-%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%86%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%B3/pgnfefoljgaelbckgfbijijhblgophjo)
- [Weblio English/Japanese](https://chrome.google.com/webstore/detail/weblio%E3%83%9D%E3%83%83%E3%83%97%E3%82%A2%E3%83%83%E3%83%97%E8%8B%B1%E5%92%8C%E8%BE%9E%E5%85%B8/oingodpdjohhkelnginmkagmkbplgema)
- [Markdown Viewer](https://chrome.google.com/webstore/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk)
- [Charset](https://chrome.google.com/webstore/detail/charset/oenllhgkiiljibhfagbfogdbchhdchml)

# 設定

## 検索エンジン

1. Chromeを起動します。
2. アドレスバーに「chrome://settings/searchEngines」と入力し、Enterキーを押します。
3. 以下の通り、入力ボックスに入力します。

| Name     | Shortcut  | URL
| -------- | --------- | ---------
| Google   | gj        | -
| Google English   | ge | <https://www.google.com/?gl=us&hl=en&gws=cr&pws=0>
| Google翻訳 | gt       | <https://translate.google.com/?source=osdd#auto%7Cauto%7C%25s>
| DeepL    | dl        | <https://www.deepl.com/ja/translator#en/ja/%s>
| Google Lens | gl | <https://lens.google.com/search?p=>
| Bookmark | bm | -

## 優先言語

1. Chromeを起動します。
2. アドレスバーに「chrome://settings/languages」と入力し、Enterを押します。
3. [言語を追加]を押します。
4. 優先言語を選択し、[追加]をクリックします。
5. [Google Chromeをこの言語で表示]をクリックします。
