import socket

site = input("Enter site: ")
ip = socket.gethostbyname(site)
print(f"IP of {site} is {ip}")
print("Scanning ports...")

for port in [21, 22, 80, 443, 8080]:
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is closed")
    s.close()
