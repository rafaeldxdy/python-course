import socket
import pyperclip

def get_local_ipv4():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

local_ip = get_local_ipv4()

# Copy to clipboard
pyperclip.copy(local_ip)

print(f"Local IPv4 Address ({local_ip}) copied to clipboard!")
