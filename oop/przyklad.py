class SwietyMikolaj:
    def __init__(self, imie = "Mikołaj"):
        self.imie = imie

    def przywitaj_sie(self):
        print(f"Ho ho ho! Jestem {self.imie}")

    def daj_prezent(self, dla_kogo):
        return f"Prezent dla {dla_kogo}"

mikolaj1 = SwietyMikolaj()
mikolaj1.imie = "Mikołajek"
print("Ten Święty Mikołaj nazywa się:", mikolaj1.imie)
inni_mikolaje = [SwietyMikolaj("Andrzej"), SwietyMikolaj("Maniek"), SwietyMikolaj()]

mikolaj1.przywitaj_sie()
for mikolaj in inni_mikolaje:
    mikolaj.przywitaj_sie()

print(mikolaj1.daj_prezent("Agaty"))