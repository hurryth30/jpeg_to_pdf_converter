import os


# ファイル名、フォルダ名の一括変更スクリプト
#  再帰処理で実行される


def rename_items(base_path):
    # 変更したい文字列のリスト
    targets = ['Manga-Zip.info_', '13DL.ME_', '13DL.me_', 'DLRAW.TO-', 'DLRAW.NET-', '(Digital SD) (KG Manga)','[aKraa]', '別スキャン', '電子書籍', '(一般コミック)']
    # 指定された文字列を新しい文字列に置き換える

    def replace_target(name):
        for target in targets:
            if target in name:
                return name.replace(target, '')
        return name

    for root, dirs, files in os.walk(base_path, topdown=False):
        # フォルダ名の変更
        for dir_name in dirs:
            new_dir_name = replace_target(dir_name)
            if new_dir_name != dir_name:  # 名前が変更される場合
                old_dir_path = os.path.join(root, dir_name)
                new_dir_path = os.path.join(root, new_dir_name)
                os.rename(old_dir_path, new_dir_path)
                print(f"フォルダ名を変更しました: {old_dir_path} -> {new_dir_path}")

        # ファイル名の変更
        for file_name in files:
            new_file_name = replace_target(file_name)
            if new_file_name != file_name:  # 名前が変更される場合
                old_file_path = os.path.join(root, file_name)
                new_file_path = os.path.join(root, new_file_name)
                os.rename(old_file_path, new_file_path)
                print(f"ファイル名を変更しました: {old_file_path} -> {new_file_path}")


if __name__ == "__main__":
    # base_directory = input("処理を行うディレクトリのパスを入力してください: ")
    base_directory = '/media/hashimo/enjoy/torrent/'
    rename_items(base_directory)