from scapy.all import srp, Ether, ARP, conf
from time import sleep
from datetime import datetime
from json import dump

from auto_bro import make_subnets
from cfg import ARP_DELAY, ARP_OUTFILE
#from rgb import blink_led

class Host:
    def __init__(self, ipv4, subnet, mac):
        self.ipv4 = ipv4
        self.subnet = subnet
        self.mac = mac
        self.ts = datetime.now()

def arp_scan():
    subnets = make_subnets()
    for net in subnets:
        if '\n' in net:
            net = net.strip('\n')
        conf.verb = 0
        ans, unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=net),timeout=2, iface='eth0', inter=0.1) # whatis inter?
        hosts = []

        for snd,rcv in ans:
            ipv4 = rcv.sprintf(r'%ARP.psrc%')
            mac = rcv.sprintf(r'%Ether.src%')
            H = Host(ipv4, net, mac)
            print(H.ipv4, '\t', H.mac, '\t', H.ts)
            
            hosts.append(H)
    #print(hosts)
    print('#######')
    return hosts

def write_arp(host_arr, fname):
    json_name = 'hosts_' + host_arr[0].subnet
    data = {}
    data[json_name] = []

    for H in host_arr:
        #print(H.ipv4, H.mac, H.ts)
        data[json_name].append({'ipv4':H.ipv4, 'mac':H.mac, 'ts':str(H.ts)})

    with open(fname, 'a+') as f:
        dump(data,f)

    return

def continuous_arp():

    while True:
        try:
            write_arp(arp_scan(), ARP_OUTFILE)
            blink_led(purple)
            sleep(ARP_DELAY)
        except:
            continue
#continuous_arp()
write_arp(arp_scan(), ARP_OUTFILE)
