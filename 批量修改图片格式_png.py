from PIL import Image
import os
from pillow_heif import register_heif_opener
register_heif_opener()


def convert_images_to_png(input_folder, output_folder):
    # 检查输出文件夹是否存在，不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的文件
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        # 仅处理图片文件
        if filename.lower().endswith(('.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp','.heic')):
            # 打开图像并转换为PNG
            with Image.open(file_path) as img:
                # 去掉文件扩展名
                base_filename = os.path.splitext(filename)[0]
                output_path = os.path.join(output_folder, base_filename + '.png')
                
                # 保存为PNG格式
                img.save(output_path, 'PNG')
                print(f'已转换: {filename} -> {output_path}')

# 设置输入和输出文件夹路径
input_folder = 'file_path'
output_folder = 'file_path'

# 执行转换
convert_images_to_png(input_folder, output_folder)
