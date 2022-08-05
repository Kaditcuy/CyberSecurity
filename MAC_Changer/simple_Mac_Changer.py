#!/usr/bin/env python

"""
* Changes the mac address of eth0(i.e a network interface) yo 00:11:22:33:44:66
"""
import subprocess;

network_interface = " eth0 ";
new_mac = " 00:66:33:11:22:44 ";
        
subprocess.call("ifconfig" + network_interface + "down", shell=True);
subprocess.call("ifconfig" + network_interface + "hw ether" + new_mac , shell=True);
subprocess.call("ifconfig" + network_interface + "up", shell=True);
