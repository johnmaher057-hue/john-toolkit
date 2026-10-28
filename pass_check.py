import re

pw = input("Hat el password el 3ayz tefhaso: ")

score = 0
if len(pw) >= 8: score+=1
if len(pw) >= 12: score+=1
if re.search(r"[A-Z]", pw): score+=1
if re.search(r"[0-9]", pw): score+=1
if re.search(r"[!@#$%^&*]", pw): score+=1

print("\n--- El Nateega ---")
if score <=2:
    print(f"❌ DA3EEF GEDAN! Score {score}/5 - Haker hayfeko fi saney")
    print("Haker momken yegiboo be Brute Force fi < 1 hour")
elif score == 3:
    print(f"⚠️ MOTAWASET Score {score}/5 - momken yetfek")
else:
    print(f"✅ GAAMED Score {score}/5 - hayakhod 100s seneen 3ashan yetfek!")

common = ["123456", "password", "ahmed", "cairo", "123456789"]
if pw.lower() in common or len(pw) < 6:
    print("🚨 Dah mn aktar 10 passwords mashhoura! Kol el hackers 3arfeno!")

print("------------------")
