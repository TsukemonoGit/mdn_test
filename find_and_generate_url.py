import os
import random
import json
import requests

# スクリプトが存在するディレクトリのパス
script_dir = os.path.dirname(os.path.abspath(__file__))
# 検索対象のフォルダへのパス
search_dir = os.path.join(script_dir, "content/files/en-us")

# index.mdファイルを再帰的に探索する関数
def search_index_md_files(directory):
    index_md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "index.md":
                index_md_files.append(os.path.join(root, file))
    return index_md_files


# ランダムに1つのindex.mdファイルを選択してURLを作成する関数
def generate_random_url(index_md_files):

    
    # index_filesからランダムに1つのindex.mdファイルを選択
    random_index_md_file = random.choice(index_md_files)
    
    # 選択したindex.mdファイルからslug情報を取得
    slug = get_slug_from_index_md(random_index_md_file)
    
    if slug:
        # URLを作成
        url_ja = f"https://developer.mozilla.org/ja/docs/{slug}"
        url_en = f"https://developer.mozilla.org/en-US/docs/{slug}"

        
        # URLをチェックして存在する方を返す
        if url_exists(url_ja):
            return url_ja
        elif url_exists(url_en):
            return url_en
        else:
            print("Both URLs are not available.")
            return None
    else:
        print("Slug information not found in the selected index.md file.")
        return None

# URLの存在をチェックする関数
def url_exists(url):
    response = requests.head(url)
    return response.status_code == 200

# index.mdファイルからslug情報を取得する関数
def get_slug_from_index_md(index_md_file):
 
    # index.md ファイルを読み込んで内容を取得
    with open(index_md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # slug 情報を適切に抽出する処理を実装
    # ここでは、例として正規表現を使用して抽出する例を示します
    import re
    # 正規表現パターンを定義（例: "slug: 任意の文字列"）  match = re.search(r'slug:\s*(.*)', file_response.text)
    pattern = r"slug:\s*(.*)"
    # 正規表現でマッチング
    match = re.search(pattern, content)
    if match:
        # マッチした部分を取得して slug として返す
        slug = match.group(1).strip()
        return slug
    else:
        print("Slug information not found in the selected index.md file.")
        return None

# メイン処理
def main():
        # index.mdファイルを再帰的に探索
    index_md_files = search_index_md_files(search_dir)
    # ランダムにURLを生成
    random_url = generate_random_url(index_md_files)
    if random_url:
        print(random_url)

if __name__ == "__main__":
    main()
