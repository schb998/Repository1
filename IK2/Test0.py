import os
import pandas as pd
import numpy as np
import re
import math
from scipy import interpolate
import matplotlib.pyplot as plt


def matches(method_name, column_names, gaitcycle):
    if method_name == 'moments':
        if str(gaitcycle) == 'Right':
            pattern = r"_r_"
        else:
            pattern = r"_l_"

        ## read gaitcycle valid data for moments
        results = ['pelvis_tilt_moment', 'pelvis_list_moment', 'pelvis_rotation_moment']

        regex = re.compile(pattern)
        for index, string in enumerate(column_names):
            # Search for the pattern in each string
            match = regex.search(string)
            if match:
                # results.append((index, match.group()))
                results.append(column_names[index])

    # print(results)
    return results


 ## get angles data
def matches_angles(column_names, gaitcycle):
    results = ['pelvis_tilt','pelvis_list','pelvis_rotation']
    rads_columns = ['pelvis_rotation']
    for name in column_names:
        if name[-2] != '_':
            continue
        else:
            if gaitcycle[0].lower() == name[-1]:
                results.append(name)
                rads_columns.append(name)

        return results, rads_columns



if __name__ == "__main__":
    data_path = 'C:\\Users\\schb998\\MyData\\MyData\\PLB_04\\Power\\'

    info_data_path = data_path + 'InfoSheet/' + 'Trials_PLB_04.csv'
    info_data = pd.read_csv(info_data_path).values

    #moments = []
    valid_data = []
    for row in info_data:
        if row[4] == 'No':
            continue
        else:
            valid_data.append(row)

    ## read gaitcycle valid data

    valid_moments_data = []

    for idx, row in enumerate(valid_data):
        gaitcycle = row[-1]
        moments_data = pd.read_csv(data_path + 'PLB_04_ID/' + row[0] + '.csv')
        columns = moments_data.columns

        valid_gaitcycle_columns = matches('moments', columns, gaitcycle)
        valid_filtered_data = moments_data[valid_gaitcycle_columns]
        valid_moments_data.append(valid_filtered_data)
    plt.figure()
    for tri in valid_moments_data:
        cols = [c for c in tri.columns]
        plt.plot(tri[cols[-3]], label=cols[-3])
    plt.legend()

    angles_valid_data = []
    for row in info_data:
        if row[4] == 'No':
            continue
        angles_data = pd.read_csv(data_path + 'PLB_04_Ik/' + row[0] + '.csv')
        gaitcycle = row[-1]
        columns_r = [f for f in angles_data.columns if 'right' in row[-1].lower() and f.endswith('_r')]
        columns_l = [f for f in angles_data.columns if 'left' in row[-1].lower() and f.endswith('_l')]
        columns = columns_r
        if 'left' in row[-1].lower():
            columns = columns_l
        #print(columns)
        valid_gaitcycle_columns, rads_columns = matches_angles(columns, gaitcycle)
        columns.insert(0,'pelvis_tilt')
        columns.insert(1,'pelvis_list')
        columns.insert(2,'pelvis_rotation')
        time_x = angles_data['time']
        deg_data0 = (np.pi/180)*angles_data[columns]
        angles_valid_data.append(deg_data0)

    plt.figure()
    for tri in angles_valid_data:
        cols = [c for c in tri.columns]
        plt.plot(tri[cols[-3]], label=cols[-3])
    plt.legend()

    x_time = [f for f in range(0, 100)]
    # calculate angular velocity
    angular_velocity = []

    for i in range(len(angles_valid_data)):
        trial = angles_valid_data[i]
        t_col = [t for t in trial.columns]
        curve = {}
        dev_curve = {}
        x = [f for f in range(0, 100)]
        data = trial.to_numpy()
        for j in range(0, trial.shape[1]):
            p = interpolate.InterpolatedUnivariateSpline(x, data[:, j])
            curve[j] = p
            dev_curve[j] = p.derivative()
        a = []
        for j in range(0, trial.shape[1]):
            a.append(dev_curve[j](x_time))
        vel = np.squeeze(np.array(a)).transpose()
        angular_velocity.append(pd.DataFrame(data=vel, columns=trial.columns))
        pass

    plt.figure()
    for tri in angular_velocity:
        cols = [c for c in tri.columns]
        plt.plot(tri[cols[-3]], label=cols[-3])
    plt.legend()

    print(angular_velocity)

    # power calc

    power_columns = []
    for vd in valid_moments_data:
        cols = [c for c in vd.columns]
        cl = []
        for c in cols:
            cl.append(c.replace('moment', 'power'))
        power_columns.append(cl)

    powers = []
    for i in range(len(valid_data)):
        p_col = power_columns[i]
        power_data = []
        valid_moments_data_columns = []
        for cols in valid_moments_data[i]:
            valid_moments_data_columns.append(cols)

        angular_velocity_columns = []
        for cols in angular_velocity[i]:
            angular_velocity_columns.append(cols)

        valid_moments_data_process = valid_moments_data[i]
        angular_velocity_process = angular_velocity[i]
        power_data = np.zeros([100, 10])
        print(len(power_columns))
        for j in range(0, len(power_columns[i])):
            pn = power_columns[i][j]
            vn = valid_moments_data_columns[j]
            an = angular_velocity_columns[j]
            M = valid_moments_data_process[vn]
            w = angular_velocity_process[an]
            P = M*w
            power_data[:, j] = P

        power_df = pd.DataFrame(power_data, columns=p_col)

        powers.append(power_df)
        power_df.to_csv(data_path + 'power_results_'+ str(i)  +'.csv')
    plt.figure()
    for tri in powers:
        cols = [c for c in tri.columns]
        plt.plot(tri[cols[-3]], label=cols[-3])
    plt.legend()
    plt.show()

