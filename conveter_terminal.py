import requests

endpoint = "https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey="

currency_from = input("From: ")

currency_to = input("To: ")

get_request  = requests.get(endpoint.format(currency_from, currency_to))

print(round(get_request.json()["rate"], 2))