import os
from fpdf import FPDF
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def images_to_pdf(images, output_pdf_path):
    pdf = FPDF()
    
    for image_path in images:
        try:
            img = Image.open(image_path)
            pdf.add_page()
            pdf.image(image_path, x=10, y=10, w=pdf.w - 20)  # w-20でサイドマージンを考慮
        except Exception as e:
            print(f"Error adding image {image_path}: {e}")
    
    pdf.output(output_pdf_path)

def gather_images_from_directory(directory):
    images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  # 対応する画像形式
                images.append(os.path.join(root, file))
    return images

def process_directory(base_directory):
    tmp_directory = os.path.join(base_directory, "tmp")
    os.makedirs(tmp_directory, exist_ok=True)
    
    # 1階層下の各サブディレクトリを対象にする
    for subdir in os.listdir(base_directory):
        subdir_path = os.path.join(base_directory, subdir)
        if os.path.isdir(subdir_path):
            images = gather_images_from_directory(subdir_path)
            if images:
                output_pdf_path = os.path.join(tmp_directory, f"{subdir}.pdf")
                images_to_pdf(images, output_pdf_path)
                print(f"Created PDF: {output_pdf_path}")

def choose_directory():
    root = tk.Tk()
    root.withdraw()  # Tkinterのメインウィンドウを隠す
    directory = filedialog.askdirectory(title="対象のディレクトリを選択")
    if directory:
        process_directory(directory)
    else:
        print("ディレクトリが選択されませんでした。")

if __name__ == "__main__":
    choose_directory()