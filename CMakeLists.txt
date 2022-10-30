cmake_minimum_required(VERSION 3.0.2)
project(r1mini_nv_jb)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  darknet_ros_msgs
  rospy
  std_msgs
  
)
catkin_python_setup()


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES r1mini_nv_jb
#  CATKIN_DEPENDS message_generation rospy std_msgs
#  DEPENDS system_lib
)

install(
  DIRECTORY scripts/
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  USE_SOURCE_PERMISSIONS
)

install(
  DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  USE_SOURCE_PERMISSIONS
)


