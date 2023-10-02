import matplotlib.pyplot as plt

def criar_grafico_de_dispersao(titulos, dados, titulo_grafico, titulo_eixo_x, titulo_eixo_y, nome_arquivo_saida):
    if not dados:
        print("Erro: Não há dados para criar o gráfico.")
        return

    plt.figure(figsize=(10, 6))
    for i, coluna in enumerate(dados):
        if 0 <= i < len(coluna):
            plt.scatter(range(len(coluna)), coluna, label=titulos[i] if titulos else f'Coluna {i+1}', alpha=0.7)

    plt.title(titulo_grafico)
    plt.xlabel(titulo_eixo_x)
    plt.ylabel(titulo_eixo_y)
    plt.legend()
    plt.grid(True)

    plt.savefig(f'saida/{nome_arquivo_saida}.png')
    plt.show()

def cria_automatico_dispersao():
    titulos = ["x", "y"]  
    dados = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
        [3.5, 2.0, 4.2, 1.8, 2.5, 3.0, 2.7, 4.5, 3.8, 2.1]  
    ]

    titulo_grafico = "Gráfico de Dispersão"
    titulo_eixo_x = "Valores de x"
    titulo_eixo_y = "Valores de y"
    nome_arquivo_saida = "scatterplot_predefinido"

    criar_grafico_de_dispersao(titulos, dados, titulo_grafico, titulo_eixo_x, titulo_eixo_y, nome_arquivo_saida)