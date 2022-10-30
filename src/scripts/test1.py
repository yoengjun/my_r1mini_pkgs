#!/usr/bin/python

import sys
import rospy
import actionlib

from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import quaternion_from_euler
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


rospy.init_node('init_pose')
pub_init = rospy.Publisher("initialpose", PoseWithCovarianceStamped, queue_size=1)


def update_init_pose(x, y, theta):
    init_pose.header.stamp = rospy.Time.now()
    init_pose.pose.pose.position.x = x
    init_pose.pose.pose.position.y = y
    init_pose.pose.pose.orientation.w = 1.0
    q = quaternion_from_euler(0.0, 0.0, theta)
    init_pose.pose.pose.orientation.x = q[0]
    init_pose.pose.pose.orientation.y = q[1]
    init_pose.pose.pose.orientation.z = q[2]
    init_pose.pose.pose.orientation.w = q[3]

def send_goal(x,y,theta):
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    q = quaternion_from_euler(0.0, 0.0, theta)
    goal.target_pose.pose.orientation.x=q[0]
    goal.target_pose.pose.orientation.y=q[1]
    goal.target_pose.pose.orientation.z=q[2]
    goal.target_pose.pose.orientation.w=q[3]
    
    client.send_goal(goal)

def move_goal(a,b,theta):

    send_goal(a,b,theta)
    wait = client.wait_for_result()
    if not wait:
        print('Error')
    else:
        print(client.get_result())


init_pose = PoseWithCovarianceStamped()
init_pose.header.frame_id = "map" 
init_pose.header.stamp = rospy.Time.now()
init_pose.pose.pose.position.x = 0.0
init_pose.pose.pose.position.y = 0.0
init_pose.pose.pose.orientation.w = 1.0
update_init_pose(0.0, 0.0, 1)
pub_init.publish(init_pose)

client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
client.wait_for_server()

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"




move_goal(1.1, 2.8, 1)
print('----find object position 1----')


move_goal(0.3, 0.4, -1)
print('----position 2----')

print('----go home----')
move_goal(-0.05, 0.0, -1)
print('----home end----')









    
#rospy.Subscriber('darknet_ros/bounding_boxes', BoundingBoxes, new_bb, queue_size=10)




