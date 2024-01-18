


import os
 

all_files = []
for root, dirs, files in os.walk('E:\\Git\\2022\\bing_images'):
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)
        if os.path.isfile(file_path):
            all_files.append(file_path)
            
# print(all_files)