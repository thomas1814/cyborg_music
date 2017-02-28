cmake_minimum_required(VERSION 2.8.3)
project(cyborg_music)

find_package( catkin REQUIRED COMPONENTS
	roscpp
	rospy
	std_msgs
	message_generation
	actionlib_msgs
	actionlib
	genmsg
)

#catkin_install_python( PROGRAMS src/music.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

catkin_package( CATKIN_DEPENDS 
	roscpp
	rospy
	std_msgs
	message_runtime
	actionlib_msgs
)

include_directories( ${catkin_INCLUDE_DIRS} )
