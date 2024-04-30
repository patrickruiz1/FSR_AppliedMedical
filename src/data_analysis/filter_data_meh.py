import os
import csv
import pandas as pd 

def retrieve_datapath(FSR_name):
    data_dir = file_path = os.path.join(os.getcwd(), 'data', FSR_name)
    



FSR_dir = 'FSR_01'
file_name = 'FSR_01_calibration_data_29Apr24_10-48-51.csv'
file_path = os.path.join(os.getcwd(), 'data', FSR_dir, file_name)

df = pd.read_csv(file_path, index_col = False)

drop_rows = []
for index, row in df.iterrows():
    if row[2] == ' None':
        drop_rows.append(index)

df = df.drop(drop_rows)

loadcell_data, dmm_data = [], []
for index, row in df.iterrows():
    if row[0] == 'LoadCell':
        loadcell_data.append([row[1], row[2]])

pair = 0
for i in range(len(loadcell_data)):
    for index, j in df.iterrows():
        if loadcell_data[i][0] == j[1]:
            dmm_data.append([j[1], j[2]])
            pair = pair + 1
            print(str(pair) + ' out of ' + str(len(loadcell_data)*2) + ' found')

load, ohms = [], []
for row in range(len(dmm_data)):
    if row%2 == 0:
        load.append(dmm_data[row])
    else:
        ohms.append(dmm_data[row])


new_df = pd.DataFrame()
new_df['load'] = load
new_df['ohms'] = ohms

new_df.to_csv('filtered_data.csv')
