import pathlib
import pillow_heif
from PIL import Image

def heic_to_jpg(image_path, save_path):
    """
    pillow_heif を利用して HEIC 画像を読み込み、JPEG 形式で保存する関数
    """
    # pillow_heif.read_heif はリストで返すので、[0]で最初の画像を取得
    heif_file = pillow_heif.read_heif(image_path)[0]
    # PIL.Image.frombytes() で画像オブジェクトに変換
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    # JPEG に変換して保存（必要に応じ quality パラメータも調整可）
    image.save(save_path, "JPEG", quality=70)

def main():
    # 入力フォルダと出力フォルダのパスを指定（必要に応じ適宜変更してください）
    input_folder = pathlib.Path('./input')
    output_folder = pathlib.Path('./output')
    
    # 出力フォルダが存在しない場合は作成
    if not output_folder.exists():
        output_folder.mkdir(parents=True, exist_ok=True)

    # 入力フォルダ内のすべての .HEIC ファイルを再帰的に取得
    heic_files = list(input_folder.glob('**/*.HEIC'))
    
    if not heic_files:
        print("変換対象の HEIC ファイルが見つかりませんでした。")
        return

    for heic_file in heic_files:
        # 各ファイルのパス（文字列化）
        image_path = str(heic_file)
        # 出力先のパス：出力フォルダ直下に、元ファイル名.jpg として保存
        save_path = str(output_folder / (heic_file.stem + '.jpg'))
        try:
            heic_to_jpg(image_path, save_path)
            print(f"{image_path} の変換が完了しました。")
        except Exception as e:
            print(f"{image_path} の変換中にエラーが発生しました: {e}")
    
    print("全ての変換が完了しました。")

if __name__ == '__main__':
    main()
