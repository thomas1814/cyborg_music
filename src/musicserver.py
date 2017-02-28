#!/usr/bin/env python
"""Created by Thomas Rostrup Andersen on 11/11/2016.
Copyright (C) 2016 Thomas Rostrup Andersen. All rights reserved."""

import time
import os
import vlc
import roslib 
import rospy
import actionlib
from std_msgs.msg import String
from cyborg_controller.msg import StateMachineAction, StateMachineGoal, StateMachineResult, StateMachineFeedback, EmotionalState, EmotionalFeedback, SystemState

__author__ = "Thomas Rostrup Andersen"
__copyright__ = "Copyright (C) 2016 Thomas Rostrup Andersen"
#__license__ = ""
__version__ = "0.0.2"
__all__ = []

class MusicServer():
	"""MusicServer"""

	timeout = 20 # (secunds)

	# The initzialzation. Sets up all the ROS topics.
	def __init__(self):
		self.server_music = actionlib.SimpleActionServer(rospy.get_name() + "/music", StateMachineAction, execute_cb=self.server_music_callback, auto_start = False)
		self.server_music.start()
		rospy.loginfo("MusicServer: Activated")


	# Called when the controller (state machine) sets the music state as active
	def server_music_callback(self, goal):
		rospy.loginfo("MusicServer: Executing music state...")
		homedir = os.path.expanduser("~")
		music = vlc.MediaPlayer(homedir + "/music.mp3")
		music.play()

		# This is the state loop
		rate = rospy.Rate(0.5) # (hz)
		start = time.time() # Prevent eternal looping
		while not rospy.is_shutdown():

			# Checkin with the controller
			if self.server_music.is_preempt_requested():
				music.stop()
				self.server_music.set_preempted()
				return

			# Timer
			end = time.time()
			if (end - start > self.timeout):
				music.stop()
				self.server_music.set_aborted()
				return
			rate.sleep()

