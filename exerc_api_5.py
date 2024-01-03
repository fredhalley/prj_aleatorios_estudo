import requests
import pprint

link = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/aplicacao#!/"

requisicao = requests.get(link)

informacoes = requisicao.json()

#print(informacoes)

pprint.pprint(informacoes)