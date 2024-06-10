#  d_GraphMakerStandards.py
#
#  This script is used to generate graphs for all participants in a given folder.
#  It is assumed that the participant folders are named in the format:
#  Inputs:
#  folder_path: Path to folder containing participant folders
#  total_angles: Dictionary of angles to be plotted.
#  inter_comparison: If false, interventions will be plotted separately.

#  Outputs: Mean +/- Standard Deviation for each angle for each participant (Graph and corresponding data).
#  Non-mean data will also be saved.

# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
import matplotlib.pyplot as plt

from plot_single import *
from plot_multi import *
from plot_multi_non_mean import *
from plot_special_spm1d import *

# Set directory path
folder_path = "C:\\Users\\alow056.UOA\\OneDrive - The University of Auckland\\UOA\\PhD\\Research\\year " \
              "3\\Gait\\Participants\\"  # path to data

total_angles = {"right": ["hip_flexion_r", "hip_adduction_r", "hip_rotation_r", "knee_angle_r", "ankle_angle_r",
                          "subtalar_angle_r"],
                "left": ["hip_flexion_l", "hip_adduction_l", "hip_rotation_l", "knee_angle_l", "ankle_angle_l",
                         "subtalar_angle_l"]}

inter_comparison = True  # If false, interventions will be plotted separately.
direction = ["Away"]  # Gait Phase Away OR Return

# Create dictionary of all experiments
data = {
    'profileX': {
        'left': {
            'experiment1': ['Baseline', 'LeftBellyVib1min20Hz'],
            'experiment2': ['post_RightTendonVib1min20HzPost', 'WBV1min20Hz'],
            'experiment3': ['post_WBV1min20HzPost', 'LeftBellyVib1min55Hz'],
            'experiment4': ['post_LeftBellyVib1min55HzPost', 'WBV3min20Hz']
        },
        'right': {
            'experiment1': ['post_LeftBellyVib1min20HzPost', 'RightTendonVib1min20Hz']
        }
    },
    # Profile Justin
    'profileY': {
        'left': {
            'experiment1': ['post_RightBellyVib1min20HzPost', 'LeftTendonVib1min20Hz'],
            'experiment2': ['post_LeftTendonVib1min20HzPost', 'WBV1min20Hz']
        },
        'right': {
            'experiment1': ['Baseline', 'RightBellyVib1min20Hz']
        }
    },
    # Profile Julie
    'profileZ': {
        'left': {
            'experiment1': ['Baseline', 'LeftBellyVib1min55Hz'],
            'experiment2': ['post_WBV1min22HzPost', 'WBV3min22Hz'],
            'experiment3': ['post_WBV3min22HzPost', 'LeftBellyVib1min20Hz'],
            'experiment4': ['post_RightTendonVib1min20HzPost', 'LeftBellyVib3min20Hz'],
            'experiment5': ['post_LeftBellyVib1min20HzPost', 'WBV1min20Hz']
        },
        'right': {
            'experiment1': ['post_LeftBellyVib1min55HzPost', 'RightTendonVib1min55Hz'],
            'experiment2': ['post_RightTendonVib1min55HzPost', 'WBV1min22Hz'],
            'experiment3': ['post_LeftBellyVib1min20HzPost', 'RightTendonVib1min20Hz']
        }
    }
}
# Add each participant to the dictionary and assign a profile to each
participant_list = {'Participant_01': 'profileX', 'Participant_02': 'profileX', 'Participant_03': 'profileZ',
                    'Participant_04': 'profileY', 'Participant_05': 'profileX'}
participant_list = {'Participant_02': 'profileX'}

for p in participant_list:
    participant = ['{}'.format(p)]
    for s in data[participant_list[p]]:
        side = [s]
        experiments_list = data[participant_list[p]][s]
        for e in experiments_list:
            plt.close('all')
            experiments = experiments_list[e]
            print('{} {} {}'.format(participant, side, experiments))

            if inter_comparison:  # Conditions plotted on the same graph
                # plot_single(folder_path, total_angles, participant, direction, side, experiments) # Forms graphs/data for individual experiments
                plot_multi(folder_path, total_angles, participant, direction, side, experiments) # Forms non-mean data and mean plots/data
                # plot_multi_non_mean(folder_path, total_angles, participant, direction, side, experiments) # Forms non-mean plots
                plot_special_spm1d(folder_path, total_angles, participant, direction, side, experiments)

                print('doing some inter batch')
            else:
                for n in range(len(experiments_list)):  # Conditions plotted on separate graphs (i.e. one graph/series)
                    experiments = ['{}'.format(experiments_list[n])]
                    # print('{} {}'.format(participant, experiments))
                    # plot_single(folder_path, total_angles, participant, direction, side, experiments)
                    # plot_multi(folder_path, total_angles, participant, direction, side, experiments)
                    # plot_multi_non_mean(folder_path, total_angles, participant, direction, side, experiments)
                    # plot_special(folder_path, total_angles, participant, direction, side, experiments)