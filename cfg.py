#!/usr/bin/env python3

from datetime import datetime

ARP_JSON = '/root/arp_scans/arp_results_' + datetime.now().strftime('%d_%b_%y') + '.json'
ARP_CSV = '/root/arp_scans/arp_results_' + datetime.now().strftime('%d_%b_%y') + '.csv'
ARP_DELAY = 30

IFACE = 'eth0'


DEPLOY_DELAY = 10
DEPLOY_CMD = 'broctl deploy'
SERVICE_LOCK = 'ssh'
NETWORK_CONF = '/usr/local/bro/etc/networks.cfg'
NODE_CONF = '/usr/local/bro/etc/node.cfg'

