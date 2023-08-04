# Network-Scanner
You can view the number of devices currently connected to your network and obtain their local IP addresses and MAC addresses.
--
I created a basic network scanner using argparse and scapy.
**Syntax:** python3 **file_name** --target **ip_address / subnet**
*E.g.* `python3 networkScanner.py --target 192.162.11.1/24`
**REMINDER:** Use with root/administrative privileges.
#
In order to proceed, it is necessary to have argparse, ipaddress, and scapy installed.
* pip install argparse
* pip install ipaddress
* pip install scapy 

 ## **Sample Output:**
IP   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  MAC Address
_----------------------------------------------_
192.166.11.1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 00:50:58:c0:00:06 
_----------------------------------------------_
192.166.11.2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 00:50:58:ea:55:09
_----------------------------------------------_
192.166.11.254 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 00:50:58:f8:c4:6e
