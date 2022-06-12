#!/bin/bash

xrandr --output HDMI-0 --scale 1.3333x1.3333 # Scale monitor from 1080p to 1440p 
xrandr --output DP-0 --pos 1440x580 # Move monitor 1 to desired position.
xrandr --output DP-2 --pos 4880x1050 # Move monitor 3 to desired position.