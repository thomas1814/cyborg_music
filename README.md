# README
This repository contains the source code for the music state ROS node in the NTNU Cyborg.

Node name: cyborg_music  
Language: Python  
Numbers of actionlib server(s): 1  

## Requirements:
* ROS  
* python-vlc  

python-vlc can be installed:  
//This is pip2 for Python 2.7 (used by ROS)  
$ sudo apt-get install python-pip  
$ sudo apt-get install vlc  
$ pip2 install python-vlc  

## Features:
*The music state: The Cyborg`s music state plays music for 20 seconds. Available at actionlib server topic cyborg_music/music. It plays a file called ~/music.mp3 (must exist!).

## Usage:
$ rosrun cyborg_music music.py
