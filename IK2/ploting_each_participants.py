import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import glob

# Define the path to the main folder
# folder_path = r"C:\Users\schb998\MyData\MyData\All_IK_Results"
folder_path = r"C:\Users\schb998\MyData\MyData\All_ID_Normalised_Weight"

#subdirectories = [d for d in os.listdir(folder_path)]
subdirectories = ['S2']
print(subdirectories)
temp = {p: {'left': [], 'right': []} for p in subdirectories}

csv_files = "C:\\Users\\schb998\\MyData\\MyData\\All_Trials_Info\\"
csv_files = glob.glob(os.path.join(csv_files, "*.csv"))

mean_pd = {p: {'left': None, 'right': None} for p in subdirectories}

for folder in subdirectories:
    folder_root_path = os.path.join(folder_path, folder)
    file_names = os.listdir(folder_root_path)
    participant = [f for f in csv_files if folder in f]
    info_sheet = pd.read_csv(participant[0])
    sides = info_sheet['Valid GaitCycle'].to_list()
    trial = []
    yes_nos = info_sheet['Dynamic'].to_list()

    try:
        # if folder == 'S6':  # only need because both heading exist
        #     trial = info_sheet['Trials'].to_list()
        # else:
            trial = info_sheet['Trials/Events'].to_list()

    except KeyError:
        trial = info_sheet['Trials'].to_list()

    for row in range(0, info_sheet.shape[0]):
        # if isinstance(yes_nos[row], float) or isinstance(yes_nos[row], np.float32) or isinstance(yes_nos[row], np.float64):
        #     continue
        if yes_nos[row].lower() == 'no':
            continue
        t = trial[row]
        s = sides[row]
        target_file = [f for f in file_names if t.lower() in f.lower()]
        if s == 'Left':
            temp[folder]['left'].append(target_file[0])
        if s == 'Right':
            temp[folder]['right'].append(target_file[0])
pass
plt.figure(figsize=(10, 6))

for folder in subdirectories:
    if folder == 'S2' and temp[folder]['left'] is not None:
        data_left = [pd.read_csv("{0}\\{1}\\{2}".format(folder_path,folder,d)) for d in temp[folder]['left']]
        data_files = [d[:d.rindex('.')] for d in temp[folder]['left']]
    for dl in range(0, len(data_left)):
            plt.plot(-data_left[dl]['pelvis_list_moment'], label=folder+"_{0}_l".format(data_files[dl]), linewidth=2)
       # plt.plot(temp[folder]['left']['ankle_angle_l'], label=folder, linewidth=2)
    if folder == 'S2' and temp[folder]['right'] is not None:
       # plt.plot(temp[folder]['right']['ankle_angle_r'], label=folder, linewidth=2)
       data_right = [pd.read_csv("{0}\\{1}\\{2}".format(folder_path, folder, d)) for d in temp[folder]['right']]
       data_files = [d[:d.rindex('.')] for d in temp[folder]['right']]
    for dr in range(0, len(data_right)):
            plt.plot(-data_right[dr]['pelvis_list_moment'], label=folder+"_{0}_r".format(data_files[dr]), linewidth=2)

plt.title("Pelvis List", fontsize=18)
plt.xlabel("Gait Cycle (%)", fontsize=18)
plt.ylabel("Down(-)/Up(+) (N/Kg)", fontsize=18)
plt.legend()
plt.show()