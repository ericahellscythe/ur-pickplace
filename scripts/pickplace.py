#!/usr/bin/env python3

import time
import rospy
import argparse
from onrobot_library import PPP
from universalrobot_library import ur_robot

def get_param():
    parser = argparse.ArgumentParser(description='Set options')
    parser.add_argument('--gripper', dest='gripper', type=str, default="rg2", choices=['rg2', 'rg6'], help='set gripper type, rg2 or rg6')
    parser.add_argument('--ip', dest='ip', type=str, default="192.168.1.1", help='set ip address')
    parser.add_argument('--port', dest='port', type=str, default="502", help='set port number')
    return parser.parse_args()

def pickplace_program():
    ur.go_to_pose_goal()
    # ppp.move_rg_gripper(1000, 200)
    # ppp.vacuum_on()
    # time.sleep(1)
    # ppp.release_vacuum()
    # time.sleep(1)
    # ppp.vacuum_on_channelB()
    # time.sleep(1)
    # ppp.release_vacuum()
    # ppp.close_connection()
    
if __name__ == '__main__':
    args = get_param()
    onrobot_gripper = args.gripper
    onrobot_ip = args.ip
    onrobot_port = args.port
    ppp = PPP(onrobot_gripper, onrobot_ip, onrobot_port)
    rospy.init_node("ur10", anonymous=True)
    ur = ur_robot()
    pickplace_program()