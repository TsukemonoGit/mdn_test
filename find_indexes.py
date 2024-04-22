import os
import random
import json

# 保存先ディレクトリ
save_dir="./data"
 # 検索対象のフォルダへのパス
search_dir = "./content/files/en-us"  
# ディレクトリが存在しない場合は作成する
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# index.mdファイルを再帰的に探索する関数
def search_index_md_files(directory):
    index_md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "index.md":
                index_md_files.append(os.path.join(root, file))
    return index_md_files

# ランダムに1つのindex.mdファイルを選択する
def select_random_index_md_file(index_md_files):
    return random.choice(index_md_files)

# index.mdファイルからslug情報を取得する関数
def get_slug_from_index_md(index_md_file):
    with open(index_md_file, 'r') as f:
        content = f.read()
        # ここでslug情報を適切に抽出する処理を実装してください
        # 例: slug = extract_slug(content)
        # extract_slug()は、index.mdファイルの内容からslug情報を抽出する自作の関数です
        # もしくは、正規表現などを使用して適切な方法でslug情報を取得します
        slug = "your_generated_slug"
    return slug

# index.mdファイルのリストを保存する関数
def save_index_md_files(index_md_files, save_path):
    with open(save_path, 'w') as f:
        json.dump(index_md_files, f)
        
# メイン処理
def main():
    # index.mdファイルを再帰的に探索
    index_md_files = search_index_md_files(search_dir)
    # index.mdファイルのリストを保存
    save_path = os.path.join(save_dir, "index_files.json")
    save_index_md_files(index_md_files, save_path)
    # if index_md_files:
    #     # ランダムに1つのindex.mdファイルを選択
    #     random_index_md_file = select_random_index_md_file(index_md_files)
        
    #     # 選択したindex.mdファイルからslug情報を取得
    #     slug = get_slug_from_index_md(random_index_md_file)
        
    #     if slug:
    #         # URLを作成
    #         full_url = f"https://example.com/{slug}"  # ここを適切なURLに変更してください
    #         print("Generated URL:", full_url)
    #     else:
    #         print("Slug information not found in the selected index.md file.")
    # else:
    #     print("No index.md files found in the specified directory.")

if __name__ == "__main__":
    main()