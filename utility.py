"""
-----------------------------
UGA ROBOTICS UTILITY LIBRARY
-----------------------------
"""

def angle_to_pos(angle: int = 0):#takes in angle(0-300), returns pos for dynamixel
    if angle > 300:
        angle = 300
    elif angle < 0:
        angle = 0
    pos: int = int((angle/300)*1023)
    return pos
