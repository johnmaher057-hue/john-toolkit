import socket

target = input("Hat el IP (142.251.142.78 bta3 google): ")
print(f"Bafhas {target} ...")

for port in [21, 22, 80, 443, 8080]:
    s = socket.socket()
    s.settimeout(1)
    if s.connect_ex((target, port)) == 0:
        print(f"✅ Port {port} MAFTUH")
    else:
        print(f"❌ Port {port} ma2foul")
    s.close()

print("\nKhalas! Law l2et 80 w 443 maftouhin yb2a da website 3adi")
