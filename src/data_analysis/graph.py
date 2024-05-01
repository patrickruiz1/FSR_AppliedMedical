import os 
import ast
import csv
import pandas as pd 
import matplotlib.pyplot as plt

FSR_dir = 'FSR_S1'
file_name = 'FSR_S1_Calibration_PreCond_Filtered.csv'
file_path = os.path.join(os.getcwd(), 'data', FSR_dir, file_name)

# values = []
# with open(file_path, 'r') as csvfile:
#     csv_file = csv.reader(csvfile)
    
#     for row in csv_file:
#         # final_values = []
#         for value in row[1:]:  # Skip the first value in each row
#             sublist = value.strip("[]").split(", ")
#             last_value = sublist[-1].strip("' ")
#             values.append(last_value)
#         # print(values)

# load, ohms = [], []
# for i in len(range(values)):
#     if i%2 == 0:
#         load.append(i)
#     else:
#         ohms.append(i)

load, ohms = [], []
values = []

with open(file_path, 'r') as csvfile:
    csv_file = csv.reader(csvfile)
    
    for row in csv_file:
        for value in row[1:]:  # Skip the first value in each row
            sublist = value.strip("[]").split(", ")
            last_value = sublist[-1].strip("' ")
            values.append(last_value)

for i in range(len(values)):
    if i % 2 == 0:
        load.append(values[i])
    else:
        ohms.append(values[i])

# print(len(load))
# print(len(ohms))

swag_load = pd.DataFrame(load)
swag_load.to_csv('load.csv')
swag_ohms = pd.DataFrame(ohms)
swag_ohms.to_csv('ohms.csv')


# plt.scatter(ohms, load)
# plt.show()


# with open(file_path, 'r') as csvfile:
#     csv_file = csv.reader(csvfile)
    
#     for row in csv_file:
#         print(row)

#     for row in csv_file:
#         values = list(row.values())
#         print(values)


# df = pd.read_csv(file_path, index_col = False)
# print(df)