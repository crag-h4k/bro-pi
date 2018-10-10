#!/usr/bin/python3

from subprocess import check_output, run, Popen,call
from time import sleep
from sys import argv

from utils import make_node, make_conf, make_subnets, check_service
from cfg import DEPLOY_DELAY, NETWORK_CONF, NODE_CONF, DEPLOY_CMD, SERVICE_LOCK
#from rgb import blink_led
from arp import continuous_arp

def deploy_bro():
    print('Deploying Bro')

    check_service(SERVICE_LOCK)
    make_conf(make_subnets(), NETWORK_CONF)
    make_conf(make_node(), NODE_CONF)
    #blink_led(orange)
    #sleep(DEPLOY_DELAY)
    #blink_led(yellow)
    #Popen(DEPLOY_CMD,shell=True)
    Popen(DEPLOY_CMD,shell=True)
    #blink_led(green)
    return 
