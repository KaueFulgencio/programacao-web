import csv

def read_csv(arquivo, possui_titulos=True):
    with open(arquivo, newline='') as file:
        leitor_csv = csv.reader(file)
        dados = [linha for linha in leitor_csv]
    
    if possui_titulos:
        titulos = dados[0]
        dados = dados[1:]
        return titulos, dados
    else:
        return None, dados
