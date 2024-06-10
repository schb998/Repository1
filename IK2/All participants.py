import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import glob

# Define the path to the main folder
folder_path = r"C:\Users\schb998\MyData\MyData\All_IK_Results"
# listing subdirectories folders
subdirectories = [d for d in os.listdir(folder_path)]
print(subdirectories)
# dictionary for subdirectories
temp = {p: {'left': [], 'right': []} for p in subdirectories}

csv_files = "C:\\Users\\schb998\\MyData\\MyData\\All_Trials_Info\\"
csv_files = glob.glob(os.path.join(csv_files, "*.csv"))
# connecting subdirectories name to left and write in info sheet
mean_pd = {p: {'left': None, 'right': None} for p in subdirectories}
# loop over each folder in subdirectory list
for folder in subdirectories:
    folder_root_path = os.path.join(folder_path, folder)
    file_names = os.listdir(folder_root_path)
    # matching participants to info sheet
    participant = [f for f in csv_files if folder in f]
    # reads the first CSV file from the participant list and loads its data into a pandas DataFrame called info_sheet
    info_sheet = pd.read_csv(participant[0])
    # extracts Valid GaitCycle from info sheet
    sides = info_sheet['Valid GaitCycle'].to_list()
    trial = []
    # yes_nos = info_sheet['Dynamic'].to_list()

    try:
        if folder == 'S6':  # only need because both heading exist
            trial = info_sheet['Trials'].to_list()
        else:
            trial = info_sheet['Trials/Events'].to_list()

    except KeyError:
        # store data related to trials or events
        trial = info_sheet['Trials'].to_list()

    # if 'yes' in yes_nos:
    for row in range(0, info_sheet.shape[0]):
        # if yes_nos[row].lower() == 'no':
        #     continue
        t = trial[row]
        s = sides[row]
        # if row >= len(yes_nos) or yes_nos[row].lower() == 'no':
        #     continue
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
     if folder == 'PLB_06':
      continue
 # Plot mean as a solid line
     if mean_pd[folder]['left'] is not None:
       # plt.plot(mean_pd[folder]['left']['hip_flexion_l'], label=folder, linewidth=2, color='red')
        plt.plot(mean_pd[folder]['left']['hip_flexion_l'], label=folder, linewidth=2)
     if mean_pd[folder]['right'] is not None:
        plt.plot(mean_pd[folder]['right']['hip_flexion_r'], label=folder, linewidth=2)
       #  plt.plot(mean_pd[folder]['right']['hip_flexion_r'], label=folder, linewidth=2, color='blue')

plt.title("Hip Flexion")
plt.xlabel("Gait Cycle (%)")
plt.ylabel("Ext(-)/Flex(+) (Deg)")
plt.legend()
plt.show()



pass
