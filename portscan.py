import socket
from termcolor import colored

print(colored("scanning port with python", "blue"))
print(colored("port ex: '20' '20-40' or '20,21,24'", "blue"))


def scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        serviceversion = sock.recv(1024)
        serviceversion = serviceversion.decode("utf-8")
        serviceversion = serviceversion.strip("\n")
        portstate = f"Port {str(port)} is open"
        print(colored(portstate, "yellow"), end="   ")
        print(colored(serviceversion, "yellow"))
    except ConnectionRefusedError:
        print(colored(f"Port {str(port)} is closed", "red"))
    except UnicodeDecodeError:
        print(colored(f"Port {str(port)} is open", "yellow"))


ip_target = input(colored("IP Address: ", "green"))
ports = input(colored("Port: ", "green"))

if "," in ports:
    portlist = ports.split(",")
    for port in portlist:
        scan(ip_target, int(port))
elif "-" in ports:
    portrange = ports.split("-")
    start = int(portrange[0])
    end = int(portrange[1])
    for port in range(start, end + 1):
        scan(ip_target, int(port))
else:
    scan(ip_target, int(ports))
