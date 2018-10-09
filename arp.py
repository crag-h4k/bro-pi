from scapy.all import srp, Ether, ARP, conf
from time import sleep
from datetime import datetime

from auto_bro import make_subnets
from cfg import ARP_DELAY, ARP_OUTFILE


class Host:
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac
        self.ts = datetime.now()

def arp_scan():
    subnets = make_subnets()
    for net in subnets:
        conf.verb = 0
        ans, unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=net),timeout=2, iface='eth0', inter=0.1) # whatis inter?
        hosts = []

        for snd,rcv in ans:
            ip = rcv.sprintf(r'%ARP.psrc%')
            mac = rcv.sprintf(r'%Ether.src%')
            H = Host(ip,mac)
            print(H.ip, H.mac, H.ts)
            hosts.append(H)

    return hosts

def write_arp(host_arr, fname):

    for H in host_arr:
        text = str(H.ip) + ',' + str(H.mac) + ',' + str(H.ts) + '\n'
        with open(fname, 'a+') as f:
            f.write(text)

    f.close()
    
    return

def continuous_arp():

    while True:
        write_arp(arp_scan(), ARP_OUTFILE)
        sleep(ARP_DELAY)
