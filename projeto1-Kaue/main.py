import matplotlib.pyplot as plt

import read_arq_csv

import ger_grafico_linhas
import ger_histograma
import ger_grafico_dispersao

def main():

    while True:
        print('=============MENU===============')
        print('  ESCOLHA UMA DAS TRÊS OPÇÕES   ')
        print('1- Gráfico de linhas')
        print('2- Dispersão (Scatterplot)')
        print('3- Histograma')
        print('4- Sair do programa')
        print('===============================')
        print('Criar Grafico com parametros predefinidos')
        print('5- Grafico de Linhas')
        print('6- Dispersão (Scatterplot)')
        print('7- Histograma')
        escolha = int(input('Digite a opção (1 a 4):'))

        if escolha == 1:
            arquivo_csv = input("Digite o nome do arquivo CSV de entrada: ")
            titulos, dados = read_arq_csv.read_csv(arquivo_csv)
            if not dados:
                print("Erro: Não foi possível ler o arquivo CSV.")
                continue
            titulo_grafico = input("Digite o título do gráfico: ")
            titulo_eixo_x = titulos[0] if titulos else input("Digite o título do eixo X: ")
            titulo_eixo_y = input("Digite o título do eixo Y: ")
            nome_arquivo_saida = input("Digite o nome do arquivo de saída (sem extensão): ")
            ger_grafico_linhas.criar_grafico_de_linha(titulos, dados, titulo_grafico, titulo_eixo_x, titulo_eixo_y, nome_arquivo_saida)

        elif escolha == 2:
            arquivo_csv = input("Digite o nome do arquivo CSV de entrada: ")
            titulos, dados = read_arq_csv.read_csv(arquivo_csv)
            if not dados:
                print("Erro: Não foi possível ler o arquivo CSV.")
                continue
            
            titulo_grafico = input("Digite o título do gráfico: ")
            titulo_eixo_x = titulos[0] if titulos else input("Digite o título do eixo X: ")
            titulo_eixo_y = input("Digite o título do eixo Y: ")
            nome_arquivo_saida = input("Digite o nome do arquivo de saída (sem extensão): ")
            ger_grafico_dispersao.criar_grafico_de_dispersao(titulos, dados, titulo_grafico, titulo_eixo_x, titulo_eixo_y, nome_arquivo_saida)
            
        elif escolha == 3:
            arquivo_csv = input("Digite o nome do arquivo CSV de entrada: ")
            _, dados = read_arq_csv.read_csv(arquivo_csv, possui_titulos=False)
            if not dados:
                print("Erro: Não foi possível ler o arquivo CSV.")
                continue
            titulo_grafico = input("Digite o título do gráfico: ")
            titulo_eixo_x = input("Digite o título do eixo X: ")
            titulo_eixo_y = input("Digite o título do eixo Y: ")
            nome_arquivo_saida = input("Digite o nome do arquivo de saída (sem extensão): ")
            ger_histograma.criar_histograma(dados[0], titulo_grafico, titulo_eixo_x, titulo_eixo_y, nome_arquivo_saida)
            
        elif escolha == 4:
            print("Fechando.")
            break
        elif escolha == 5:
            ger_grafico_linhas.cria_automatico_linhas()
            break
        elif escolha == 6:
            ger_grafico_dispersao.cria_automatico_dispersao()
            break
        elif escolha == 7:
            ger_histograma.cria_histograma_automatico()
            break
        
        else:
            print("Coloque um numero entre 1 e 7")

if __name__ == "__main__":
    main()