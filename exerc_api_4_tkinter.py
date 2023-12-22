import tkinter as tk
import requests
import json
#
def buscar_cep():
    cep1 = entry_cep_1.get()
    cep = cep1.strip()
    link = "https://viacep.com.br/ws/{}/json/".format(cep)
    requisicao = requests.get(link)
    print(requisicao)
    cep_dic = requisicao.json()
    print("Buscar CEP")
    print(cep_dic)
    if requisicao.status_code == 200:   
        rua = cep_dic['logradouro']
        entry_cep_2.delete(0, tk.END)
        entry_cep_2.insert(0,rua)
        bairro = cep_dic['bairro']
        entry_cep_3.delete(0, tk.END)
        entry_cep_3.insert(0,bairro)
        cidade = cep_dic['localidade']
        entry_cep_4.delete(0, tk.END)
        entry_cep_4.insert(0,cidade)
        estado = cep_dic['uf']
        entry_cep_5.delete(0, tk.END)
        entry_cep_5.insert(0,estado)
        ddd = cep_dic['ddd']
        entry_cep_6.delete(0, tk.END)
        entry_cep_6.insert(0,ddd)
    else:
        print("Erro ao buscar CEP. Status code:", requisicao.status_code)

# Criar a janela principal
root = tk.Tk()
#Configuração da tela principal
root.configure(bg="white")
root.title("API - Pesquisa de CEP")
root.geometry("500x300")
#Label da aplicação da tela principal
label_CEP_1 = tk.Label(root, text="CEP:", bg="white")
label_CEP_1.grid(row=0, column=0, padx=10, pady=10,sticky='NSEW')
label_CEP_2 = tk.Label(root, text="Rua:", bg="white")
label_CEP_2.grid(row=1, column=0, padx=10, pady=10,sticky='NSEW')
label_CEP_3 = tk.Label(root, text="Bairro:", bg="white")
label_CEP_3.grid(row=2, column=0, padx=10, pady=10,sticky='NSEW')
label_CEP_4 = tk.Label(root, text="Cidade:", bg="white")
label_CEP_4.grid(row=3, column=0, padx=10, pady=10,sticky='NSEW')
label_CEP_5 = tk.Label(root, text="Estado:", bg="white")
label_CEP_5.grid(row=4, column=0, padx=10, pady=10,sticky='NSEW')
label_CEP_6 = tk.Label(root, text="DDD:", bg="white")
label_CEP_6.grid(row=5, column=0, padx=10, pady=10,sticky='NSEW')
#Dados de entrada
entry_cep_1 = tk.Entry(root, width=10)
entry_cep_1.grid(row=0, column=1, padx=10, pady=10, sticky='NSEW')
entry_cep_2 = tk.Entry(root, width=10)
entry_cep_2.grid(row=1, column=1, padx=10, pady=10, sticky='NSEW', columnspan=3)
entry_cep_3 = tk.Entry(root, width=10)
entry_cep_3.grid(row=2, column=1, padx=10, pady=10, sticky='NSEW', columnspan=3)
entry_cep_4 = tk.Entry(root, width=10)
entry_cep_4.grid(row=3, column=1, padx=10, pady=10, sticky='NSEW', columnspan=3)
entry_cep_5 = tk.Entry(root, width=10)
entry_cep_5.grid(row=4, column=1, padx=10, pady=10, sticky='NSEW', columnspan=3)
entry_cep_6 = tk.Entry(root, width=10)
entry_cep_6.grid(row=5, column=1, padx=10, pady=10, sticky='NSEW', columnspan=3)
#Botao de busca do CEP
btn_busca_cep = tk.Button(root, text="Buscar Endereço", command=buscar_cep, border=0)
btn_busca_cep.grid(row=0, column=2, padx=10, pady=10, sticky='NSEW', columnspan=1)
# Iniciar o loop principal
root.mainloop()