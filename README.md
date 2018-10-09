broctl is too slow if it generates crash reports, I edited broctl to skip that step in node.py. Link my edited version by running the following command:


`ln ./confs/node.py /usr/local/bro/lib/broctl/BroControl/node.py`


Cronjobs to run at boot and check that it is running every 5 mins, I am using flock to ensure that main.py wll not running if already running


`@reboot /usr/bin/flock -n /home/r0ll0/bro-pi/.cron.lock /usr/bin/python3 /home/r0ll0/bro-pi/main.py`
`*/5 * * * * /usr/bin/flock -n /home/r0ll0/bro-pi/.cron.lock /usr/bin/python3 /home/r0ll0/bro-pi/main.py`
