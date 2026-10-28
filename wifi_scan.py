import os

print("--- WiFi Scanner - Shabaktek Enta Bs ---")
print("Bndawwar 3ala el agheza...")

# هيجيب الـ IP بتاعك
os.system("ip route | grep src")

print("\nKatab el rakam da, masalan: 192.168.1.0/24")
target = input("Hat el network (masalan 192.168.1.0/24): ")

print(f"\nBiscan {target} ... estana 10s")
os.system(f"nmap -sn {target}")
print("\n--- Khalas! Kol IP zahar fo2 da gehaz motasel ---")
