import socket
import whois

site = input("Enter site: ").strip()
print(f"\n--- [1] IP Lookup for {site} ---")
try:
    ip = socket.gethostbyname(site)
    print(f"IP: {ip}")
except Exception as e:
    print(f"Error: {e}")

print(f"\n--- [2] WHOIS for {site} ---")
try:
    w = whois.whois(site)
    print(f"Domain: {w.domain_name}")
    print(f"Registrar: {w.registrar}")
    print(f"Creation: {w.creation_date}")
except Exception as e:
    print(f"Error: {e}")

print(f"\n--- [3] Subdomains for {site} ---")
subs = ["www", "mail", "ftp", "admin", "test", "dev", "api", "blog", "shop", "m", "store", "support"]
for sub in subs:
    full = f"{sub}.{site}"
    try:
        ip = socket.gethostbyname(full)
        print(f"[FOUND] {full} -> {ip}")
    except:
        pass

print("\n[ DONE ] Happy Hacking!")
