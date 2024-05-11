#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int16

def callback_smartguys(data):
    global smartguys_data
    smartguys_data = data.data
    check_and_display()

def callback_xs(data):
    global xs_data
    xs_data = data.data
    check_and_display()

def check_and_display():
    if smartguys_data == "HIGH" and xs_data > 50:
        rospy.loginfo(smartguys_data + " " + str(xs_data) + ": " + "LANCAR")
    elif smartguys_data == "MEDIUM" and xs_data > 50:
        rospy.loginfo(smartguys_data + " " + str(xs_data) + ": " + "PATAH-PATAH")
    elif smartguys_data == "LOW" and xs_data > 50:
        rospy.loginfo(smartguys_data + " " + str(xs_data) + ": " + "NGE-LAG")
    else:
        rospy.loginfo(smartguys_data + " " + str(xs_data) + ": " + "MENDING TURU")

rospy.init_node('budi_subscriber')
smartguys_data = ""
xs_data = 0
rospy.Subscriber('smartguys_data', String, callback_smartguys)
rospy.Subscriber('xs_data', Int16, callback_xs)
rospy.spin()
