print("""Witamy w naszym kantorze. Obsługiwane waluty:
   - EUR
   - USD
   - CHF""")

kursy_walut = {
    "EUR": 4.27,
    "USD": 3.87,
    "CHF": 3.88
}

wartosc_portfela_PLN = 0
wartosc_portfela_EUR = 0
wartosc_portfela_USD = 0
wartosc_portfela_USD = 0
lista_transakcji = {}

while True:
    waluta = input("Podaj walutę (EUR/USD/CHF) lub wpisz 'koniec' aby podsumować transakcję:")
    if waluta.lower() == 'koniec':
        print(f"Należność za transakcje: {wartosc_portfela_PLN} PLN")
        print(f"Kupiłeś następujące waluty:", lista_transakcji)
        break
    action = input("Czy chcesz dokonać kupna, czy sprzedaży waluty? [k/s]")
    ilosc = float(input("Ile chcesz na to przeznaczyć środków?"))
    if waluta == 'EUR':
        if action == 'k':
            kupno_EUR = ilosc / kursy_walut[waluta]
            wartosc_portfela_EUR += round(kupno_EUR, 2)
            wartosc_portfela_PLN += ilosc
            lista_transakcji[waluta] = wartosc_portfela_EUR
        if action == 's':
            sprzedaz_EUR = kursy_walut[waluta] * ilosc
            wartosc_portfela_EUR -= ilosc
            wartosc_portfela_PLN -= round(sprzedaz_EUR, 2)
            lista_transakcji[waluta] = wartosc_portfela_EUR
    elif waluta == 'USD':
        if action == 'k':
            kupno_USD = ilosc / kursy_walut[waluta]
            wartosc_portfela_USD += round(kupno_USD, 2)
            wartosc_portfela_PLN += ilosc
            lista_transakcji[waluta] = wartosc_portfela_USD
        if action == 's':
            sprzedaz_USD = kursy_walut[waluta] * ilosc
            wartosc_portfela_USD -= ilosc
            wartosc_portfela_PLN -= round(sprzedaz_USD, 2)
            lista_transakcji[waluta] = wartosc_portfela_USD
    elif waluta == 'CHF':
        if action == 'k':
            kupno_CHF = ilosc / kursy_walut[waluta]
            wartosc_portfela_CHF += round(kupno_CHF, 2)
            wartosc_portfela_PLN += ilosc
            lista_transakcji[waluta] = wartosc_portfela_USD
        if action == 's':
            sprzedaz_CHF = kursy_walut[waluta] * ilosc
            wartosc_portfela_CHF -= ilosc
            wartosc_portfela_PLN -= round(sprzedaz_CHF, 2)
            lista_transakcji[waluta] = wartosc_portfela_USD
    else:
        print("Brak waluty w kantorze.")