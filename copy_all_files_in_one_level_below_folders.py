import os
from PIL import Image
from fpdf import FPDF

def images_to_pdf(img_paths, output_pdf):
    pdf = FPDF()

    for img_path in img_paths:
        img = Image.open(img_path)
        img_width, img_height = img.size
        # PDFページを追加 (単位: mm)
        pdf.add_page(orientation='P', format=[img_width * 1.264583, img_height * 0.264583])
        pdf.image(img_path, x=1, y=0, w=img_width * 0.264583, h=img_height * 0.264583)

    pdf.output(output_pdf)

# 現在のディレクトリを取得
current_dir = os.getcwd()
tmp_dir = os.path.join(current_dir, 'tmp')

# tmpフォルダが存在しない場合は作成
if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir)

# 2階層下のディレクトリを走査
for entry in os.listdir(current_dir):
    entry_path = os.path.join(current_dir, entry)
    if os.path.isdir(entry_path):
        all_images = []
        for root, dirs, files in os.walk(entry_path):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    all_images.append(os.path.join(root, file))
        
        # 画像が見つかった場合、PDFを作成
        if all_images:
            pdf_name = os.path.basename(entry_path) + '.pdf'
            output_pdf_path = os.path.join(tmp_dir, pdf_name)
            images_to_pdf(all_images, output_pdf_path)
            print(f"PDF saved at: {output_pdf_path}")
        else:
            print(f"No images found in directory: {entry_path}")