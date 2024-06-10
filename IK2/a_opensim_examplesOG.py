# Imports relavant classes/functions (UpperCase = class, smallCase = funciton)
# Class, function (begins with "def"), package
import pandas as pd
#util = utility
#YAT = "Yet Another Tool". pkg = Package, sdo = Storage data object
#yatpkg.util.data : StorageIO = inpout/output, reads in files lke TRC, COP3, MOT, STO.


from yatpkg.util.data import StorageIO, StorageType
# from yatpkg.mlde.ml_util import YatsdoML
from yatpkg.util.data import Yatsdo as YatsdoML
from yatpkg.util.opensim_tools import IK
from scipy.signal import find_peaks #scipy = Scientific python (which is built ontop of numpy) will call numpy itself
import numpy as np # math functions
import os #os = operation system, therefore allows interacting with operating system
import matplotlib.pyplot as plt
import copy


# Creates IK setup file
def create_ik_setup_from_template(info=None, save_name="ik_setup.xml"):

    IK.write_ik_setup(info["trc_file"],
                      info["template"],
                      info["model_file"],  # Opensim Model file
                      info["output_motion_file"],
                      save_name)

def batch_run_ik(file_list):
    for f in file_list:
        IK.run(f)
    pass


def find_stride(file):
    # sto = StorageIO.load(file, StorageType.mot)
    data0 = pd.read_csv(file)
    leg_mapper = {"knee_angle_r": "right",
                  "knee_angle_l": "left"
                  }
    leg = {}
    for keyw in ["knee_angle_r", "knee_angle_l"]: #keyw = keyword

        kd_ = copy.deepcopy(data0[keyw]) #kd = Knee Data
        ar, _ = find_peaks(kd_, distance=20) #ar = Angles right
        ar0, _ = find_peaks(-kd_, distance=20, height=np.max(-kd_) * 0.5)
        peakR = [p for p in ar0 if -kd_[p] <= np.max(-kd_)]
        pkr = []
        stride = []
        indx = -1
        for pk in peakR:
            indx += 1
            pkList = []
            temp_list = []
            for ark in ar:
                k = ark - pk
                if k > 0:
                    pkList.append(ark)
                if k < 0:
                    temp_list.append(ark)
            if len(temp_list) == 2 and indx == 0:
                pkr.append(temp_list[0])
            if len(pkList) > 0:
                v = pkList[0]
                if v not in pkr:
                    pkr.append(pkList[0])

        for pr in range(0, len(pkr) - 1):
            st = pkr[pr]
            en = pkr[pr + 1]
            dc = copy.deepcopy(data0.iloc[st:en, :].to_numpy())
            dc[:, 0] = dc[:, 0] - dc[0, 0]  # zero time
            ml = YatsdoML(dc)
            ml.column_labels = [c for c in data0.columns]

            # calculate sample time
            dt = dc[-1, 0] / 100
            t_samples = [it * dt for it in range(0, 101)]
            sample = ml.get_samples(t_samples, as_pandas=True)
            stride.append(sample)
        leg[leg_mapper[keyw]] = stride
    return leg


# Setups Data file directory, Creates IK setup file, calculates IKs in a batch (through Opensims)
# NOTE: Folder Directories must be setup with the same naming convention (else will not work)
# Scale vicon, capture motion, reconstruct, label, label, clean (gap fill and delete unnamed markers), export .TRC.
# Scale an Opensim Model, name opensim model file correctly (participant name_gait2392_simbody.osim), run code to create
# IK and strides)
if __name__ == '__main__':

    # Setup

    #Change these Varibles
    participant = "participant_07"  # Participant
    direction = "Away"  # Gait Phase Away OR Return
    folder_path = "C:\\Users\\schb998\\MyData\\Participants\\"
    # folder_path = "C:\\Users\\alow056.UOA\\OneDrive - The University of Auckland\\UOA\\PhD\\Research\\year " \
    #               "3\\Gait\\Participants\\"  # path to data
    data_directory = "{0}/participant gait {1}/".format(participant, direction)
    outputdir_for_iksetup = folder_path + data_directory + "IKSetups/"

    if not os.path.exists(outputdir_for_iksetup):
        os.makedirs(outputdir_for_iksetup)

    outputdir_for_ik = folder_path + data_directory + "IKs/"
    if not os.path.exists(outputdir_for_ik):
        os.makedirs(outputdir_for_ik)


    #Creating the XML file. Assumes that the markers do not chnge between the trials
    trc = [f for f in os.listdir(folder_path + data_directory) if f.endswith(".trc")]
    #print("{1}/{0}".format(file, wdir))
    for file in trc: # For loop, runs through the variable trc and stores current index as "file"
        ikconfig = { #Looking up the files. Therefore, put in path for the file
            "model_file": "{0}{1}/participant model/{1}_scaled.osim".format(folder_path, participant), #Specific model file
            "trc_file": "{0}{1}/{2}".format(folder_path, data_directory, file),
            "output_motion_file": outputdir_for_ik + "{0}.sto".format(file[:file.index(".trc")]),
            # "template": "C:\\Users\\alow056.UOA\\OneDrive - The University of Auckland\\UOA\\PhD\\Research\\year 3\\Gait\\template\\IK_walk.xml"
            "template": "C:\\Users\\schb998\\MyData\\Participants\\template\\IK_Setups.xml"
        }
        create_ik_setup_from_template(info=ikconfig, save_name=outputdir_for_iksetup + "{0}.xml".format(file[:file.index(".trc")]))

    # End of Setup

    # Batch run of IKs
    c = [folder_path + "{0}IKSetups/".format(data_directory) + f for f in os.listdir(folder_path + "{0}IKSetups/".format(data_directory))]
    batch_run_ik(c)