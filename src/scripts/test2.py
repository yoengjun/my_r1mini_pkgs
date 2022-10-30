#!/usr/bin/python

import sys
import rospy
from darknet_ros_msgs.msg import BoundingBoxes
from geometry_msgs.msg import Twist

rospy.init_node('test2')

def callback():
    print(rospy.Subscriber('darknet_ros/bounding_boxes', BoundingBoxes,callback))

     
if __name__ == '__main__':
    callback()




