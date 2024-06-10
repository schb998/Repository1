import numpy as np
import pandas as pd
import os
from yatpkg.util.data import StorageIO, StorageType, Yatsdo
import matplotlib.pyplot as plt

def normalize_data(data_path, output_dir, weight=35):

    """
    Normalize data from 0 to 100 and save as .csv files.

    Args:
    - data_path: Path to the directory containing data files
    - output_dir: Directory to save the normalized data

    Returns:
    - None
    """
   # print("hello world")
    try:
        weght = 40
        # Loop through each file in the data directory
        for file_name in os.listdir(data_path):
            if file_name.endswith(".mot"):  # Check if file is a csv file
                print(f"Processing file: {file_name}")
                # Load the data from the file
                file_path = os.path.join(data_path, file_name)

                # Skip non-numeric rows at the beginning of the file
                # with open(file_path, 'r') as f:
                #     for line in f:
                #         if line.strip().replace('.', '', 1).isdigit():
                #             break
                #     file_position = f.tell()  # Get the file pointer position

                # Load the data from the file starting from the saved file pointer position
                # data = np.loadtxt(file_path, delimiter=",", skiprows=file_position)
                s = StorageIO.load(file_path, sto_type=StorageType.mot)
                data = s.data.to_numpy()
                d = Yatsdo(data)
                mn = np.min(d.x)
                mx = np.max(d.x)
                rg = mx-mn
                step = rg/100
                time_points = [t*step + mn for t in range(0, 100)]
                norm_l = d.get_samples(time_points)
                norm_l[:, 0] = [x for x in range(0, 100)]
                norm_l[:, 1:] /= weight
                ret = pd.DataFrame(data=norm_l, columns=[c for c in s.data.columns])
                # Create the output directory if it doesn't exist
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                # Save normalized data as CSV
                output_file_name = os.path.splitext(file_name)[0] + "_normalized.csv"
                output_file_path = os.path.join(output_dir, output_file_name)
                ret.to_csv(output_file_path, index=False)
                # plt.figure(figsize=(10, 6))
                # plt.figure()
                # plt.plot(output_file_name)
                # plt.show()


                print("Normalized data saved as {0}".format(output_file_path))
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':

    print()

    data_path = "C:\\Users\\schb998\\MyData\\MyData\\S7\\ID_Results\\"
    output_dir = "C:\\Users\\schb998\\MyData\\TEST\\"
    participant_weight = 35

    print("We are the main")
    normalize_data(data_path, output_dir, weight=participant_weight)


apples = normalize_data(data_path, output_dir, weight=participant_weight)


