import json
# import os # alternatywnie


def main():
    # if os.path.exists('employees.json'): # alternatywnie
    try:
        with open('employees.json') as f:
            employees = json.load(f)
    except json.decoder.JSONDecodeError:
        employees = []
    except FileNotFoundError:
        employees = []

    action = input("Co chcesz zrobić? [d - dodaj, w - wypisz]")
    if action == 'd':
        imie = input("Imię:")
        nazwisko = input("Nazwisko:")
        rok_ur = int(input("Rok urodzenia:"))
        pensja = float(input("Pensja:"))
        employee = {
            'imie': imie,
            'nazwisko': nazwisko,
            'rok_ur': rok_ur,
            'pensja': pensja
        }
        employees.append(employee)
        with open('employees.json', 'w') as f:
            json.dump(employee, f)
    elif action == 'w':
        for numer, employee in enumerate(employees):
            print(f"  - [{numer+1}] {employee['imie']} {employee['nazwisko']} - rocznik: {employee['rok_ur']}, pensja: {employee['pensja']}")


if __name__ == "__main__":
    main()

# TODO: import z gita