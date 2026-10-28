import socket
import requests

site = input("Enter site (ex: google.com): ").strip()
if site.startswith("http"):
    site = site.replace("https://","").replace("http://","").split("/")[0]

print(f"\n--- Info for {site} ---\n")

# 1- ال IP
try:
    ip = socket.gethostbyname(site)
    print(f"[IP] {ip}")
except Exception as e:
    print(f"[IP] Error: {e}")
    ip = None

# 2- ال Header بتاع السيرفر
try:
    r = requests.get(f"https://{site}", timeout=5)
    print(f"[Status] {r.status_code}")
    print(f"[Server] {r.headers.get('Server', 'Not found')}")
    print(f"[Powered] {r.headers.get('X-Powered-By', 'Not found')}")
    print(f"\n[All Headers]:")
    for k,v in r.headers.items():
        print(f"  {k}: {v}")
except Exception as e:
    print(f"[HTTP] Error: {e}")

print("\n[ DONE ]")
