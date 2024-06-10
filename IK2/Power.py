
import pandas as pd
import numpy as np
import os
from yatpkg.util.data import Yatsdo, StorageIO
data_directory_IK = "C:\\Users\\schb998\\MyData\\TestAnklePower\\"
data_directory_ID = "C:\\Users\\schb998\\MyData\\MyData\\PLB_02\\ID_normalisedData\\"

# Initialize an empty list to store joint angles
joint_angles = []

# Loop through mot files in the directory
for filename in os.listdir(data_directory_IK):
    if filename.endswith(".mot"):
        filepath = os.path.join(data_directory_IK, filename)
        df = pd.read_mot(filepath)
        # change
        joint_angles = df["ankle_angle_r"].tolist()
        joint_angles.extend(joint_angles)

# Convert angles to radians
radian_angles = [np.radians(angle) for angle in joint_angles]

# Initialize an empty list to store angular velocities
angular_velocities = []

# Loop through each data point (except the first one)
for i in range(1, len(df)):
    # Calculate time difference
    delta_t = df['time'].iloc[i] - df['time'].iloc[i - 1]

    # Calculate joint angle difference
    delta_theta = df['joint_angle'].iloc[i] - df['joint_angle'].iloc[i - 1]

    # Compute angular velocity
    angular_velocity_i = delta_theta / delta_t

    # Append to the list
    angular_velocities.append(angular_velocity_i)

# Add the angular velocities back to the DataFrame
df['angular_velocity'] = [np.nan] + angular_velocities

# Optionally, plot the angular velocity
plt.plot(df['time'], df['angular_velocity'], label='Angular Velocity')
plt.xlabel('Time')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('Angular Velocity vs. Time')
plt.legend()
plt.show()
























