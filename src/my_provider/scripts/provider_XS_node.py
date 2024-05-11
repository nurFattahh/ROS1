#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16
import random

rospy.init_node('xs_publisher')
pub = rospy.Publisher('xs_data', Int16, queue_size=10)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    data = random.randint(0, 100)
    pub.publish(data)
    rospy.loginfo("XS data sent: %s", data)
    rate.sleep()
