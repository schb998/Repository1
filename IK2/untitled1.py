# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:38:10 2024

@author: schb998
"""

from yatpkg.util.data import StorageIO, StorageType, Yatsdo, TRC, Mesh, MYXML
from yatpkg.util.opensim_tools import IK
from scipy.signal import find_peaks
import numpy as np
import os


def create_ik_setup_from_template():
    # example data can be found in the 'yatpkg/util/examples/example_data' folder
    data = "/example_data/opensim/"   # path to data
    ikconfig = {
        "model_file": os.getcwd()+data + "gait2392_simbody.osim",
        "marker_file": os.getcwd()+data + "Sit00.trc",
        "output_motion_file": os.getcwd()+data + "test.sto",
        "template": os.getcwd()+data + "IK_walk.xml"
    }
    save_name = "ik_setup.xml"
    IK.write_ik_setup_xml(ikconfig, save_name)


def create_id_setup_from_template():
    s = StorageIO.load("G:/Shared drives/Rocco Hip Replacement Study/01/opensim/pre-op/force_plate/Sit00.mot",
                       StorageType.mot)
    s.write_mot("G:/Shared drives/Rocco Hip Replacement Study/01/opensim/pre-op/force_plate/Sit00abc.mot")
    m = MYXML("G:/Shared drives/Rocco Hip Replacement Study/01/opensim/xml/sitpre.xml")
    m.set_value("results_directory", "abc")
    m.write("G:/Shared drives/Rocco Hip Replacement Study/01/opensim/xml/sitpre_test.xml")
    print()
    vicon_config = []
    w = ""
    se = ""
    s = ""
    s0 = {}
    for cf in vicon_config:
        f = w + s + "/" + se + "/" + cf
        m = MYXML(f)
        dc = s0[s]
        a = m.tree.getElementsByTagName("ParamDefinitionList")
        for b in a:
            if b.attributes['name'].value == "DeviceOutputComponent::Analog EMG::Voltage":
                c = b.getElementsByTagName("ParamList")
                for d in c:
                    p = d.getElementsByTagName("Param")
                    for n in p:
                        if n.attributes['name'].value == "DeviceOutputComponentName":
                            print(n.attributes['value'].value)
                            n.attributes['value'].value = dc[n.attributes['value'].value]
                            print(n.attributes['value'].value)
                            break
                pass
        m.write(f)



def batch_run_ik():
    data = os.getcwd()
    file_list = [f for f in os.listdir(data) if f.endswith(".xml")]
    for f in file_list:
        IK.run(f)
    pass


def find_stride(file):
    sto = StorageIO.load(file, StorageType.mot)
    leg = {"knee_angle_r": "right_",
           "knee_angle_l": "left_"
           }

    for keyw in ["knee_angle_r", "knee_angle_l"]:
        kd_ = sto.data[keyw]
        ar, _ = find_peaks(kd_, distance=20)
        ar0, _ = find_peaks(-kd_, distance=20, height=np.max(-kd_) * 0.1)
        peakR = [p for p in ar0 if -kd_[p] < np.max(-kd_) * 0.6]
        pkr = []
        stride = []
        for pk in peakR:
            pkList = []
            for ark in ar:
                k = ark - pk
                if k < 0:
                    pkList.append(ark)
            if len(pkList) > 0:
                pkr.append(pkList[-1])
        for pr in range(0, len(pkr) - 1):
            st = pkr[pr]
            en = pkr[pr + 1]
            dc = sto.data.iloc[st:en, :].to_numpy()
            dc[:, 0] = dc[:, 0] - dc[0, 0]  # zero time
            ml = Yatsdo(dc)
            ml.column_labels = [c for c in sto.data.columns]

            # calculate sample time
            dt = dc[-1, 0] / 100
            t_samples = [it * dt for it in range(0, 100)]
            sample = ml.get_samples(t_samples, as_pandas=True)
            stride.append(sample)
        leg[keyw] = stride
    return leg


def convert_opensim_vtp_to_stl():
    Mesh.convert_vtp_2_stl_batch("D:/Apps/OpenSim 4.4/Geometry/")


if __name__ == '__main__':

    # t = TRC.create_from_c3d("E:/12 Test run-20231212T034950Z-001/05-12 Test run/test_0512_OG/New Session/straight path 1.c3d")
    # t.write("E:/12 Test run-20231212T034950Z-001/05-12 Test run/test_0512_OG/New Session/straight path 1.trc")
    # # print(os.getcwd())
    # create_ik_setup_from_template()
    batch_run_ik()
    # data = "C://Users//tyeu008//Downloads//P001_1402//MMG//Test//T1//test_1402//Straight path 1_test.trc"
    # s: TRC = StorageIO.load(data, StorageType.trc)
    # print(type(s))

    # convert_opensim_vtp_to_stl()

    print()
    pass