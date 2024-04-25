https://nostter.app/npub1fuffhzfv7xdrm5htde4mp9e5n6ywn763cq6mzxtetyqvsg66kkasp9zzyz


https://developer.mozilla.org/ja/docs/Web のサイトからランダムのページを一定時間間隔でNostrにポスト

https://github.com/mdn/content をサブモジュールにして、

- generate_url.yml
  
  でfind_and_generate_url.pyを実行して
  フォルダの中のindex.mdを探して
  その中からランダムに一つ選んで、
  index.mdの中身からサイトのタイトルとURLを出して、
  ポスト
  最初からいっこだけランダムなフォルダに探しに行ったほうがよいかも？

- update_submodule.yml
  
  サブモジュールのアップデートチェック
