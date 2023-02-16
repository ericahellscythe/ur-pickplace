from pymodbus.client.sync import ModbusTcpClient as ModbusClient

import sys
import copy
import time
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg


class PPP:
    
    def __init__(self, gripper, ip, port):
        self.client = ModbusClient(
            ip,
            port=port,
            stopbits=1,
            bytesize=8,
            parity='E',
            baudrate=115200,
            timeout=1)
        if gripper not in ['rg2', 'rg6']:
            print("Please specify either rg2 or rg6.")
            return
        self.gripper = gripper  # RG2/6
        self.open_connection()

    def open_connection(self):
        """Opens the connection with the gripper."""
        try:
            self.client.connect()
            print('connected to gripper')
        except Exception as e:
            print(e)

    def close_connection(self):
        """Closes the connection with the gripper."""
        self.client.close()

    # Target force to be reached when gripping and holding a workpiece.
    # The valid range is 0-400 for the RG2 and 0-1200 for the RG6.
    def set_target_force(self, force_val):
        result = self.client.write_register(address=0, value=force_val, unit=66)

    # Moves gripper to the specified width
    def move_rg_gripper(self, width_val, force_val):
        try:
            width_val = int(width_val)
            force_val = int(force_val)
            if self.gripper == 'rg2':
                if width_val >= 0 or width_val <= 1100:
                    if force_val >= 0 or force_val <= 400:
                        params = [force_val, width_val, 16]
                        print("moving gripper.")
                        result = self.client.write_registers(address=0, values=params, unit=66)
            if self.gripper == 'rg6':
                if width_val >= 0 or width_val <= 1400:
                    if force_val >= 0 or force_val <= 1200:
                        params = [force_val, width_val, 16]
                        print("moving gripper.")
                        result = self.client.write_registers(address=0, values=params, unit=66)
        except ValueError:
            print('Wrong input')
            return
        
    def vacuum_on(self):
        """Turns on all vacuums."""
        modeval = 0x0100  # grip
        command = 0x00ff  # 100 % vacuum
        commands = [modeval+command, modeval+command]
        result = self.client.write_registers(address=0, values=commands, unit=67)
        print("Turning on all vacuums.")

    def release_vacuum(self):
        """Releases all vacuums"""
        modeval = 0x0000  # release
        command = 0x0000  # 0 % vacuum
        commands = [modeval+command, modeval+command]
        result = self.client.write_registers(address=0, values=commands, unit=67)
        print("Release all vacuums.")
        time.sleep(1.0)

    def vacuum_on_channelA(self):
        """Turns on the vacuum of channel A."""
        modeval = 0x0100  # grip
        command = 0x00ff  # 100 % vacuum
        result = self.client.write_register(address=0, value=modeval+command, unit=67)
        print("Turn on the vacuum of channel A.")

    def vacuum_on_channelB(self):
        """Turns on the vacuum of channel B."""
        modeval = 0x0100  # grip
        command = 0x00ff  # 100 % vacuum
        result = self.client.write_register(address=1, value=modeval+command, unit=67)
        print("Turn on the vacuum of channel B.")

    def release_vacuum_channelA(self):
        """Releases the vacuum of channel A."""
        modeval = 0x0000  # release
        command = 0x0000  # 0 % vacuum
        result = self.client.write_register(address=0, value=modeval+command, unit=67)
        print("Release the vacuum of channel A.")
        time.sleep(1.0)

    def release_vacuum_channelB(self):
        """Releases the vacuum of channel B."""
        modeval = 0x0000  # release
        command = 0x0000  # 0 % vacuum
        result = self.client.write_register(address=1, value=modeval+command, unit=67)
        print("Release the vacuum of channel B.")
        time.sleep(1.0)