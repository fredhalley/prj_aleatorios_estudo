import requests
import json

moeda = 'USD-BRL'
cotacoes = requests.get('https://economia.awesomeapi.com.br/last/{}' .format(moeda))
cotacoes_dic = cotacoes.json()
moeda_alt = moeda.replace("-", "")
print(moeda_alt)
print(cotacoes_dic[moeda_alt]['bid'])
