# Code to extract strides from each IK trial (i.e. trials with multiple strides in it).
# Must specify participant, direction, and which leg (left or right)
# Files/directory must also be setup correctly according to template
# Goes through all trials, identifies each stride, then stores each stride into a single CSV

# Will create and export files to "Strides Extracted"


import matplotlib.pyplot as plt
import a_opensim_examples
from a_opensim_examples import find_stride
import os
import pandas as pd

participant = "participant_07"  # Participant
direction = "Away"  # Gait Phase Away OR Return
folder_path = "C:\\Users\\schb998\\MyData\\Participants\\"
# folder_path = "C:\\Users\\alow056.UOA\\OneDrive - The University of Auckland\\UOA\\PhD\\Research\\year " \
#               "3\\Gait\\Participants\\"  # path to data
data_directory = "{0}/participant gait {1}/".format(participant, direction)
# outputdir_for_iksetup = folder_path + data_directory + "IKSetups/"

# Trial Details
# participant = "participant_03"  # Participant
# direction = "Return"  # Gait Phase Away OR Return
side = ['left', 'right']  # specify which leg (right or leg) # Specify leg side

# File Path directory
# folder_path = "C:\\Users\\alow056.UOA\\OneDrive - The University of Auckland\\UOA\\PhD\\Research\\year " \
#               "3\\Gait\\Participants\\"  # path to data
# data_directory = "{0}/participant gait {1}/".format(participant, direction)
inputdir_for_ik = folder_path + data_directory + "IKs Filtered/"

# column names is a dictonary (3D). Therefore column names -> right/left -> data (e.g. angles)
column_names = {"right": ["hip_flexion_r", "hip_adduction_r", "hip_rotation_r", "knee_angle_r", "ankle_angle_r",
                          "subtalar_angle_r"],
                "left": ["hip_flexion_l", "hip_adduction_l", "hip_rotation_l", "knee_angle_l", "ankle_angle_l",
                         "subtalar_angle_l"]}

# ---------------------------
# WORKING ON THIS SECTION

# Loop through both sides
# for sides in column_names:

# ---------------------------


for s in side:
    iK_names = os.listdir(inputdir_for_ik)
    leg_data = {i: [] for i in column_names[s]}  # Creates an empty dictionary (space to store the data (ik)
    data_column_name = {i: [] for i in column_names[s]}  # stores strings of the column headings
    for file_name in iK_names:
        if file_name.endswith(".csv") and "static" not in file_name.lower():  # confirms file is an .sto
            strides = find_stride(inputdir_for_ik + file_name)  # Extracts strides. Storing as a 3D dictionary
            # (Side, left and right),

            # list each stride, stride data (normalised)
            for i in range(0, len(strides[s])):  # goes through each stride for specified leg, stores that information
                stride = strides[s][i][column_names[s]]  # current stride
                for j in range(0, len(column_names[s])):  # Loops though
                    leg_data[column_names[s][j]].append(stride.iloc[:, j])  # Taking only the desired data from the
                    # larger stride dictionary (i.e. matrix) ("iloc" returns all the rows in the column j)
                    data_column_name[column_names[s][j]].append(
                        file_name + "_" + s + "_stride_" + str(i))  # Creates a list of all the column headings
            pass
    pass

    # Creates folder for storing the individual strides
    folder_strides = folder_path + data_directory + "Strides Extracted/"
    if not os.path.exists(folder_strides):
        os.makedirs(folder_strides)

    # Compiles all the strides (from all trials) into one CSV
    for j in range(0, len(column_names[s])):  # Loops though
        temp_table = pd.DataFrame(data=leg_data[column_names[s][j]])
        desired_data = temp_table.transpose()
        desired_data.columns = data_column_name[column_names[s][j]]  # .columns specifies the headings/labels
        outfilename = "{2}{0} IKs {1}.csv".format(participant, column_names[s][j], folder_strides)
        desired_data.to_csv(outfilename, index=False)
