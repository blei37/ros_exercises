#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import math
import random

def publisher():
    rospy.init_node("fake_scan_publisher")
    pub = rospy.Publisher("fake_scan", LaserScan, queue_size=10)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        scan_msg = LaserScan()
        scan_msg.header.stamp = rospy.get_rostime()
        scan_msg.header.frame_id = "base_link"
        scan_msg.angle_min = (-2.0/3.0) * math.pi 
        scan_msg.angle_max = (2.0/3.0) * math.pi
        scan_msg.angle_increment = (1.0/300.0) * math.pi
        scan_msg.range_min = 1.0
        scan_msg.range_max = 10.0
        scan_msg.scan_time= (1.0/20.0)
        ranges = []
        for _ in range(401):
            ranges.append(random.uniform(1.0, 10.0))
        scan_msg.ranges = ranges
        pub.publish(scan_msg)
        rospy.loginfo(scan_msg)
        rate.sleep()


if __name__ == '__main__':
    publisher()

