#!/usr/bin/env python3

from dynamixel_handler import DynamixelHandler
import time, utility

handler = DynamixelHandler(1000000) 
#All Dynamixel Motors Used and their IDs
DYN_1 = 6
DYN_2 = 5

handler.open_port()

handler.set_pos(DYN_1, utility.angle_to_pos(1))
time.sleep(3)
print(handler.get_pos(DYN_1))
handler.set_pos(DYN_1, utility.angle_to_pos(300))
time.sleep(3)
print(handler.get_pos(DYN_1))

"""handler.set_pos(DYN_2, 200)
time.sleep(1)
handler.set_pos(DYN_2, 800)
time.sleep(1)
"""
handler.close_port()
