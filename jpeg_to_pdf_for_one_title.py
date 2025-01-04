import os
from fpdf import FPDF


def find_image_files(directory):
    """
    指定されたディレクトリ内の画像ファイルを再帰的に検索し、そのパスをリストで返します。

    Args:
        directory (str): 検索対象のディレクトリ。
    """
    # 一般的な画像ファイルの拡張子
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    # 画像ファイルのパスを格納するリスト
    image_file_paths = []
    # ディレクトリを再帰的に探索
    for root, _, files in os.walk(directory):
        for file in files:
            # 拡張子が画像ファイルに該当する場合
            if file.lower().endswith(image_extensions):
                # フルパスを表示
                file_path = os.path.join(root, file)
                image_file_paths.append(file_path)
    # 日本語をソートしてページ順を正す
    image_file_paths.sort()
    return image_file_paths


def create_pdf_from_images(image_paths, output_pdf_path):
    """画像ファイルをまとめて1つのPDFを作成"""
    pdf = FPDF()

    for image_path in image_paths:
        # 画像のサイズを取得
        pdf.add_page()
        try:
            pdf.image(image_path, x=10, y=10, w=pdf.w - 20)  # wを指定して画像を幅いっぱいに表示
        except Exception as e: 
            # 画像が読み込めないとき
            print(f"画像の読み込みに失敗しました: {image_path}")
            continue
    # PDFを保存
    pdf.output(output_pdf_path)


def jpeg_to_pdf_for_one_dir(target_directory_path, output_path):
    """指定されたディレクトリ内の画像ファイルをPDFにまとめる"""
    # pdf名を取得
    pdf_name = os.path.basename(target_directory_path)
    # PDFファイルのパス
    pdf_path = os.path.join(output_path, f"{pdf_name}.pdf")
    # 画像ファイルのパスを取得
    image_files = find_image_files(target_directory_path)

    # 画像が見つかった場合、PDFを作成
    if image_files:
        create_pdf_from_images(image_files, pdf_path)
        print(f"PDFファイル '{pdf_path}' が作成されました。")
    else:
        print("画像ファイルは見つかりませんでした。")


def get_subdirectories(path):
    """指定されたパスの1階層下にあるサブディレクトリのパスを取得"""
    subdirectories = []
    # 現在のディレクトリの1階層下を取得
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):  # フォルダかどうかを確認
            subdirectories.append(full_path)
    return subdirectories


def convert(target_directory_path):
    # 出力先のフォルダのパス
    pdf_folder_path = os.path.join(target_directory_path, 'pdf')
    # フォルダが存在しない場合は作成
    if not os.path.exists(pdf_folder_path):
        os.makedirs(pdf_folder_path)
    # 1階層下のフォルダのパスを取得
    subdir_paths = get_subdirectories(target_directory_path)
    # 各サブディレクトリで処理を行う
    for subdir_path in subdir_paths:
        jpeg_to_pdf_for_one_dir(subdir_path, pdf_folder_path)


if __name__ == "__main__":
    # 現在の作業ディレクトリのパスを取得
    # current_directory = os.getcwd()
    current_directory = "/media/hashimo/enjoy/torrent/HUNTER×HUNTER/"
    # 全ての画像ファイルを１つのPDFへ変換
    convert(current_directory)
