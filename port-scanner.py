import socket

target = input("Enter IP or site: ").strip()
try:
    target_ip = socket.gethostbyname(target)
except:
    target_ip = target

print(f"\nScanning {target} ({target_ip})...\n")

ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 8080]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target_ip, port))
    
    if result == 0:
        print(f"[OPEN] Port {port} is OPEN")
    else:
        print(f"[CLOSED] Port {port}")
    
    s.close()

print("\n[ DONE ] Scan finished!")
