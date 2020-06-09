import urllib.request
from datetime import date, timedelta
import json


def exUSD(date_transaction):
    url = f'http://api.nbp.pl/api/exchangerates/rates/c/usd/{date_transaction}/?format=json'
    try:
        with urllib.request.urlopen(url) as r:
            data = r.read()
        exchange = json.loads(data)['rates'][0]
        print("USD/PLN exchange rate for this transaction:", exchange['bid'])
        exchange_rate = exchange['bid']
        print("Kurs z dnia:", exchange['effectiveDate'])
        exchange_date = exchange['effectiveDate']
    except urllib.error.HTTPError:
        exUSD(date_transaction - timedelta(days=1))


if __name__ == "__main__":
    exUSD(date.today())

#TODO: czy tu ma być zrzucanie zapytania do pliku?
