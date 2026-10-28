import secrets, string
import arabic_reshaper

def ar(text):
    # ده بيعدل الحروف المقطعة
    return arabic_reshaper.reshape(text)[::-1]  # بنعكسها عشان Termux

chars = string.ascii_letters + string.digits + "@#$_!&"
p = ''.join(secrets.choice(chars) for _ in range(16))

print(ar("اداة تامين الحسابات"))
print(f"باسورد قوي: {p}")
print(ar("احفظ الباسورد ده"))
print("haveibeenpwned.com : افحص ايميلك من")

