#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import random

rospy.init_node('smartguys_publisher')
pub = rospy.Publisher('smartguys_data', String, queue_size=10)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    data = random.choice(["LOW", "MEDIUM", "HIGH"])
    pub.publish(data)
    rospy.loginfo("SmartGuys data sent: %s", data)
    rate.sleep()
