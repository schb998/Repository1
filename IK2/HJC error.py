import numpy as np


def calculate_error(point1, point2):
    # Convert points to numpy arrays
    point1 = np.array(point1)
    point2 = np.array(point2)

    # Calculate the Euclidean distance
    error = np.linalg.norm(point1 - point2)
    return error


# data
hip_joint_center_method1 = [-0.0055977200857277786]
hip_joint_center_method2 = [-0.060201]  # second method values

error = calculate_error(hip_joint_center_method1, hip_joint_center_method2)
print(f"Error between the two methods: {error}")
