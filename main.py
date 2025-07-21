import json
import os

from PIL import Image


def main():
    # Jsonファイルを読み込む
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    input_folder_path = config.get('input_folder')
    output_folder_path = config.get('output_folder')

    # Jsonファイルのinput_folderから画像ファイルを取得する
    if not os.path.exists(input_folder_path):
        print(f"Input folder does not exist: {input_folder_path}")
        return  # 入力フォルダが存在しない場合は終了

    # 入力フォルダ内の画像ファイル（PNG, JPG, JPEG）をリストアップ
    image_files = []
    for filename in os.listdir(input_folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_files.append(filename)

    # 入力フォルダに画像ファイルがない場合は終了
    if not image_files:
        print(f"No image files found in the input folder: {input_folder_path}")
        return  # 入力フォルダに画像ファイルがない場合は終了

    # 出力フォルダが存在しない場合は実行しているディレクトリに出力フォルダを作成する
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
        print(f"Output folder created: {output_folder_path}")

    # 画像ファイルをWebP形式に変換する
    try:
        for image_file in image_files:
            input_image_file_path = os.path.join(input_folder_path, image_file)
            output_image_file_path = os.path.join(
                output_folder_path,
                f"{os.path.splitext(image_file)[0]}.webp"
            )

            # 画像を開いてWebP形式で保存
            with Image.open(input_image_file_path) as img:
                img.save(output_image_file_path, format='webp')
                print(
                    f"Converted {image_file} to WebP format and saved to "
                    f"{output_image_file_path}"
                )
    except Exception as e:
        print(f"An error occurred while converting images: {e}")
        # 変換中にエラーが発生した場合は終了
        return
    print("Image conversion completed successfully.")


if __name__ == "__main__":
    main()
