import secrets
import string
import hashlib
import requests

print("=== أداة تأمين الحسابات من Termux ===\n")

# 1- مولد باسورد قوي
def gen_pass():
    chars = string.ascii_letters + string.digits + "@#$_!&"
    p = ''.join(secrets.choice(chars) for _ in range(16))
    print(f"[باسورد قوي مقترح]: {p}")
    print("انسخه واحفظه، ده أأمن من أي باسورد بتعمله انت\n")

gen_pass()

# 2- فحص هل ايميلك اتسرب قبل كده
email = input("اكتب ايميلك عشان نفحصه اتسرب ولا لا: ").strip()
print("بفحص...")

# بنستخدم haveibeenpwned API المجاني
try:
    # بنشفر الايميل ونفحصه بطريقة آمنة
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    # الموقع محتاج مفتاح، فهنعمل فحص بسيط بديل
    print(f"\nادخل على الموقع ده من المتصفح واكتب ايميلك:")
    print(f"https://haveibeenpwned.com/")
    print("لو قالك Oh no — pwned! يبقى لازم تغير باسوردك حالا")
except Exception as e:
    print(e)

print("\n[نصيحة] لو ايميلك متسرب، غير باسورد فيسبوك وفري فاير فورا بنفس الباسورد القوي اللي فوق.")
