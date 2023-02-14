#!/usr/bin/env python3

import rospy
import argparse
from robot_library import PPP

def get_param():
    parser = argparse.ArgumentParser(description='Set options')
    parser.add_argument('--ip', dest='ip', type=str, default="192.168.1.1", help='set ip address')
    parser.add_argument('--port', dest='port', type=str, default="502", help='set port number')
    return parser.parse_args()

def pickplace_program():
    ppp = PPP(onrobot_ip, onrobot_port)

if __name__ == '__main__':
    args = get_param()
    onrobot_ip = args.ip
    onrobot_port = args.port
    pickplace_program()