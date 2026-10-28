import socket, random, string, re, base64

def banner():
    print("""

  JOHN TOOLKIT v1.0 - White Hat
  The Ethical Hacker

""")

def gen_pass():
    chars = string.ascii_letters + string.digits + "!@#$%"
    pw = ''.join(random.choice(chars) for _ in range(12))
    print(f"\n✅ Strong Password: {pw}")

def encrypt():
    text = input("Enter text: ")
    enc = base64.b64encode(text.encode()).decode()
    print(f"Encrypted: {enc}")

def decrypt():
    code = input("Enter code: ")
    try:
        dec = base64.b64decode(code).decode()
        print(f"Original: {dec}")
    except:
        print("Invalid code!")

def get_ip():
    site = input("Enter site: ")
    try:
        ip = socket.gethostbyname(site)
        print(f"IP {site} = {ip}")
    except:
        print("Invalid name")

def port_scan():
    target = input("Enter IP: ")
    print(f"Scanning {target}...")
    for port in [21,22,80,443,8080]:
        s=socket.socket(); s.settimeout(0.5)
        if s.connect_ex((target,port))==0:
            print(f"✅ Port {port} OPEN")
        else:
            print(f"❌ Port {port} closed")
        s.close()

def link_check():
    url=input("Enter link: ")
    danger=0
    if "@" in url: print("🚩 contains @"); danger+=1
    if "http://" in url: print("🚩 http not https"); danger+=1
    for w in ["login","free","gift","verify"]:
        if w in url.lower(): print(f"🚩 suspicious word {w}"); danger+=1
    if danger==0: print("✅ Clean")
    else: print(f"❌ Danger {danger}/4 - Don't click!")

def pass_check():
    pw=input("Enter password: ")
    score=0
    if len(pw)>=8: score+=1
    if len(pw)>=12: score+=1
    if re.search(r"[A-Z]",pw): score+=1
    if re.search(r"[0-9]",pw): score+=1
    if re.search(r"[!@#$%^&*]",pw): score+=1
    print(f"Score {score}/5 - ", end="")
    if score<=2: print("WEAK!")
    elif score==3: print("Medium")
    else: print("STRONG!")

while True:
    banner()
    print("1- Gen Password\n2- Encrypt\n3- Decrypt\n4- Get IP\n5- Scan Ports\n6- Check Link\n7- Check Password\n0- Exit")
    ch=input("\nChoose: ")
    if ch=="1": gen_pass()
    elif ch=="2": encrypt()
    elif ch=="3": decrypt()
    elif ch=="4": get_ip()
    elif ch=="5": port_scan()
    elif ch=="6": link_check()
    elif ch=="7": pass_check()
    elif ch=="0": break
    else: print("Invalid")
    input("\nPress Enter...")
