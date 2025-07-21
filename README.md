# image-converter-webp-python

## 概要
このツールは画像ファイルをWebP形式に変換するPythonスクリプトです。
WebPは従来の画像フォーマットと比較して、高い圧縮率と画質を両立する最新の画像フォーマットです。
パッケージ管理ツールにuvを使用しています。

### 主な機能
- 複数の画像フォーマット（JPG、JPEG、PNG）からWebPへの変換
- 複数ファイルの一括変換

## 使用方法
1. 変換元画像ファイルを入れるディレクトリを作成します。
2. 1で作成したディレクトリに変換したい画像ファイルを入れます。
3. config.jsonのinput_folderに変換元の画像ファイルが入っているディレクトリパスを指定します。
4. config.jsonのout_folderに変換した画像ファイル出力先を指定します。
5. python main.pyを実行します。

## ライセンス
MITライセンス

---

## Overview
This tool is a Python script that converts image files to WebP format. WebP is a modern image format that provides superior compression and quality compared to traditional image formats.
The package management tool "uv" is used.

### Key Features
- Convert multiple image formats (JPG, JPEG, PNG) to WebP
- Batch conversion of multiple files

## Usage
1. Create a directory for the source image files.
2. Place the images you want to convert into the directory created in step 1.
3. Set the path of the source image directory to `input_folder` in config.json.
4. Set the output directory path for the converted images to `output_folder` in config.json.
5. Run `python main.py`.

## License
MIT