import os
from os import path
import shutil
import csv

cur_path = os.getcwd()
csv_path = cur_path +'/query.csv'
f = open(csv_path, 'r', encoding='utf-8')
rd = csv.reader(f)

src_path = cur_path + '/image'
dst_path = cur_path + '/image_copy'

if not path.isdir(dst_path):
    os.makedirs(dst_path)

for line in rd:
    file_dir = src_path + '/' + line[0]
    if path.exists(file_dir):
        shutil.copy(file_dir, dst_path)
        print(file_dir)

f.close()
