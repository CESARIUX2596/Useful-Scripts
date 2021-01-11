#! /bin/bash
# This script turns off the LEDs on the raspberry pi, needs sudo privileges to run.
echo 'Bravo Six, going dark...'
echo 0 >/sys/class/leds/led0/brightness
echo 0 >/sys/class/leds/led1/brightness
