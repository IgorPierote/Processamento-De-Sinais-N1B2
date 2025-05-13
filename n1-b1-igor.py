import matplotlib.pyplot as plt
import numpy as np
import re

def exibir_sinal_discreto(amostras, titulo='Exemplo: Sinal Discreto', rotulo_x='n (índice)', rotulo_y='Valor'):
    """
    Exibe um gráfico stem de um sinal discreto.
    
    Parâmetros:
    amostras (list ou np.array): Valores do sinal
    titulo (str): Título do gráfico
    rotulo_x (str): Nome do eixo x
    rotulo_y (str): Nome do eixo y
    """
    n = np.arange(len(amostras))
    
    plt.figure(figsize=(10, 4))
    linhas, marcadores, _ = plt.stem(n, amostras, linefmt='b', markerfmt='bo', basefmt=" ")
    plt.setp(linhas, linewidth=1.2)
    plt.setp(marcadores, markersize=5)
    
    plt.title(titulo, fontsize=13)
    plt.xlabel(rotulo_x)
    plt.ylabel(rotulo_y)
    plt.xticks(n)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.tight_layout()
    plt.show()


def transformar_e_plotar(amostras):
    """
    Aplica transformações típicas de tempo em um sinal discreto:
    - Atraso de 2 unidades
    - Reflexão temporal
    - Compressão por 2
    """
    amostras = np.array(amostras)
    n = np.arange(len(amostras))
    
    atrasado = np.roll(amostras, 2)
    atrasado[:2] = 0
    
    reflexo = amostras[::-1]
    
    comprimido = amostras[::2]
    n_comprimido = np.arange(len(comprimido))
    
    plt.figure(figsize=(14, 8))
    
    plt.subplot(2, 2, 1)
    plt.stem(n, amostras, linefmt='b', markerfmt='bo', basefmt=" ")
    plt.title("Original $x[n]$")
    plt.grid(True, linestyle=':', alpha=0.7)
    
    plt.subplot(2, 2, 2)
    plt.stem(n, atrasado, linefmt='g', markerfmt='go', basefmt=" ")
    plt.title("Atraso de 2: $x[n-2]$")
    plt.grid(True, linestyle=':', alpha=0.7)

    plt.subplot(2, 2, 3)
    plt.stem(n, reflexo, linefmt='r', markerfmt='ro', basefmt=" ")
    plt.title("Reflexão: $x[-n]$")
    plt.grid(True, linestyle=':', alpha=0.7)

    plt.subplot(2, 2, 4)
    plt.stem(n_comprimido, comprimido, linefmt='m', markerfmt='mo', basefmt=" ")
    plt.title("Compressão: $x[2n]$")
    plt.grid(True, linestyle=':', alpha=0.7)
    
    plt.tight_layout()
    plt.show()


def avaliar_sistema(expressao):
    """
    Avalia um sistema baseado na sua equação de entrada.
    
    Retorna:
    - tipo de memória (estático ou dinâmico)
    - causalidade
    - invariância temporal
    """
    padrao = r'(x|y)\[n([+-]\d+)?\]'
    encontrados = re.findall(padrao, expressao)
    
    possui_memoria = any(shift for _, shift in encontrados)
    memoria_tipo = "dinâmico (com memória)" if possui_memoria else "estático (sem memória)"
    
    causal = all(not shift or '-' in shift or shift == '' for _, shift in encontrados)
    causalidade = "causal" if causal else "não causal"
    
    if re.search(r'(x|y)\[[^\]]*(\d+\s*\*\s*n|n\s*[\*/^])', expressao):
        invariancia = "variante no tempo"
    else:
        invariancia = "invariante no tempo"
    
    return memoria_tipo, causalidade, invariancia


# Execução do script
sinal = [0, -2, -1, 0, 1, 2, 3, 0, 0]

exibir_sinal_discreto(sinal)
transformar_e_plotar(sinal)

entrada_usuario = input("Digite a equação do sistema (ex: y[n] = x[n] - x[n-2]): ")
tipo_memoria, tipo_causalidade, tipo_invariancia = avaliar_sistema(entrada_usuario)

print(f"\nAnálise do Sistema:")
print(f"- Memória: {tipo_memoria}")
print(f"- Causalidade: {tipo_causalidade}")
print(f"- Invariância no tempo: {tipo_invariancia}")