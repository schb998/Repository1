import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
from yatpkg.util.data import StorageIO, StorageType

if __name__ == '__main__':
    mot = pd.read_csv("Z:\\Paediatric Data\\Motion Capture\\PLB-02\\Day 1\\Walk01-07.csv", skiprows=4)
    find("Frame,Sub Frame,FP2 - Force,FP2 - Moment,FP2 - CoP,FP3 - Force, FP3 - Moment,FP3 - CoP")
    data_directory = "{0}/ForcePlateData {1}/".format
    s = StorageIO.load("Z:\\Paediatric Data\\Motion Capture\\PLB-02\\Day 1\\Walk01-07.csv", StorageType.nexus)
    data_sio = s.data
    f = mot.iloc[:, 18:21]
    f = f.to_numpy()
    data = []
    for i in range(0, 12070):
        try:
            data.append([float(f[i, 0]), float(f[i, 1]), float(f[i, 2])])
        except ValueError:
            data.append([0.0, 0.0, 0.0])
            pass
    data_np = np.asarray(data)
    start_id = -1
    is_heel_found = False
    end_id = -1
    is_toe_found = False
    for i in range(0, data_np.shape[0]):
        if i > start_id and abs(data_np[i, 2]) > 10 and not is_heel_found:
            start_id = i
            is_heel_found = True

        if i > end_id and is_heel_found and abs(data_np[i, 2]) < 10 and not is_toe_found:
            end_id = i
            is_toe_found = True

    plot.figure()
    plot.plot(data_np[:, 2])
    plot.plot(start_id, data_np[start_id, 2], 'x')
    plot.plot(end_id, data_np[end_id, 2], 'x')
    plot.show()
    print()