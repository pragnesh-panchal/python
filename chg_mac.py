#!/usr/bin/env python

#Importing necessary libraries to complete this script
import subprocess
import os
import sys


#Funtion for calling the usage of the script
def Usage():
    print("#########################################################################\n")
    print("Incorrect usage of script\n")
    print("Usage: python chg_mac.py <interface> <mac-address>\n")
    print("<interface> should be the interface value (e.g: eth0 or wlan0)\n")
    print("<mac-address> your desired mac-address for the interface.")	
    return



#Condition for calling the usage function	
if len(sys.argv) > 3:
    print("Too many arguments passed please see the usage below\n")
    Usage()

elif len(sys.argv) <= 2:
    print("Arguments are missing please see the usage below\n")
    Usage()    

else:
    #Commands to execute in shell
    subprocess.call("ifconfig " + sys.argv[1] +" down", shell=True)
    subprocess.call("ifconfig " + sys.argv[1] + " hw ether "+ sys.argv[2], shell=True)
    subprocess.call("ifconfig "+ sys.argv[1] + " up", shell=True)
