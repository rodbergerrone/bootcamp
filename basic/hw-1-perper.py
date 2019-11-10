import datetime
x = datetime.datetime.now()
dob = int(input("Podaj rok urodzenia postaci (przed 1960 r.): "))
dob2 = x.year - dob
print(f"Ta osoba urodziła się przed {dob2} laty.")
dob3 = "pra" * (dob2 // 29 - 2)
if dob2 < 60:
    print("Postać zbyt młoda.")
else:
    print(f"To mogła być Twoja {dob3}babka.")