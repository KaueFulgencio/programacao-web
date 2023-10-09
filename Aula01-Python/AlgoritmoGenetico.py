import random

# Parâmetros do algoritmo genético
tamanho_populacao = 100
taxa_mutacao = 0.1
numero_geracoes = 100

# Função de aptidão fictícia (minimizar a soma dos quadrados)
def funcao_aptidao(cromossomo):
    return sum(x**2 for x in cromossomo)

# Inicialização da população
populacao = [[random.uniform(-5, 5) for _ in range(5)] for _ in range(tamanho_populacao)]

# Loop principal do algoritmo genético
for geracao in range(numero_geracoes):
    # Avaliação da aptidão de cada indivíduo na população
    aptidoes = [funcao_aptidao(individuo) for individuo in populacao]

    # Seleção dos pais com base na aptidão
    pais = []
    for _ in range(tamanho_populacao):
        indice_pai1 = random.choices(range(tamanho_populacao), weights=[1 / (aptidao + 1) for aptidao in aptidoes])[0]
        indice_pai2 = random.choices(range(tamanho_populacao), weights=[1 / (aptidao + 1) for aptidao in aptidoes])[0]
        pai1 = populacao[indice_pai1]
        pai2 = populacao[indice_pai2]
        pais.append((pai1, pai2))

    # Cruzamento (crossover) para criar filhos
    filhos = []
    for pai1, pai2 in pais:
        ponto_corte = random.randint(0, len(pai1) - 1)
        filho = pai1[:ponto_corte] + pai2[ponto_corte:]
        filhos.append(filho)

    # Mutação em alguns dos filhos
    for i in range(len(filhos)):
        if random.random() < taxa_mutacao:
            gene_mutante = random.randint(0, len(filhos[i]) - 1)
            filhos[i][gene_mutante] = random.uniform(-5, 5)

    # Substituição da população pela nova geração (pais + filhos)
    populacao = filhos

# Encontrar o melhor indivíduo após todas as gerações
melhor_individuo = min(populacao, key=funcao_aptidao)
melhor_aptidao = funcao_aptidao(melhor_individuo)

print("Melhor solução encontrada:")
print("Cromossomo:", melhor_individuo)
print("Aptidão:", melhor_aptidao)
