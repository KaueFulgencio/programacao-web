import matplotlib.pyplot as plt

def criar_histograma(dados, titulo_grafico, titulo_eixo_x, titulo_eixo_y, nome_arquivo_saida, bins=10):
    if not dados:
        print("Erro: Não há dados para criar o gráfico.")
        return

    plt.figure(figsize=(10, 6))
    plt.hist(dados, bins=bins, edgecolor='k')

    plt.title(titulo_grafico)
    plt.xlabel(titulo_eixo_x)
    plt.ylabel(titulo_eixo_y)
    plt.grid(True)

    plt.savefig(f'saida/{nome_arquivo_saida}.png')
    plt.show()

def cria_histograma_automatico():
    
    dados = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]
    titulo_grafico = "Gráfico de Histograma"
    titulo_eixo_x = "Valores"
    titulo_eixo_y = "Frequência"
    nome_arquivo_saida = "histograma_teste"
    
    criar_histograma(dados, titulo_grafico, titulo_eixo_x, titulo_eixo_y, nome_arquivo_saida, bins=5)