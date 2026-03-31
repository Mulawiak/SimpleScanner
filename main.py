import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port",type=str, help="Specify ports to scan.\n Usage: -p [port] or -p [start_port]-[end_port]")
parser.add_argument("-ip", type=str, help="Specify the host to scan (IPv4 address). Usage: -ip [host_ipv4_address]")
args = parser.parse_args()

# Assign port arg to list, and specify if user wants to scan one port, or range of ports.
if '-' in args.port:
    try:
        start_port, end_port = map(int, args.port.split('-'))
        if end_port > 65535:
            print("ERROR. Chosen port is above 65535!")
            exit()
        ports_to_scan = range(start_port, end_port + 1)
    except ValueError:
        print("ERROR. Invalid port number")
        exit()
else:
    try:
        if int(args.port) > 65535:
            print("ERROR. Port above 65535")
            exit()
        ports_to_scan = [int(args.port)]
    except ValueError:
        print("ERROR. Port has to be an integer")
        exit()

# assign -ip arg to variable "HOST".
HOST = args.ip

# function connecting to host, returning True if connection is successful, otherwise return False
def scan(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.001)
        s.connect((host, port))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False

# scanning defined port or ports
for port in ports_to_scan:
    if scan(HOST, port):
        print('Port ' + str(port) + ' is open')