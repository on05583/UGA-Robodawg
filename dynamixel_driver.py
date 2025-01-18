#!/usr/bin/env python3

from utils.dynamixel_handler import DynamixelHandler
import time

handler = DynamixelHandler(1000000) 
#All Dynamixel Motors Used and their IDs
DYN_1 = 8
DYN_2 = 5

handler.open_port()

handler.set_pos(DYN_1, 200)
time.sleep(1)
handler.set_pos(DYN_1, 800)
time.sleep(1)

handler.set_pos(DYN_2, 200)
time.sleep(1)
handler.set_pos(DYN_2, 800)
time.sleep(1)

handler.close_port()
