
https://developer.mozilla.org/ja/docs/Web のサイトからランダムのページを一定時間間隔でNostrにポスト

https://github.com/mdn/content をサブモジュールにして、

- generate_url.yml
  フォルダの中のindex.mdを探して
  その中からランダムに一つ選んで、
  index.mdの中身からサイトのタイトルとURLを出して、
  ポスト

- update_submodule.yml
  サブモジュールのアップデートチェック
