'''
    ---------------------------------------------
    -  Simple Python Script Blocks All Ports !  -
    -           Very Simple Script !            -
    ---------------------------------------------
'''
import os
import platform

if platform == "linux" or platform == "linux2":
    for i in range(65535):
        os.system("iptables -A INPUT -p tcp --destination-port {} -j DROP".format(i))
        # Also Block Udp Traffic !
        os.system("iptables -I INPUT -p udp --dport {} -j DROP".format(i))
