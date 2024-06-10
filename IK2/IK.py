# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:42:32 2024

@author: schb998
"""
<?xml version="1.0" encoding="UTF-8" ?>
<OpenSimDocument Version="40000">
	<InverseKinematicsTool>
		<!--The time range for the study.-->
		<time_range>-1 -1</time_range>
		<!--Name of the resulting inverse kinematics motion (.mot) file.-->
		<output_motion_file></output_motion_file>
		<!--Markers and coordinates to be considered (tasks) and their weightings. The sum of weighted-squared task errors composes the cost function.-->
		<IKTaskSet>
			<objects>
				<IKMarkerTask name="RACR">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LACR">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="Head">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="CLAV">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RSJC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RLEL">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RMEL">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RFAradius">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RFAulna">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LSJC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LLEL">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LMEL">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LFAradius">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LFAulna">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RASI">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LASI">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RPSI">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LPSI">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LHJC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RHJC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RLFC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RMFC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RKJC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RFib">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RTB2">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RLMAL">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RMMAL">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RAJC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RCAL">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RTOE">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RMT5">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LLFC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LMFC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LKJC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LFib">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LTB2">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LLMAL">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LMMAL">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LAJC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LCAL">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LTOE">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LMT5">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="REJC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LEJC">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="R_tibial_plateau">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="L_tibial_plateau">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="RMT2">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
				<IKMarkerTask name="LMT2">
					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
					<apply>true</apply>
					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
					<weight>1</weight>
				</IKMarkerTask>
			</objects>
			<groups />
		</IKTaskSet>
		<!--TRC file (.trc) containing the time history of observations of marker positions obtained during a motion capture experiment. Markers in this file that have a corresponding task and model marker are included.-->
		<marker_file></marker_file>
		<!--The name of the storage (.sto or .mot) file containing the time history of coordinate observations. Coordinate values from this file are included if there is a corresponding model coordinate and task. -->
		<coordinate_file>Unassigned</coordinate_file>
	</InverseKinematicsTool>
</OpenSimDocument>

