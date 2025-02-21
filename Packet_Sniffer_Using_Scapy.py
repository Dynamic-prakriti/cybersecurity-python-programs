from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

# Sniff packets
print("Sniffing network traffic... (Press Ctrl+C to stop)")
sniff(prn=packet_callback)


'''
A packet sniffer listens to network traffic and displays packet details.
It can be used for network monitoring, penetration testing, and malware analysis.


Algorithm:
Capture incoming network packets.
Extract source & destination IPs, protocol, and payload.
Display packet summary to the user.
'''