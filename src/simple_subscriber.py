#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import math

def callback(data):
    pub = rospy.Publisher("random_float_log", Float32)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    pub.publish(math.log(data.data))

def listener():
    rospy.init_node("simple_subscriber")
    rospy.Subscriber("my_random_float", Float32, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

