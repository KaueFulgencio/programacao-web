#Input em python
def pessoa():
    nomepessoa=input('O nome:')
    verbo=input('Digite o Verbo:')
    numero=input('Digite o Numero:')
    objeto=input('Digite o Objeto:')
    print(f'{nomepessoa} {verbo} {numero} {objeto}')

#Estruturas de decisão
def impar_ou_par():
    numero=int(input("Digite o Numero: "))
    if numero % 2 == 0:
        print('é par')
    else:
        print('é impar')

def despertador():
    hora=int(input("Digite as Horas: "))
    if hora >= 6 and hora <= 12:
        print('Bom dia!')
    elif hora >= 13 and hora <= 18:
        print('Boa Tarde!')
    elif hora >= 19 and hora <= 24:
        print('Boa noite!')
    elif hora >= 0 and hora <= 5:
        print('Bom sono!')
    else: 
        print('Digite um valor entre 0 e 24!')

def calcula_ano_bissexto(ano):
    if ano % 400 == 0:
        print(ano, 'é bissexto')
        return True
    elif ano % 100 == 0:
        print(ano, 'não é bissexto')
        return False
    elif ano % 4 == 0:
        print(ano, 'é bissexto')
        return True
    else:
        print(ano, 'não é bissexto')
        return False 
    

def data():
    mes=int(input("Digite o mes: "))
    ano=int(input("Digite o ano: "))
    if mes == 1 or mes == 3 or mes == 5 or mes == 6 or mes == 8 or mes == 10 or mes == 12:
        print("O mes", mes, 'possui 31 dias')
    elif mes == 4 or mes == 7 or mes == 9 or mes == 11:
        print("O mes", mes, 'possui 30 dias ')
    elif mes == 2:
        if calcula_ano_bissexto(ano):
            print("O mes", mes, 'tem 29 dias')
        else:
            print("O mes", mes, 'tem 28 dias')
    else:
        print('Selecione um mes de 0 a 12')          

data()