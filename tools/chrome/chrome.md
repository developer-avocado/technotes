# Goolge Chrome Manual

## Build Environment

1. Access Google download page.

   - [Google Chrome Linux](https://www.google.com/chrome/?platform=linux)

2. Click [Download Chrome].

3. Select [64 bit .deb (For Debian/Ubuntu)] and click [Accept and Install].

4. Execute the downloaded file to install the Chrome.

   ```bash
   sudo sh -c 'ls | grep chrome | xargs -I{} dpkg -i {}'
   ```

## Extensions

- [Vimium](https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb)
- [Awesomescreenshot](https://chrome.google.com/webstore/detail/awesome-screenshot-and-sc/nlipoenfbbikpbjkfpfillcgkoblgpmj)
- [DeepL Translate](https://chrome.google.com/webstore/detail/deepl-translate-beta-vers/cofdbpoegempjloogbagkncekinflcnj)
- [Google Translate](https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb)
- [Weblio extension](https://chrome.google.com/webstore/detail/weblio-%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%86%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%B3/pgnfefoljgaelbckgfbijijhblgophjo)
- [Weblio English/Japanese](https://chrome.google.com/webstore/detail/weblio%E3%83%9D%E3%83%83%E3%83%97%E3%82%A2%E3%83%83%E3%83%97%E8%8B%B1%E5%92%8C%E8%BE%9E%E5%85%B8/oingodpdjohhkelnginmkagmkbplgema)
- [Markdown Viewer](https://chrome.google.com/webstore/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk)
- [Charset](https://chrome.google.com/webstore/detail/charset/oenllhgkiiljibhfagbfogdbchhdchml)

# Settings

## Search Engine

1. Open Chrome.
2. Type chrome://settings/searchEngines in the address bar and press Enter.
3. Click [Add] in Site search and type the following item in the input box.

| Name     | Shortcut  | URL
| -------- | --------- | ---------
| Google   | gj        | -
| Google English   | ge | <https://www.google.com/?gl=us&hl=en&gws=cr&pws=0>
| Google翻訳 | gt       | <https://translate.google.com/?source=osdd#auto%7Cauto%7C%25s>
| DeepL    | dl        | <https://www.deepl.com/ja/translator#en/ja/%s>
| Google Lens | gl | <https://lens.google.com/search?p=>
| Bookmark | bm | -

## Languages

1. Open Chrome.
2. Type chrome://settings/languages in the address bar and press Enter.
3. Click [Add languages].
4. Select preffered language at [Preferred languages] and click [Add].
5. Click [Three dot leader] at selected prefferd language and [Display Google Chrome in this language].