#!/usr/bin/python

import sys
import rospy
from darknet_ros_msgs.msg import BoundingBoxes

from geometry_msgs.msg import Twist



def new_bb():

    pub_cmd = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('find_up')

    for box in bb_msg.bounding_boxes:
        if box.Class == 'bottle':
            x = (box.xmin + box.xmax)/2
            y = (box.ymin + box.ymax)/2
            vx = 0.0
            vw = 0.0
            print "X=%d, Y=%d"%(x, y)
            if x < 600: # Image is in the left
                vx = 0.0
                vw = 0.1 #To the left
            elif x > 800: # image is in the right
                vx = 0.0
                vw = -0.1 # To the right
            else:
                vx = 0.1
                vw = 0.0
            twist = Twist()
            twist.linear.x = vx
            twist.angular.z = vw
            pub_cmd.publish(twist)

if __name__ == '__main__':
    try:
        new_bb()
    except rospy.ROSInterruptException:
        pass



