import urllib.request
import requests
from datetime import date, timedelta
import json


def exUSD(date_transaction):
    url = f'http://api.nbp.pl/api/exchangerates/rates/c/usd/{date_transaction}/?format=json'
    try:
        with urllib.request.urlopen(url) as r:
            data = r.read()
        exchange = json.loads(data)['rates'][0]
        exchange_rate = exchange['bid']
        exchange_date = exchange['effectiveDate']
        print(exchange_rate)
    except urllib.error.HTTPError:
        exUSD(date_transaction - timedelta(days=1))


def get_BTCEUR_rate(date_transaction):
    url = "https://api.bitbay.net/rest/trading/orderbook/BTC-EUR"
    headers = {'content-type': 'application/json'}

    response = requests.request("GET", url, headers=headers)
    response2 = response.json()

    print(response2["buy"][0]['ra'])


if __name__ == "__main__":
    exUSD(date.today())
    get_BTCEUR_rate(date.today())


#TODO: czy tu ma być zrzucanie zapytania do pliku?
