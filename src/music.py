#!/usr/bin/env python
"""Created by Thomas Rostrup Andersen on 11/11/2016.
Copyright (C) 2016 Thomas Rostrup Andersen. All rights reserved."""

import rospy
import sys
from musicserver import MusicServer

__author__ = "Thomas Rostrup Andersen"
__copyright__ = "Copyright (C) 2016 Thomas Rostrup Andersen"
#__license__ = ""
__version__ = "0.0.2"
__all__ = []

"""Cyborg Music Module"""


def main():
	rospy.init_node("cyborg_music")
	music_server = MusicServer()
	rospy.spin()

if __name__ == "__main__":
	print("Cyborg Music: Starting Program...")

	if sys.version_info < (2,5):
		print("Cyborg Music: Running Python version " + str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro) + " (Python version 2.5 or grater is required)...")
		exit()

	main()

	print("Cyborg Music: End of Program...")
