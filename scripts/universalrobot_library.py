from __future__ import print_function
from six.moves import input #pyright: ignore

import sys
import rospy
import numpy as np
import moveit_msgs.msg
import moveit_commander
import geometry_msgs.msg

from tf.transformations import *
from scipy.spatial.transform import Rotation as R
from moveit_commander.conversions import pose_to_list

class ur_robot:

    def __init__(self):
        super(ur_robot, self).__init__()
        moveit_commander.roscpp_initialize(sys.argv)
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.move_group = moveit_commander.MoveGroupCommander('manipulator')
        self.planning_frame = self.move_group.get_planning_frame()
        self.eef_link = self.move_group.get_end_effector_link()
        self.group_names = self.robot.get_group_names()

        display_trajectroy_publisher = rospy.Publisher("/move_group/display_planned_path", moveit_msgs.msg.DisplayTrajectory, queue_size=20)


    def go_to_pose_goal(self):

        pose_goal = self.move_group.get_current_pose().pose
        pose_goal.position.z += 0.4

        self.move_group.set_pose_target(pose_goal)
        success = self.move_group.go(wait=True)
        self.move_group.stop()
        self.move_group.clear_pose_targets()