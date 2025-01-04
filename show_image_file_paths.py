import os

def find_images(directory):
    """
    指定されたディレクトリ内の画像ファイルを再帰的に検索し、そのパスを表示します。

    Args:
        directory (str): 検索対象のディレクトリ。
    """
    # 一般的な画像ファイルの拡張子
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    
    # ディレクトリを再帰的に探索
    for root, _, files in os.walk(directory):
        for file in files:
            # 拡張子が画像ファイルに該当する場合
            if file.lower().endswith(image_extensions):
                # フルパスを表示
                print(os.path.join(root, file))


# 使用例
if __name__ == "__main__":
    # ユーザーからディレクトリパスを入力
    search_dir = "/media/hashimo/enjoy/torrent/Dr.スランプ アラレちゃん/[鳥山明] Dr.スランプ アラレちゃん 文庫版 第01巻/"
    
    # ディレクトリが存在するか確認
    if os.path.isdir(search_dir):
        print("画像ファイルを検索中...\n")
        find_images(search_dir)
    else:
        print("指定されたディレクトリが存在しません。")