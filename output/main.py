import os
from PIL import Image
import pyheif

input_folder = './input'  # 入力.HEIC画像のディレクトリ
output_folder = './output'  # 出力.JPG画像のディレクトリ

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.heic'):
        heif_file = pyheif.read(os.path.join(input_folder, filename))
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')
        image.save(output_path, "JPEG", quality=70)

print("変換完了")