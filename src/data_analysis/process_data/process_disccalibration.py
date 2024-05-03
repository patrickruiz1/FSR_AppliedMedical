import os 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

def calibration_discrete_curvefitting(FSR_dir, file_name, ref_force):
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'processed', file_name)
    save_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'calibration', file_name)

    df = pd.read_csv(file_path, index_col = None)

    data = {}
    flag, new_data, counter = False, [], 0
    for index, row in df.iterrows():
        if row.iloc[0] > ref_force:
            flag = True
            new_data.append([float(row.iloc[0]), float(row.iloc[1])])
        else:
            if flag == True:
                data[counter] = new_data
                counter = counter + 1
                flag = False
                new_data = []
            else:
                pass
    
    new_data = {}
    for i in list(data.keys()):
        if len(data[i]) == 1:
            new_data[i] = data[i]
        else:
            curr, diff, val = 0, 100, 0
            for j in data[i]:
                diff = ref_force - j[0]
                if diff < curr:
                    curr = diff
                    diff = 0
                    val = j
                else:
                    pass
        new_data[i] = val

    data_df = pd.DataFrame.from_dict(new_data, orient = 'index', columns = ['Force (lbf)', 'Resistance (Ohms)'])
    data_df.to_csv(save_path, index = False)

os.system('clear')
# os.system('cls')
FSR_dir = 'FSR_S1'
file_name = 'FSR_S1_Calibration(9.0lbf)' + '.csv'
calibration_discrete_curvefitting(FSR_dir, file_name, 9.0)