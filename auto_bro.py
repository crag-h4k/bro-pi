#!/usr/bin/python3

from subprocess import check_output, run, Popen
from time import sleep
from sys import argv

from cfg import DEPLOY_DELAY, NETWORK_CONF, NODE_CONF, DEPLOY_CMD, SERVICE_LOCK


def make_subnets():
    
    subnets = []
    ip_addr = check_output('hostname -I',shell=True).decode('utf-8')
    addrs = ip_addr.split(' ')
    
    for addr in addrs:
        if addr[:2].isdigit() == False:
            continue
        subnets.append(addr.rsplit('.',1)[0] + '.0/24\n')
    return subnets

def check_iface_state(iface):

    command = 'cat /sys/class/net/' + iface + '/operstate'

    if 'up' in check_output(command ,shell=True).decode('utf-8'):
        print(iface + ' up')
        return True

    else:
        print(iface + ' down')
        return False
    
def make_node():
    
    iface_list = []
    ifaces = check_output('ls /sys/class/net',shell=True).decode('utf-8').split('\n')
    text = '[logger]\ntype=logger\nhost=localhost\n#\n[manager]\ntype=manager\nhost=localhost\n#\n[proxy]\ntype=proxy\nhost=localhost\n#\n'

    iface_list.append(text)

    for iface in ifaces:
        if (iface == '') or (iface == 'lo') or ('br' in iface):
            continue
        if check_iface_state(iface) == False:
            continue
        
        worker_text = '[worker-'+iface+']\ntype=worker\nhost=localhost\ninterface='+iface+'\n#\n'
        
        iface_list.append(worker_text) 

    return iface_list

def check_service(service):

    command = 'ss -4 state listening'

    while service not in check_output(command,shell=True).decode('utf-8'):
        continue
    
    print(service,'up')
    
    return True
    
def make_conf(text_list, outfile):

    with open(outfile, 'w+') as f:

        for text in text_list:
            f.write(text)

        f.close()

def deploy_bro():

    check_service(SERVICE_LOCK)
    make_conf(make_subnets(), NETWORK_CONF)
    make_conf(make_node(), NODE_CONF)
    sleep(DEPLOY_DELAY)
    Popen(DEPLOY_CMD,shell=True)
    return 

