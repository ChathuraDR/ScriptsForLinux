#!/bin/sh
while :
do
	LIFE=$(upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep percentage | cut -d":" -f2 | cut -d"%" -f1)
	STATE=$(upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep state | cut -d":" -f2 | grep charging)
	
	if [ $? -eq 0 ] && [ $LIFE -eq 100 ]; 
	then
		play bell.wav 2> /dev/null
	fi
done
