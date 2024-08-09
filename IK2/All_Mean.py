import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import glob

# Define the path to the main folder
folder_path = r"C:\Users\schb998\MyData\MyData\All_IK_Results"

subdirectories = [d for d in os.listdir(folder_path)]
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
    # yes_nos = info_sheet['Dynamic'].to_list()

    try:
        if folder == 'S6':  # only need because both heading exist
            trial = info_sheet['Trials'].to_list()
        else:
            trial = info_sheet['Trials/Events'].to_list()

    except KeyError:
        trial = info_sheet['Trials'].to_list()

    for row in range(0, info_sheet.shape[0]):
        # if yes_nos[row].lower() == 'no':
        #     continue
        t = trial[row]
        s = sides[row]
        target_file = [f for f in file_names if t.lower() in f.lower()]
        if s == 'Left':
            temp[folder]['left'].append(target_file[0])
        if s == 'Right':
            temp[folder]['right'].append(target_file[0])

    def mean_data(side):
        data_block = [pd.read_csv("{0}\\{1}\\{2}".format(folder_path, folder, f)) for f in temp[folder][side]]
        if len(data_block) == 0:
            return None
        # storage of data
        results_temp = np.zeros([100, data_block[0].shape[1]])
        cols = [c for c in data_block[0].columns]
        for d in range(0, len(data_block)):
            d0 = data_block[d].to_numpy()
            results_temp += d0
        results = pd.DataFrame(data=results_temp/len(data_block), columns=cols)
        return results
    mean_pd[folder]['left'] = mean_data('left')
    mean_pd[folder]['right'] = mean_data('right')

pass
plt.figure(figsize=(10, 6))

for folder in subdirectories:
     # if folder == 'PLB_06':
     #  continue
 # Plot mean as a solid line
     if mean_pd[folder]['left'] is not None:
       #plt.plot(mean_pd[folder]['left']['hip_rotation_l'], label=folder, linewidth=2, color='red')
        plt.plot(mean_pd[folder]['left']['ankle_angle_l'], label=folder, linewidth=2)
     if mean_pd[folder]['right'] is not None:
       # plt.plot(mean_pd[folder]['right']['ankle_angle_r'], label=folder, linewidth=2)
        plt.plot(mean_pd[folder]['right']['hip_rotation_r'], label=folder, linewidth=2, color='blue')

plt.title("Knee")
plt.xlabel("Gait Cycle (%)")
plt.ylabel("Ev(-)/Inv(+) (Deg)")
plt.legend()
plt.show()



pass
