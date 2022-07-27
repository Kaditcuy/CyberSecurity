#!/usr/bin/env python

"""
* Imports subprocess module from the python library
* Using the call function in suprocess to execute command line commands.
"""
import subprocess;

"""
*subprocess.call - Passes the argument as an OS command
* @ifconfig: Shell command to list and configure a network interface
* @shell = True: argument to make sure command only runs on a shell os 
"""
subprocess.call("ifconfig", shell=True);