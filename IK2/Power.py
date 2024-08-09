
import os
import pandas as pd
import numpy as np
import re
import math
import matplotlib.pyplot as plt

data_path = './C:/Users/schb998/OneDrive - The University of Auckland/Desktop/Data and Code/'

info_data_path = data_path + 'InfoSheet/' + 'Trials_PLB_02.csv'
info_data = pd.read_csv(info_data_path).values

valid_data = []
for row in info_data:
    if row[4] == 'No':
        continue
    else:
        valid_data.append(row)
    #moments.append(pd.read_csv(data_path + 'PLB_02_ID/' + row[0] + '.csv'))
    #print(row)

def matches(method_name, column_names, gaitcycle):
    if method_name == 'moments':
        if str(gaitcycle) == 'Right':
            pattern = r"_r_"
        else:
            pattern = r"_l_"

        ## read gaitcycle valid data for moments
        results = ['pelvis_tilt_moment', 'pelvis_list_moment', 'pelvis_rotation_moment']

        regex = re.compile(pattern)
        for index, string in enumerate(column_names):
            # Search for the pattern in each string
            match = regex.search(string)
            # print(string)
            # print(match)
            if match:
                # results.append((index, match.group()))
                results.append(column_names[index])

    # print(results)
    return results


## read gaitcycle valid data

valid_moments_data = []

for idx, row in enumerate(valid_data):
    gaitcycle = row[-1]
    moments_data = pd.read_csv(data_path + 'PLB_02_ID/' + row[0] + '.csv')
    columns = moments_data.columns

    valid_gaitcycle_columns = matches('moments', columns, gaitcycle)
    valid_filtered_data = moments_data[valid_gaitcycle_columns]
    valid_moments_data.append(valid_filtered_data)

pass
plt.figure(figsize=(10, 6))
plt.plot(valid_moments_data)







