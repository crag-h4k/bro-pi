#!/usr/bin/python3
from datetime import datetime

ARP_OUTFILE = './scans/arp_results_' + datetime.now().strftime('%d%b%y_%H:%M%S') + '.csv'
ARP_DELAY = 5

DEPLOY_DELAY = 5
DEPLOY_CMD = 'broctl deploy'
SERVICE_LOCK = 'ssh'
NETWORK_CONF = '/usr/local/bro/etc/network.cfg'
NODE_CONF = '/usr/local/bro/etc/node.cfg'
