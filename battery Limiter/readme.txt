add this folder somewhere on your linux machine, and if you want to run this scirpt automatically on startup
just add this script into your cronjob,

As an example if you put this on your /opt directory,
run 
$crontab -e
then add, @reboot /opt/battery\ Limiter/battery.sh
