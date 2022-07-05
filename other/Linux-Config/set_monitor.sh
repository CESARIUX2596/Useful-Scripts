#!/bin/bash

xrandr --output HDMI-0 --scale 1.3333x1.3333 --rate 60 # Scale monitor from 1080p to 1440p 
xrandr --output DP-0 --pos 1440x580 --rate 144 # Move monitor 1 to desired position.
xrandr --output DP-2 --pos 4880x1050 --rate 165 # Move monitor 3 to desired position.