import requests
import json

cep = "74023030"

link = "https://viacep.com.br/ws/{}/json/".format(cep)

requisicao = requests.get(link)

cep_dic = requisicao.json()

print(cep_dic['uf'])