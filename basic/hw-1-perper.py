# Zadanie domowe 3 - wyzwanie dla chętnych:
# Genealogia. Napisz program pomagający oszacować ile pokoleń różni użytkownika od znanych postaci historycznych. Program pyta użytkownika o rok urodzenia się postaci, a następnie drukuje informacje: ile lat temu urodziła się ta postać i relację - kim ta osoba mogłaby być dla użytkownika (np. prababką). Można zapisać aktualny rok (2019) w kodzie programu, nie trzeba go znikąd pobierać. Zakładamy, średnią różnicę między pokoleniami 30 lat - tzn, że średnio przez wieki ludzie mieli dzieci w wieku 30 lat. To daje następujące relacje:
# Postać urodzona 60-89 lat temu: babka
# Postać urodzona 90-119 lat temu: prababka
# Postać urodzona 120-149 lat temu: praprababka
# itd.
# Program nie musi obsługiwać lat od 1960 wzwyż (czyli postaci urodzonych mniej niż 60 lat temu).


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