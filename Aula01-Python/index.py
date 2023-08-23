#Primeiro codigo em python

#nomepessoa=input('O nome:')
#verbo=input('Digite o Verbo:')
#numero=input('Digite o Numero:')
#objeto=input('Digite o Objeto:')

#print(f'{nomepessoa} {verbo} {numero} {objeto}')

#numero=int(input("Digite o Numero: "))
#if numero % 2 == 0:
#    print('é par')
#else:
#    print('é impar')

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