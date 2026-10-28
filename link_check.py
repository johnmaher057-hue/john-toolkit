def check_link(url):
    print(f"\nBafhas: {url}\n")
    danger = 0
    
    if "@" in url: 
        print("🚩 خطر: فيه @ في اللينك - ده حركة هاكرز!")
        danger+=1
    if url.count(".") > 3:
        print("🚩 خطر: نقط كتير - ممكن يكون موقع مزيف")
        danger+=1
    if "http://" in url:
        print("🚩 خطر: مش مؤمن https - ممكن يسرق بياناتك")
        danger+=1
    
    bad_words = ["login", "verify", "free", "gift", "urgent"]
    for w in bad_words:
        if w in url.lower():
            print(f"🚩 انتبه: فيه كلمة مشبوهة '{w}'")
            danger+=1
            
    if danger == 0:
        print("✅ اللينك شكله نضيف")
    elif danger < 2:
        print("\n⚠️ متوسط الخطورة - متدوسش الا لو واثق")
    else:
        print("\n❌ خطر عالي جدا - اوعى تدوس عليه!")

link = input("Hat el link el mashbouh: ")
check_link(link)
