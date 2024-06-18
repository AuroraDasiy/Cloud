import pytesseract
from pdf2image import convert_from_path
import os
from PyPDF2 import PdfReader
from concurrent.futures import ThreadPoolExecutor

# 配置tesseract路径（仅适用于Windows）
                                            #选择你的ocr位置
pytesseract.pytesseract.tesseract_cmd = r'D:\ocr\tesseract.exe'


def convert_pdf_pages(pdf_path, start_page, end_page, lang='chi_sim',
                                    #选择poppler位置(要是没在path下的话)
                      poppler_path=r'D:\下载\poppler-24.02.0\Library\bin'):
    # 将PDF页面转换为图像
    images = convert_from_path(pdf_path, poppler_path=poppler_path, first_page=start_page, last_page=end_page)

    # 创建保存提取文字的文件
    text_file = os.path.splitext(pdf_path)[0] + ".txt"

    with open(text_file, 'a', encoding='utf-8') as f:
        for i, image in enumerate(images):
            text = pytesseract.image_to_string(image, lang=lang)
            f.write(f"Page {start_page + i}\n")
            f.write(text)
            f.write("\n\n")

    print(f"Pages {start_page} to {end_page} extracted and saved to {text_file}")

                                            # 选择poppler位置(要是没在path下的话)
def pdf_to_text(pdf_path, lang='chi_sim', poppler_path=r'D:\下载\poppler-24.02.0\Library\bin', pages_per_batch=10,
                max_workers=4):
    # 获取PDF页数
    pdf_reader = PdfReader(open(pdf_path, "rb"))
    total_pages = len(pdf_reader.pages)

    # 创建线程池
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for start_page in range(1, total_pages + 1, pages_per_batch):
            end_page = min(start_page + pages_per_batch - 1, total_pages)
            print(f"Submitting pages {start_page} to {end_page} for processing...")
            futures.append(executor.submit(convert_pdf_pages, pdf_path, start_page, end_page, lang, poppler_path))

        # 等待所有线程完成
        for future in futures:
            future.result()

    # 打印生成的文本文件路径
    text_file = os.path.splitext(pdf_path)[0] + ".txt"
    print(f"Text extracted and saved to {text_file}")


# 示例用法
pdf_path = '*.pdf' #选择要转换的对象位置
pdf_to_text(pdf_path, lang='chi_sim')  # 使用简体中文语言包