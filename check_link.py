link = input("Hat el link hna: ").lower()

khatar = ["free", "gift", "login-verify", "faceb00k", "gooogle", "bit.ly", "tinyurl", "verify-account"]

print("------------------")
if "facebook-free" in link or "google-free" in link or "free-fire" in link:
    print("⚠️  KHATAR! Facebook/Google 3omro ma by2ol free - da nasb!")
elif any(w in link for w in khatar):
    print("⚠️  KHATAR! Link mashboh, matftahosh!")
elif link.startswith("https://") and "." in link:
    print("✅ Aman - feh 2afl https")
else:
    print("⚠️ Link ghareb, et2aked meno")
print("------------------")
