import scapy.all as scapy
import argparse
import ipaddress

def commandLine():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="IP range")
    options = parser.parse_args()

    # Validate the IP range format
    try:
        ipaddress.ip_network(options.target)
    except ValueError:
        print("Invalid IP range format. Please provide a valid IP range (e.g., 192.168.0.0/24).")
        exit(1)

    return options

def printInformation(answered_clients):

    print("IP\t\tMAC Address\n-----------------------")
    clients = []
    for client in answered_clients:
        print(client["ip"] + "\t" + client["mac"])
        print("-----------------------")

def scan(ip):
    arp_req = scapy.ARP(pdst=ip) # initial ip address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # random broadcast mac address
    arp_req_broadcast = broadcast/arp_req # combine
    answered = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0] # 0 = answered list
    # The data is organized in the array as ip and mac addresses.
    clients = []
    for element in answered:
        client_dic = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients.append(client_dic)
    # The data sending to print function
    printInformation(clients)

options = commandLine()
scan(options.target)