from collections import Counter

vendas_tecnologia = {'Notebook Asus':20450, 'Iphone': 15000, 'Samsung Galaxy': 12000, 'Tv Samsung': 10000, 'PS5': 14300, 'Tablet Samsung': 20000}

aux = Counter(vendas_tecnologia)

print(aux.most_common(2))
