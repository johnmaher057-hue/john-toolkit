import secrets

words = ["Zagazig", "Mody", "Tiger", "Nile", "Ahly", "Zamalek", "Cairo", "Mango"]
symbols = ["@", "#", "$", "!"]

w1 = secrets.choice(words)
w2 = secrets.choice(words)
num = secrets.randbelow(90) + 10  # رقمين
sym = secrets.choice(symbols)

password = f"{w1}{sym}{w2}{num}"
print(f"Password Sahl: {password}")
print(f"Example: Zagazig@Mody26")
print("Sahl tktbo w qawy gdn!")
