import secrets, string

def strong_pass():
    chars = string.ascii_letters + string.digits + "@#$!&"
    return ''.join(secrets.choice(chars) for _ in range(16))

p = strong_pass()
print("--- ADAT TAMEN ---")
print(f"Password: {p}")
print("------------------")
print("1. Khod el password da")
print("2. Ro7 ghayar beh Facebook + Gmail")
print("3. Check email: haveibeenpwned.com")
print("4. Shaghal 2FA mn el settings")

