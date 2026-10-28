import socket
site = input("Hat esm el mawke3: ")
try:
    ip = socket.gethostbyname(site)
    print(f"El mawke3: {site}")
    print(f"El IP: {ip}")
except:
    print("Esm ghalat")
