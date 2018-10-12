# took out conf:1; 
from scapy.all import srp, Ether, ARP#, conf
from time import sleep
from datetime import datetime
from json import dump

from utils import make_subnets
from cfg import ARP_DELAY, ARP_JSON, ARP_CSV
#from rgb import blink_led

class Host:
    def __init__(self, ipv4, subnet, mac):
        self.ipv4 = ipv4
        self.subnet = subnet
        self.mac = mac
        self.ts = datetime.now()

def arp_scan():
    subnets = make_subnets()
    sep = '    '
    for net in subnets:
        if '\n' in net:
            net = net.strip('\n')
        #conf.verb = 0
        ans, unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=net),timeout=2, iface='eth0', inter=0.1)
        hosts = []

        for snd,rcv in ans:
            ipv4 = rcv.sprintf(r'%ARP.psrc%')
            mac = rcv.sprintf(r'%Ether.src%')
            H = Host(ipv4, net, mac)
            print(H.ipv4, sep, H.mac, sep, H.ts)
            
            hosts.append(H)
    #print(hosts)
    print('#######')
    return hosts

def write_arp_csv(host_arr, fname):

    for H in host_arr:
        text = str(H.subnet) + ',' + str(H.ip) + ',' + str(H.mac) + ',' + str(H.ts) + '\n'
        with open(fname, 'a+') as f:
            f.write(text)

    return

def write_arp_json(host_arr, fname):
    json_name = 'hosts_' + host_arr[0].subnet
    data = {}
    data[json_name] = []

    for H in host_arr:
        #print(H.ipv4, H.mac, H.ts)
        data[json_name].append({'ipv4':H.ipv4, 'mac':H.mac, 'ts':H.ts})

    with open(fname, 'a+') as f:
        dump(data,f)

    return

def continuous_arp():

    while True:
        try:
            #print('init arp scan')
            write_arp_json(arp_scan(), ARP_JSON)
            #write_arp_csv(arp_scan(), ARP_CSV
            #blink_led(purple)
            sleep(ARP_DELAY)
        except:
            continue

#continuous_arp()
