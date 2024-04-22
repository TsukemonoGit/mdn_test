import os
import random
import json
import requests

# 保存先ディレクトリ
save_dir = "./data"
# 保存したindex_files.jsonのパス
index_files_path = os.path.join(save_dir, "index_files.json")

# ランダムに1つのindex.mdファイルを選択してURLを作成する関数
def generate_random_url(index_files_path):
    # index_files.jsonを読み込む
    with open(index_files_path, 'r') as f:
        index_files = json.load(f)
    
    # index_filesからランダムに1つのindex.mdファイルを選択
    random_index_md_file = random.choice(index_files)
    
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
    # ランダムにURLを生成
    random_url = generate_random_url(index_files_path)
    if random_url:
        print(random_url)

if __name__ == "__main__":
    main()
