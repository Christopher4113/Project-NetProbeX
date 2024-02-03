import pyshark

def packet_callback(pkt):
    # Check if the packet contains email-related information
    if 'smtp' in str(pkt) or 'pop' in str(pkt) or 'imap' in str(pkt):
        print("Email-related packet found:")
        print(pkt)

# Specify the path to your packet capture file
file_path = r'Project-NetProbeX/links.pcapng'

# Open the file and set a callback function to be called for each packet
capture = pyshark.FileCapture(file_path)
capture.apply_on_packets(packet_callback)



