#!/usr/bin/env python

from std_msgs.msg import Float32
import rospy
import random

def publisher():
    pub = rospy.Publisher("my_random_float", Float32, queue_size=10)
    rospy.init_node("simple_publisher")
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        num = random.uniform(0, 10)
        rospy.loginfo("Publishing: %d", num)
        pub.publish(num)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
