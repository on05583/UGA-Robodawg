#!/usr/bin/env python3
""" Manages the dynamixel motors used within the robot """
from dynamixel_sdk import PortHandler, PacketHandler

ADDR_MX_TORQUE_ENABLE = 24
ADDR_MX_GOAL_POSITION = 30
ADDR_MX_PRESENT_POSITION = 36
PROTOCOL_VERSION = 1.0
DEVICENAME = "/dev/ttyUSB0"
TORQUE_ENABLE = 1
TORQUE_DISABLE = 0
MAX_POS_VAL = 1023
MIN_POS_VAL = 0 

class DynamixelHandler:
    """ The dynamixel handler is used to handle all the dynamixels, allowing you to
    individually set/get positions, set torque, etc. based on the IDs of the dynamixels.

    Note: The handler, as well as the dynamixels, are only built to move through one channel of
    communication. It is important to remember that the dynamixels must be on the same baudrate, 
    and working with the same protocol version. Any other dynamixel will not get the same communications.
    
    However, if you want to use two different kinds of baudrates, you can create a second DynamixelHandler
    for that specific baudrate - just be aware that a command cannot be sent through both channels at once.
    You must close one and then open the other, since they occupy the same serial port.

    ~ Rishab
    """
    def __init__(self, baud: int = 1000000):
        self.port_handler = None
        self.packet_handler = None
        self.is_port_active = False
        self.baud = baud

    def set_pos(self, dynamixel_id: int, pos: int):
        """ Sets the position of an individual dynamixel provided the ID and position """
        try:
            self.packet_handler.write2ByteTxRx(self.port_handler, dynamixel_id, ADDR_MX_GOAL_POSITION, pos)
        except Exception as e:
            return e

    def get_pos(self, dynamixel_id: int):
        """ Gets the position of an individual dynamixel provided the ID """
        dxl_present_position = self.packet_handler.read2ByteTxRx(self.port_handler, dynamixel_id, ADDR_MX_PRESENT_POSITION)
        return dxl_present_position
    
    def set_torque(self, dynamixel_id: int, on: bool):
        """ Sets the torque status of an individual dynamixel provided the ID """
        try:
            if on:
                self.packet_handler.write1ByteTxRx(self.port_handler, dynamixel_id, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
            else:
                self.packet_handler.write1ByteTxRx(self.port_handler, dynamixel_id, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
        except Exception as e:
            return e

    def open_port(self):
        """ Opens the serial stream to all the dynamixels. This is for a specific baudrate and protocol version. """
        self.port_handler = PortHandler(DEVICENAME)
        self.packet_handler = PacketHandler(PROTOCOL_VERSION) 
        self.port_handler.openPort()
        self.port_handler.setBaudRate(self.baud)
        print("Dynamixel port opened.")
        self.is_port_active = True

    def close_port(self):
        """ Closes the serial stream to all the dynamixels. Makes sure all dynamixels are set to disabled torque. """
        for id in range(0, 30):
            try:
                self.set_torque(id, False)
            except Exception as e:
                pass
        
        self.port_handler.closePort()
        print("Dynamixel port closed.")
        self.is_port_active = False

    def is_port_active(self):
        """ Returns if the current port is opened or closed. """
        return self.is_port_active
