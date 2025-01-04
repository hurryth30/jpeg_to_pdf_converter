import jpeg_to_pdf_for_one_title as jtop

if __name__ == '__main__':
    # すべてのタイトルのフォルダのベースディレクトリ
    base_directory_path = '/media/hashimo/enjoy/torrent/未処理/'
    # 各タイトルのフォルダのパスを取得
    subdirectories = jtop.get_subdirectories(base_directory_path)
    # 各タイトルのフォルダで処理を行う
    for subdir in subdirectories:
        print(f"処理を開始: {subdir}")
        jtop.convert(subdir)
