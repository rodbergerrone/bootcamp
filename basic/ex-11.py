x = int(input("Podaj pozycję gracza X w przedziale od 0 do 100: "))
y = int(input("Podaj pozycję gracza Y w przedziale od 0 do 100: "))

if x < 0 or x > 100 or y < 0 or y > 110:
    print("Nie ma ciebie na planszy.")
elif x < 10 and y < 10:
    print("Jesteś w lewym dolnym rogu.")
elif 90 >= x >= 10 and y <= 10:
    print("Jesteś na dolnej krawędzi.")
elif x < 10 and y > 90:
    print("Jesteś w lewym górnym rogu.")
elif 90 >= x >= 10 and y >= 90:
    print("Jesteś na górnej krawędzi.")
elif x > 90 and y < 10:
    print("Jesteś w prawym dolnym rogu.")
elif x <= 10 and y >= 10 and y <= 90:
    print("Jesteś na lewej krawędzi.")
elif x > 90 and y > 90:
    print("Jesteś w prawym górnym rogu.")
elif x >= 90 and y >= 10 and y <= 90:
    print("Jesteś na prawej krawędzi.")
else:
    print("Jesteś w środku planszy.")