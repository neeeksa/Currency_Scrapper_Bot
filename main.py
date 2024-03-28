import requests
import json


def main_collector(city="dnepropetrovsk"):
    def collect_and_parse_currency_data(city):
        base_url = f'https://minfin.com.ua/api/currency/simple/?base=UAH&list=usd,eur,pln,gbp,chf&city={city}'
        try:
            response = requests.get(base_url)
            if response.status_code == 200:
                currency_data = response.json()
                parsed_data = parse_currency_data(currency_data, city)
                return parsed_data
            else:
                print(f"Ошибка при получении данных: {response.status_code}")
                return None
        except Exception as e:
            print(f"Ошибка: {e}")
            return None

    def parse_currency_data(currency_data, city):
        result = []
        try:
            data = currency_data.get('data', {})
            count = 0
            for currency, details in data.items():
                if currency == 'UAH':
                    continue  # Пропускаем валюту UAH
                buy_price = details.get('midbank', {}).get('buy', {}).get('val')
                sell_price = details.get('midbank', {}).get('sell', {}).get('val')
                if buy_price is not None and sell_price is not None:
                    buy_price = round(float(buy_price), 3)  # Округляем до трех знаков после запятой
                    sell_price = round(float(sell_price), 3)  # Округляем до трех знаков после запятой
                    result.append({
                        'city': city.capitalize(),
                        'currency': currency.upper(),
                        'buy_price': buy_price,
                        'sell_price': sell_price
                    })
                    count += 1
                    if count >= 2:
                        break
        except Exception as e:
            print(f"Ошибка при обработке данных: {e}")
        return result

    parsed_data = collect_and_parse_currency_data(city)
    return parsed_data


if __name__ == '__main__':
    data = main_collector()
    print(data)
