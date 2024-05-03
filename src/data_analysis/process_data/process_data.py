import os 
import csv
import pandas as pd 

def process_data(FSR, file_name):
    FSR_dir = FSR
    file_name = file_name
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'raw', file_name)
    save_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'processed', file_name)
    
    df = pd.read_csv(file_path, index_col = False)

    drop_rows = []
    for index, row in df.iterrows():
        if row.iloc[2] == ' None':
            drop_rows.append(index)
    df = df.drop(drop_rows)

    loadcell_data, dmm_data = [], []
    for index, row in df.iterrows():
        if row.iloc[0] == 'LoadCell':
            loadcell_data.append([row.iloc[1], row.iloc[2]])
        elif row.iloc[0] == 'DMM':
            dmm_data.append([row.iloc[1], row.iloc[2]])
    
    dmm_dict = dict(dmm_data)
    loadcell_dict = dict(loadcell_data)

    for i in list(dmm_dict.keys()):
        if not i in list(loadcell_dict.keys()):
            dmm_dict.pop(i)

    new_dict = loadcell_dict.copy()

    for i in list(new_dict.keys()):
        if i in list(dmm_dict.keys()):
            value = [float(new_dict[i]), float(dmm_dict[i])]
            new_dict[i] = value
    
    new_df = pd.DataFrame(list(new_dict.values()), columns = ['Load (lbf)', 'Resistance (Ohms)'])
    new_df.to_csv(save_path)

os.system('clear')
FSR = 'FSR_S1'
file_name = 'FSR_S1_Calibration(5.0lbf)' + '.csv'
process_data(FSR, file_name)