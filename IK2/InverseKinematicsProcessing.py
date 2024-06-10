#Import packages
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import h5py
import re
import numpy as np
import os
import json
from matplotlib.colors import to_rgba
from scipy.stats import kruskal
from scipy.stats import mannwhitneyu


all_trials_stride_data = {}
strideList_dict={}
biomechanicsHeader = []
colors = ['blue', 'orange', 'green', 'red']  

#File Paths
folderpath = Path(r'F:\AlterG\Control\Data\01')
HeelPath = r'F:\AlterG\Control\Data\01\Gait\DevicesData.mat'
header_line = 8
mot_files = list((folderpath /'IKResults').glob("*.mot"))
pattern = r"\\([^\\]+)_ik"

#Processing of each mot file
for file_path in mot_files:
    file_path_str = str(file_path)
    data = pd.read_csv(file_path, sep = '\t', header = header_line)
    current_headers = data.columns
    biomechanicsHeader = list(biomechanicsHeader)
    biomechanicsHeader.extend(current_headers.tolist())
 
    match = re.search(pattern, file_path_str)
    
    if match:
        trial = match.group(1)
        with h5py.File(HeelPath, 'r') as file:
            if trial in file['NexusData']:
                nexus_data = list(file['NexusData'][trial]['Right']['emg_idx']) 
                #Kinematic Indexing
                heels = [array / 10 for array in nexus_data] 
                for header in data.columns:
                    strideList = []
                    for idx, element in enumerate(heels):
                        if idx < len(heels) - 1:
                            next_element = heels[idx + 1]
                            start_index = int(element[0])
                            end_index = int(next_element[0])
                            strideList_dict[header] = strideList
                            data_between_elements = data.iloc[start_index:end_index][header].values
                            if data_between_elements.size > 0:
                                strideList.append([data_between_elements])

                    # Append the strideList for this header and then this trial to the overall data
                    if header not in all_trials_stride_data:
                        all_trials_stride_data[header] = []
                    all_trials_stride_data[header].append(strideList)  
                    #print(len(all_trials_stride_data))

#Visualisation of of all strides - currently not plotting any graphs
def plot_all_strides_for_header(header, all_trials_stride_data):
    if header in all_trials_stride_data:
        plt.figure(figsize=(10, 6))
        print(header)

        # Iterate through each trial's strides for the header
        for trial_strides in all_trials_stride_data[header]:
            for stride in trial_strides:
                stride_data = np.array(stride).squeeze() 
                
                # ##### Plot each stride - this is not printing even without indent ######
                # if stride_data.ndim == 1 and stride_data.size > 0:  # Check to ensure non-empty 1D array
                #     plt.plot(stride_data, alpha=0.5)  # Set a low alpha to manage overlap visibility
                #     plt.title(f'All Strides for {header}')
                #     plt.xlabel('Time or Frame Index')
                #     plt.ylabel('Measurement Value')
                #     plt.grid(True)
                #     plt.show()
                # else:
                #     print(f"Header '{header}' not found in the data.")

#Interpolation to 100 points followed by mean and standard deviation plotted for each header      
for header in biomechanicsHeader:
    if header in strideList_dict and len(strideList_dict[header]) > 0:
        interpolated_values_list = []

        # Iterate over strides for the current header
        for strides in strideList_dict[header]:
            stride_array = np.array(strides)
            if len(stride_array[0]) < 1:
                continue

            #Interpolate to 100 data points
            original_indices = np.arange(len(stride_array[0]))
            interpolated_indices = np.linspace(0, len(stride_array[0]) - 1, 100)
            interpolated_values = np.interp(interpolated_indices, original_indices, stride_array[0])
            # Append interpolated values to the list
            interpolated_values_list.append(interpolated_values)
            
        # Check if the list is not empty before attempting to concatenate
        if len(interpolated_values_list) > 0:
            concatenated_array = np.vstack(interpolated_values_list)

            if concatenated_array.shape[0] > 1:  
                mean_values = np.mean(concatenated_array, axis=0)
                std_values = np.std(concatenated_array, axis=0)
                data_to_save = np.column_stack((mean_values, std_values))
                csv_filename = f'{header}_data.csv'  # Adjust filename for clarity
                np.savetxt(csv_filename, data_to_save, delimiter=',', header='Mean,Std Dev', comments='')

                # Plot the mean and standard deviation for each header
                #plt.figure()  
                plt.plot(mean_values, label=f'Mean - {header}')
                plt.fill_between(range(len(mean_values)), mean_values - std_values, mean_values + std_values, alpha=0.3, label=f'Std Dev - {header}')
                plt.xlabel('Time')
                plt.ylabel(f'{header} (Degrees)')
                plt.title(f'All Strides for - {header}')
                plt.legend()
                #plt.show()
            else:
                print(f"Not enough data for statistics in header '{header}'.")
      
#Mean and standard deviation calculations
def plot_from_csv(csv_filename, header, color, participant_label):
    data = np.loadtxt(csv_filename, delimiter=',', skiprows=1)  # Assuming the first row is a header

    # Extract mean and standard deviation columns
    mean_values = data[:, 0]
    std_values = data[:, 1]

    # Plot the mean and standard deviation with enhanced visibility
    plt.plot(mean_values, label=f'Mean - {header}', color=color, linewidth=2)
    plt.fill_between(range(len(mean_values)), mean_values - std_values, mean_values + std_values, alpha=0.2, color=color)
    plt.text(len(mean_values) - 1, mean_values[-1], participant_label, ha='right', va='center', color=color)

# Graphs plotted for individual header
for i, header in enumerate(biomechanicsHeader):
    # Modify the following lines to match your CSV file naming convention
    csv_participant1 = f'{header}_data1.csv'
    csv_participant2 = f'{header}_data2.csv'

    plt.figure()
    # Plot data from the first CSV file with the corresponding color and label for Participant 1 & 2
    plot_from_csv(csv_participant1, header, colors[i % len(colors)], participant_label='Participant 1')
    plot_from_csv(csv_participant2, header, colors[(i + 1) % len(colors)], participant_label='Participant 2')

    # Customize the plot as needed
    plt.title(f'Overlayed Graph for Header - {header}')
    plt.xlabel('% Gait Cycle')
    plt.ylabel(f'{header} (Degrees)')
    plt.legend()
    plt.show()

#############
