import os
import subprocess

def remove_pixelation(input_image_path, search_image_path, output_image_path):
    # 检查输入文件是否存在
    if not os.path.exists(input_image_path):
        raise FileNotFoundError(f"Input image file {input_image_path} does not exist.")

    # 检查搜索图像文件是否存在
    if not os.path.exists(search_image_path):
        raise FileNotFoundError(f"Search image file {search_image_path} does not exist.")

    # 构建命令
    command = [
        "python", "depix.py",
        "-p", input_image_path,
        "-s", search_image_path,
        "-o", output_image_path,
        "--backgroundcolor", "255,255,255",  # 白色背景
        "--averagetype", "linear"            # 使用 linear 类型
    ]

    # 运行命令
    try:
        subprocess.run(command, check=True)
        print(f"Output saved to {output_image_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Depix: {e}")

if __name__ == "__main__":
    # 输入图像路径
    input_image_path = "try.png"

    # 搜索图像路径
    search_image_path = "images/searchimages/debruinseq_notepad_Windows10_closeAndSpaced.png"

    # 输出图像路径
    output_image_path = "out.png"

    # 移除马赛克
    remove_pixelation(input_image_path, search_image_path, output_image_path)