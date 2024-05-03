import os 
import csv
import numpy as np
import pandas as pd 


def stability_analysis(FSR_dir):
    data_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability')
    files_list = list(os.listdir(data_path))
    sorted_files_list = sorted(files_list)[1:]
    
    data = []
    for file in sorted_files_list:
        file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'stability', file)
        with open(file_path, encoding='utf-8', errors='replace') as csvfile:
            csv_file = csv.reader((line.replace('\0', '') for line in csvfile))
            next(csv_file)
            for row in csv_file:
                data.append(row)
                print(row)


        

os.system('clear')
# os.system('cls')
FSR_dir = 'FSR_S1'
stability_analysis(FSR_dir)
