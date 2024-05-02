import os 
import numpy as np
import pandas as pd 

def system_function(x, a = 12964.65477, b = -0.90492):
    return a * np.power(x, b)

def relative_error(actual, experimental):
    return (abs(actual - experimental)/actual)*100

def calculate_rmse(actual_values, estimated_values):
    act, exp = np.array(actual_values), np.array(estimated_values)
    squared_errors = (act - exp) ** 2
    rmse = np.sqrt(np.mean(squared_errors))
    return rmse

def calculate_mae(actual_values, estimated_values):
    act, exp = np.array(actual_values), np.array(estimated_values)
    absolute_errors = np.abs(act - exp)
    mae = np.mean(absolute_errors)
    return mae

def test_analysis(FSR_dir, file_name):
    file_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'pre-processed', file_name)
    save_path = os.path.join(os.getcwd(), 'data', FSR_dir, 'test', file_name)

    df = pd.read_csv(file_path, index_col = False)

    data = {}

    flag, new_data, counter = False, [], 0
    for index, row in df.iterrows():
        if row.iloc[0] > 5:
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
    
    data_df = pd.DataFrame.from_dict(data, orient = 'index')
    print(data_df)

    # This calculates RSME and MAE and adds it to the dictionary
    new_data = {}
    for i in list(data.keys()):
        actual, experimental = [], []
        for j in data[i]:
            j.append(round(system_function(float(j[0])), 5))
            actual.append(j[1])
            experimental.append(j[2])

        rsme = round(calculate_rmse(actual, experimental), 5)
        mae = round(calculate_mae(actual, experimental), 5)
        new_data[i] = data[i], rsme, mae
        
    print(new_data)
    count = 0
    for i in list(new_data.keys()):
        print(f'RSME = {new_data[i][1]}, MAE = {new_data[i][2]}')
        count = count + 1
    print(count)

    # new_df = pd.DataFrame.from_dict(new_data, orient = 'index')
    # print(new_df)


            



os.system('cls')
FSR_dir = 'FSR_S1'
file_name = 'FSR_S1_Stability_JFF_FastLoading' + '.csv'
test_analysis(FSR_dir, file_name)