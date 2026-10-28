import whois

site = input("Enter site: ")
info = whois.whois(site)

print("\n--- WHOIS INFO ---")
print(f"Domain: {info.domain_name}")
print(f"Registrar: {info.registrar}")
print(f"Creation: {info.creation_date}")

