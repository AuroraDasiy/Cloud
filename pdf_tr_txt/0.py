import os

poppler_path = r'D:\下载\poppler-24.02.0\Library\bin'
if os.path.exists(poppler_path):
    print("Poppler path exists.")
else:
    print("Poppler path does not exist.")