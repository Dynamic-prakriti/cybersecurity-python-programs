import socket

def port_scan(target, ports):
    print(f"Scanning {target} for open ports...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# User Input
target_ip = input("Enter target IP or domain: ")
ports = input("Enter comma-separated ports to scan (e.g., 22,80,443): ")
ports = [int(port.strip()) for port in ports.split(",")]

# Run scanner
port_scan(target_ip, ports)




'''
Scans user-specified ports on a given target IP for open ports.

 Algorithm Steps:

Take user input for target IP/domain and port numbers.
Loop through each port:
Create a TCP socket connection.
Try to connect to the port (connect_ex()).
If successful, print "Port is open".
Close the socket after scanning.


'''