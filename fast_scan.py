import socket

print("--- Fast Scanner V2 - Akwa ---")

for i in range(1, 21):
    ip = f"192.168.1.{i}"
    for port in [80, 443, 445, 8080, 1900]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        if s.connect_ex((ip, port)) == 0:
            print(f"✅ L2et gehaz: {ip} - port {port} maftouh")
            break
        s.close()

print("\nKhalas scan!")
