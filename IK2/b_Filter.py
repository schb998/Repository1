# Applies a butterworth filter to IK data.
# Reads in the IK files and output the filtered file
# Must pass the correct file locations and set saved locations
# i.e code reads the IKs and then saves the filtered in a separate folder

from yatpkg.util.data import StorageIO, StorageType
from yatpkg.math.filters import Butterworth
from yatpkg.mlde.ml_util import YatsdoML
from yatpkg.util.opensim_tools import IK
from scipy.signal import find_peaks #scipy = Scientific python (which is built ontop of numpy) will call numpy itself
import numpy as np # math functions
import os #os = operating system, therefore allows interacting with operating system
import pandas as pd
import matplotlib.pyplot as plt


# Trial Details
participant = "participant_03"  # Participant
direction = "Return"  # Gait Phase Away OR Return

# File Path directory
folder_path = "C:\\Users\\alow056.UOA\\OneDrive - The University of Auckland\\UOA\\PhD\\Research\\year " \
              "3\\Gait\\Participants\\"  # path to data
data_directory = "{0}/participant gait {1}/".format(participant, direction)
inputdir_for_ik =  folder_path + data_directory + "IKs/"
outputdir_for_ik = folder_path + data_directory + "IKs Filtered/"

if not os.path.exists(outputdir_for_ik):
    os.makedirs(outputdir_for_ik)


#  -------------------

# Create loop to read through all files in folder
ik_trials = [f for f in os.listdir(inputdir_for_ik) if f.endswith(".sto")]
for trial in ik_trials:
    s = StorageIO.load(inputdir_for_ik + trial, StorageType.mot)  # Specify which file (trial) to read
    data = s.data  # Store the data
    temp = np.zeros(data.shape)

    colnames = [c for c in data.columns]
    data_np = data.to_numpy()
    for i in range(data.shape[1]):
        temp[:, i] = Butterworth.butter_low_filter(data_np[:, i], 6, 100, 4)
    out = pd.DataFrame(data=temp, columns=colnames)
    filename = trial[: trial.index('.sto')].lower()
    if 'post' in filename:
        filename = 'post_'+filename
    out.to_csv(outputdir_for_ik + '{0} filtered.csv'.format(filename), index=False)


# ------------------------

# s = StorageIO.load(outputdir_for_ik + 'BaseLine01.sto', StorageType.mot)
# data = s.data
# temp = np.zeros(data.shape)
#
# colnames = [c for c in data.columns]
# data_np = data.to_numpy()
# for i in range(data.shape[1]):
#     temp[:, i] = Butterworth.butter_low_filter(data_np[:, i], 6, 100, 4)
# out = pd.DataFrame(data=temp, columns=colnames)
# out.to_csv(outputdir_for_ik + 'filtered.csv', index=False)