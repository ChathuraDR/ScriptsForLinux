#!/bin/sh

STATUS=$(systemctl status apache2 | head -3 | grep -w 'Active' | cut -d':' -f2 | cut -d'(' -f1)
if [ $STATUS = "inactive" ];then
	$(echo "Apache2 is not running" | mail -s "Apache2 Status" xxxxxxxxxx92@gmail.com)
fi
