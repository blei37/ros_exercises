#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
from ros_exercises.msg import OpenSpace


class SpacePublisher():
    def __init__(self):
        rospy.init_node("open_space_publisher")
        rospy.Subscriber("fake_scan", LaserScan, self.callback)
        self.maxDistance = 0.0
        self.maxAngle = 0.0
        self.pub = rospy.Publisher("open_space", OpenSpace, queue_size = 10)
        self.rate = rospy.Rate(20)


    def callback(self, data):
        for i in range(len(data.ranges)):
            dist = data.ranges[i]
            if dist > self.maxDistance:
                self.maxDistance = float(dist)
                self.maxAngle = float(data.angle_min) + float(i) * float(data.angle_increment)

    def run(self):
        while not rospy.is_shutdown():
            msg = OpenSpace()
            msg.angle = self.maxAngle
            msg.distance = self.maxDistance
            self.pub.publish(msg)
            rospy.loginfo(msg)
            self.rate.sleep()
            self.rate.sleep()


if __name__ == "__main__":
    pub = SpacePublisher()
    pub.run()
