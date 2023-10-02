import matplotlib.pyplot as plt

def criar_grafico_de_linha(titulos, dados, titulo_grafico, titulo_eixo_x, titulo_eixo_y, nome_arquivo_saida):
    if not dados:
        print("Erro: Não há dados para criar o gráfico.")
        return

    plt.figure(figsize=(10, 6))

    for i, coluna in enumerate(dados):
        plt.plot(coluna, label=f'Coluna {i+1}')

    plt.title(titulo_grafico)
    plt.xlabel(titulo_eixo_x)
    plt.ylabel(titulo_eixo_y)
    plt.legend(title='Legendas')
    plt.grid(True)

    plt.savefig(f'saida/{nome_arquivo_saida}.png')
    plt.show()
