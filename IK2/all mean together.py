import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import glob

# Define the path to the main folder
folder_path = r"C:\Users\schb998\MyData\MyData\All_IK_Results"
# folder_path = r"C:\Users\schb998\MyData\MyData\All_ID_Normalised_Weight"
# listing subdirectories folders
subdirectories = [d for d in os.listdir(folder_path)]
print(subdirectories)
# dictionary for subdirectories
temp = {p: {'left': [], 'right': []} for p in subdirectories}

csv_files = "C:\\Users\\schb998\\MyData\\MyData\\All_Trials_Info\\"
csv_files = glob.glob(os.path.join(csv_files, "*.csv"))
# connecting subdirectories name to left and right in info sheet
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
            trial = info_sheet['Trials/Events'].to_list()

    except KeyError:
        # store data related to trials or events
        trial = info_sheet['Trials'].to_list()

    # if 'yes' in yes_nos:
    for row in range(0, info_sheet.shape[0]):
        # if yes_nos[row].lower() == 'no':
        #     continue
        t = str(trial[row])
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

    def mean_data_combine():
        left_col = ['pelvis_tilt', "pelvis_list", "pelvis_rotation", "pelvis_tx", "pelvis_ty", "pelvis_tz",
                    "hip_flexion_l", "hip_adduction_l", "hip_rotation_l", "knee_angle_l", "ankle_angle_l",
                    "subtalar_angle_l", "mtp_angle_l"]
        right_col = ['pelvis_tilt', "pelvis_list", "pelvis_rotation", "pelvis_tx", "pelvis_ty", "pelvis_tz",
                     "hip_flexion_r", "hip_adduction_r", "hip_rotation_r", "knee_angle_r", "ankle_angle_r",
                     "subtalar_angle_r", "mtp_angle_r"]
        data_col = ['pelvis_tilt', "pelvis_list", "pelvis_rotation", "pelvis_tx", "pelvis_ty", "pelvis_tz",
                     "hip_flexion", "hip_adduction", "hip_rotation", "knee_angle", "ankle_angle",
                     "subtalar_angle", "mtp_angle"]
        # left_col = ["pelvis_tilt_moment", "pelvis_list_moment",	"pelvis_rotation_moment",	"pelvis_tx_force",
        #             "pelvis_ty_force",	"pelvis_tz_force",	"hip_flexion_l_moment",	"hip_adduction_l_moment",
        #             "hip_rotation_l_moment", "lumbar_extension_moment",	"lumbar_bending_moment",
        #             "lumbar_rotation_moment", "knee_angle_l_moment",	"ankle_angle_l_moment",
        #             "subtalar_angle_l_moment",	"mtp_angle_l_moment",]
        # right_col = ["pelvis_tilt_moment",	"pelvis_list_moment",	"pelvis_rotation_moment",	"pelvis_tx_force",
        #              "pelvis_ty_force",	"pelvis_tz_force",	"hip_flexion_r_moment",	"hip_adduction_r_moment",
        #              "hip_rotation_r_moment", "lumbar_extension_moment",	"lumbar_bending_moment",
        #              "lumbar_rotation_moment",	"knee_angle_r_moment",	"ankle_angle_r_moment",
        #              "subtalar_angle_r_moment",	"mtp_angle_r_moment"]
        # data_col = ["pelvis_tilt_moment",	"pelvis_list_moment",	"pelvis_rotation_moment",	"pelvis_tx_force",
        #             "pelvis_ty_force",	"pelvis_tz_force",	"hip_flexion_moment",	"hip_adduction_moment",	"hip_rotation_moment",
        #             "lumbar_extension_moment",	"lumbar_bending_moment",	"lumbar_rotation_moment",	"knee_angle_moment",
        #             "ankle_angle_moment",	"subtalar_angle_moment",	"mtp_angle_moment"]

        data_block_l = [pd.read_csv("{0}\\{1}\\{2}".format(folder_path, folder, f)) for f in temp[folder]['left']]
        data_block_left = [d[left_col] for d in data_block_l]
        data_block_r = [pd.read_csv("{0}\\{1}\\{2}".format(folder_path, folder, f)) for f in temp[folder]['right']]
        data_block_right = [d[right_col] for d in data_block_r]
        if len(data_block_left) == 0:
            return None
        if len(data_block_right) == 0:
            return None
        # storage of data
        results_temp = np.zeros([100, data_block_left[0].shape[1]])
        for d in range(0, len(data_block_left)):
            d0 = data_block_left[d].to_numpy()
            results_temp += d0
        for d in range(0, len(data_block_right)):
            d0 = data_block_right[d].to_numpy()
            results_temp += d0
        results = pd.DataFrame(data=results_temp/(len(data_block_left)+len(data_block_right)), columns=data_col)
        return results
    mean_pd[folder]['left'] = mean_data('left')
    mean_pd[folder]['right'] = mean_data('right')
    mean_pd[folder]['combined'] = mean_data_combine()
pass
plt.figure(figsize=(10, 6))

for folder in subdirectories:
    if mean_pd[folder]['combined'] is not None:
        plt.plot(mean_pd[folder]['combined']['pelvis_list'], label=folder, linewidth=2)


plt.title("Pelvis List", fontsize=16)
plt.xlabel("Gait Cycle (%)", fontsize=16)
plt.ylabel("Down(-)/Up(+) (Deg)", fontsize=16)
plt.legend()
plt.show()

pass
