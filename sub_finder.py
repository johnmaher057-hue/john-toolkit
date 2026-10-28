import socket

site = input("Enter site (ex: google.com): ")
subdomains = ["www", "mail", "ftp", "admin", "test", "dev", "api", "blog", "shop"]

print(f"\nSearching subdomains for {site}...\n")

for sub in subdomains:
    full = f"{sub}.{site}"
    try:
        ip = socket.gethostbyname(full)
        print(f"[FOUND] {full} -> {ip}")
    except:
        print(f"[NOT FOUND] {full}")
