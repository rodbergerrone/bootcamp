import urllib.request
import json


def main():
    lokalizacja = input("Podaj lokalizacje: ")
    url = 'https://www.metaweather.com/api/api/location/search/?query=' + lokalizacja
    with urllib.request.urlopen(url) as r:
        data = r.read()

    found_location = json.loads(data)
    if not found_location:
        print("Nie znaleziono takiej lokalizacji")
        return
    woeid = found_location[0]["woeid"]
    url = f"https://www.metaweather.com/api/location/{woeid}/"
    with urllib.request.urlopen(url) as r:
        data = r.read()

    weather_today = json.loads(data)["consolidated_weather"][0]
    print("Temperatura:", weather_today["the_temp"], "C")
    print("Wiatr:", round(weather_today["wind_speed"] * 1.6, 2), "km/h")


if __name__ == "__main__":
    main()