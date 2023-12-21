import requests
import json
import matplotlib.pyplot as plt

moeda = 'USD-BRL'
numero_dias = 30
cotacoes = requests.get('https://economia.awesomeapi.com.br/json/daily/{}/{}' .format(moeda, numero_dias))
cotacoes_dic = cotacoes.json()
#moeda_alt = moeda.replace("-", "")
#print(cotacoes_dic)
#print(cotacoes_dic[moeda_alt]['bid'])
lista_cotacao_dolar = [float(item['bid']) for item in cotacoes_dic]
print(lista_cotacao_dolar)

plt.figure(figsize=(15, 5))
plt.plot(lista_cotacao_dolar)
plt.show()