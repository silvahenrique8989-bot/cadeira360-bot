import requests

url = "https://api.mercadolibre.com/sites/MLB/search?q=Safety%201st%20i-NXT%20360"

resposta = requests.get(url)

dados = resposta.json()

for item in dados["results"][:5]:
    print(item["title"])
    print(item["price"])
    print(item["permalink"])
    print("----------------")
