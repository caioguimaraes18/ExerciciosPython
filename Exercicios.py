# Exercicio 1 
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite 1, 2, 3 ou 4: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    print(num1, "+", num2, "=", adicao(num1, num2))

elif escolha == '2':
    print(num1, "-", num2, "=", subtracao(num1, num2))

elif escolha == '3':
    print(num1, "*", num2, "=", multiplicacao(num1, num2))

elif escolha == '4':
    print(num1, "/", num2, "=", divisao(num1, num2))

else:
    print("Opção inválida")

#------------------------------------------------------------------------------#
                  
def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  
    return True 

numero = int(input("Digite um número para verificar se é primo: "))

if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")  

#------------------------------------------------------------------------------#

def calcular_fatorial(numero):
    if numero < 0:
        return "Não é possível calcular o fatorial de um número negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

# Exemplo de uso da função
numero = int(input("Digite um número para calcular o fatorial: "))

resultado_fatorial = calcular_fatorial(numero)

if type(resultado_fatorial) == int:
    print(f"O fatorial de {numero} é {resultado_fatorial}.")
else:
    print(resultado_fatorial)

#------------------------------------------------------------------------------#

import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "openai", "inteligencia"]
    return random.choice(palavras)

def mostrar_palavra_oculta(palavra, letras_adivinhadas):
    resultado = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

def jogo_da_forca():
    palavra_oculta = escolher_palavra()
    letras_adivinhadas = []
    tentativas_maximas = 6
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print(mostrar_palavra_oculta(palavra_oculta, letras_adivinhadas))

    while tentativas < tentativas_maximas:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        letras_adivinhadas.append(letra)

        if letra not in palavra_oculta:
            tentativas += 1
            print(f"Incorreto! Tentativas restantes: {tentativas_maximas - tentativas}")
        else:
            print("Correto!")

        print(mostrar_palavra_oculta(palavra_oculta, letras_adivinhadas))

        if "_" not in mostrar_palavra_oculta(palavra_oculta, letras_adivinhadas):
            print("Parabéns! Você acertou a palavra!")
            break

    if tentativas == tentativas_maximas:
        print(f"Fim de jogo! A palavra correta era '{palavra_oculta}'.")

# Executar o jogo
jogo_da_forca()

#------------------------------------------------------------------------------#

def celsius_para_fahrenheit(celsius):
    """Converte temperatura de Celsius para Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    """Converte temperatura de Fahrenheit para Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def quilometros_para_milhas(quilometros):
    """Converte distância de quilômetros para milhas."""
    milhas = quilometros * 0.621371
    return milhas

def milhas_para_quilometros(milhas):
    """Converte distância de milhas para quilômetros."""
    quilometros = milhas / 0.621371
    return quilometros

# Exemplos de uso
temperatura_celsius = 30
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius} Celsius é igual a {temperatura_fahrenheit:.2f} Fahrenheit")

distancia_quilometros = 100
distancia_milhas = quilometros_para_milhas(distancia_quilometros)
print(f"{distancia_quilometros} quilômetros é igual a {distancia_milhas:.2f} milhas")

#------------------------------------------------------------------------------#

def calcular_media(lista):
    """Calcula a média dos números em uma lista."""
    if not lista:
        return "Lista vazia, não é possível calcular a média."
    
    soma = sum(lista)
    media = soma / len(lista)
    return media

def calcular_mediana(lista):
    """Calcula a mediana dos números em uma lista."""
    if not lista:
        return "Lista vazia, não é possível calcular a mediana."

    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)

    if tamanho % 2 == 0:
        # Se a lista tem um número par de elementos, a mediana é a média dos dois do meio
        meio_esquerda = lista_ordenada[tamanho // 2 - 1]
        meio_direita = lista_ordenada[tamanho // 2]
        mediana = (meio_esquerda + meio_direita) / 2
    else:
        # Se a lista tem um número ímpar de elementos, a mediana é o valor do meio
        mediana = lista_ordenada[tamanho // 2]

    return mediana

# Exemplos de uso
lista_numeros = [5, 2, 8, 3, 7, 1, 9]

media = calcular_media(lista_numeros)
mediana = calcular_mediana(lista_numeros)

print(f"Lista de números: {lista_numeros}")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana}")

#------------------------------------------------------------------------------#

def calcular_media(lista_numeros):
    """Calcula a média de uma lista de números."""
    if not lista_numeros:
        return None
    return sum(lista_numeros) / len(lista_numeros)

def calcular_mediana(lista_numeros):
    """Calcula a mediana de uma lista de números."""
    if not lista_numeros:
        return None
    lista_ordenada = sorted(lista_numeros)
    tamanho = len(lista_ordenada)
    
    if tamanho % 2 == 0:
        mediana = (lista_ordenada[tamanho//2 - 1] + lista_ordenada[tamanho//2]) / 2
    else:
        mediana = lista_ordenada[tamanho//2]
    
    return mediana

def contar_palavras(frase):
    """Conta o número de palavras em uma string."""
    palavras = frase.split()
    return len(palavras)

# Exemplos de uso
lista_numeros = [4, 7, 1, 9, 2, 5]
print(f"Média: {calcular_media(lista_numeros)}")
print(f"Mediana: {calcular_mediana(lista_numeros)}")

frase = "Esta é uma frase de exemplo."
print(f"Número de palavras na frase: {contar_palavras(frase)}")

#------------------------------------------------------------------------------#

def calcular_media(lista_numeros):
    """Calcula a média de uma lista de números."""
    if not lista_numeros:
        return None
    return sum(lista_numeros) / len(lista_numeros)

def calcular_mediana(lista_numeros):
    """Calcula a mediana de uma lista de números."""
    if not lista_numeros:
        return None
    lista_ordenada = sorted(lista_numeros)
    tamanho = len(lista_ordenada)
    
    if tamanho % 2 == 0:
        mediana = (lista_ordenada[tamanho//2 - 1] + lista_ordenada[tamanho//2]) / 2
    else:
        mediana = lista_ordenada[tamanho//2]
    
    return mediana

def contar_palavras(frase):
    """Conta o número de palavras em uma string."""
    palavras = frase.split()
    return len(palavras)

# Exemplos de uso
lista_numeros = [4, 7, 1, 9, 2, 5]
print(f"Média: {calcular_media(lista_numeros)}")
print(f"Mediana: {calcular_mediana(lista_numeros)}")

frase = "Esta é uma frase de exemplo."
print(f"Número de palavras na frase: {contar_palavras(frase)}")

#------------------------------------------------------------------------------#

import re

print("Cadastre aqui sua senha com os seguintes critérios:")
print("  * Ao menos 8 dígitos")
print("  * Ao menos uma letra MAIÚSCULA")
print("  * Ao menos um número")
print("  * Ao menos um caractere especial (!@#$%¨&*)")

senha = input("Digite sua senha: ")

while not (re.search(r'.{8,}', senha) and
           re.search(r'[A-Z]', senha) and
           re.search(r'\d', senha) and
           re.search(r'[!@#$%¨&*]', senha)):
    senha = input("Use como base os critérios informados: ")

print("Senha cadastrada com sucesso!")

#------------------------------------------------------------------------------#

import random
import string

def gerar_senha(comprimento, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_caracteres_especiais=True):
    caracteres = ""

    if incluir_maiusculas:
        caracteres += string.ascii_uppercase

    if incluir_minusculas:
        caracteres += string.ascii_lowercase

    if incluir_numeros:
        caracteres += string.digits

    if incluir_caracteres_especiais:
        caracteres += string.punctuation

    if not caracteres:
        print("Erro: Nenhum conjunto de caracteres selecionado.")
        return None

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Exemplo de uso
comprimento_senha = int(input("Digite o comprimento desejado para a senha: "))
maiusculas = input("Incluir letras maiúsculas? (S/N): ").upper() == 'S'
minusculas = input("Incluir letras minúsculas? (S/N): ").upper() == 'S'
numeros = input("Incluir números? (S/N): ").upper() == 'S'
caracteres_especiais = input("Incluir caracteres especiais? (S/N): ").upper() == 'S'

senha_gerada = gerar_senha(comprimento_senha, maiusculas, minusculas, numeros, caracteres_especiais)

if senha_gerada:
    print(f"A senha gerada é: {senha_gerada}")
else:
    print("Não foi possível gerar a senha.")

#------------------------------------------------------------------------------#

import random

def simular_lancamento_dados(numero_lancamentos, numero_faces):
    resultados = [random.randint(1, numero_faces) for _ in range(numero_lancamentos)]
    return resultados

def calcular_soma(resultados):
    return sum(resultados)

# Exemplo de uso
numero_lancamentos = int(input("Digite o número de lançamentos de dados: "))
numero_faces = int(input("Digite o número de faces do dado: "))

resultados_dados = simular_lancamento_dados(numero_lancamentos, numero_faces)
soma_resultados = calcular_soma(resultados_dados)

print(f"Resultados dos lançamentos: {resultados_dados}")
print(f"Soma dos resultados: {soma_resultados}")

#------------------------------------------------------------------------------#

# Bubble Sort:
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Exemplo de uso
lista_bubble = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lista_bubble)
print("Bubble Sort:", lista_bubble)

# Selection Sort:
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

# Exemplo de uso
lista_selection = [64, 25, 12, 22, 11]
selection_sort(lista_selection)
print("Selection Sort:", lista_selection)


# Merge Sort:
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        parte_esquerda = lista[:meio]
        parte_direita = lista[meio:]

        merge_sort(parte_esquerda)
        merge_sort(parte_direita)

        i = j = k = 0

        while i < len(parte_esquerda) and j < len(parte_direita):
            if parte_esquerda[i] < parte_direita[j]:
                lista[k] = parte_esquerda[i]
                i += 1
            else:
                lista[k] = parte_direita[j]
                j += 1
            k += 1

        while i < len(parte_esquerda):
            lista[k] = parte_esquerda[i]
            i += 1
            k += 1

        while j < len(parte_direita):
            lista[k] = parte_direita[j]
            j += 1
            k += 1

# Exemplo de uso
lista_merge = [38, 27, 43, 3, 9, 82, 10]
merge_sort(lista_merge)
print("Merge Sort:", lista_merge)

#------------------------------------------------------------------------------#

def verificar_palindromo(texto):
    texto = texto.lower()  # Converte para minúsculas para ignorar maiúsculas/minúsculas
    texto = ''.join(c for c in texto if c.isalnum())  # Remove caracteres não alfanuméricos

    return texto == texto[::-1]

# Exemplo de uso
palavra = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

if verificar_palindromo(palavra):
    print(f"{palavra} é um palíndromo.")
else:
    print(f"{palavra} não é um palíndromo.")

#------------------------------------------------------------------------------#

def calcular_juros_compostos(principal, taxa_de_juros, tempo):
    """
    Calcula o montante final de um investimento com juros compostos.

    Parâmetros:
    - principal: o valor inicial do investimento.
    - taxa_de_juros: a taxa de juros por período (em porcentagem).
    - tempo: o número de períodos em que o investimento é mantido.

    Retorna:
    - O montante final do investimento após o tempo especificado.
    """
    taxa_decimal = taxa_de_juros / 100.0
    montante_final = principal * (1 + taxa_decimal) ** tempo
    return montante_final

# Exemplo de uso
principal_investido = float(input("Digite o valor principal do investimento: "))
taxa_de_juros_anual = float(input("Digite a taxa de juros anual (%): "))
tempo_anos = int(input("Digite o número de anos que o investimento será mantido: "))

montante_final = calcular_juros_compostos(principal_investido, taxa_de_juros_anual, tempo_anos)
print(f"O montante final do investimento será: {montante_final:.2f}")

#------------------------------------------------------------------------------#

def validar_cartao_credito(numero_cartao):
    # Converte o número do cartão para uma lista de dígitos
    digitos = [int(digito) for digito in str(numero_cartao)]

    # Inverte a lista de dígitos
    digitos.reverse()

    # Aplica o algoritmo de Luhn
    soma = 0
    for i in range(len(digitos)):
        if i % 2 == 1:
            digito_dobrado = digitos[i] * 2
            soma += digito_dobrado if digito_dobrado < 10 else digito_dobrado - 9
        else:
            soma += digitos[i]

    # O número do cartão é válido se a soma é um múltiplo de 10
    return soma % 10 == 0

# Exemplo de uso
numero_cartao = input("Digite o número do cartão de crédito: ")

if validar_cartao_credito(numero_cartao):
    print("O número do cartão de crédito é válido.")
else:
    print("O número do cartão de crédito não é válido.")

#------------------------------------------------------------------------------#

import time

def cronometro():
    input("Pressione Enter para começar o cronômetro.")
    inicio = time.time()
    
    try:
        while True:
            tempo_decorrido = round(time.time() - inicio, 2)
            print(f"Tempo decorrido: {tempo_decorrido} segundos", end='\r')
            time.sleep(0.1)
    except KeyboardInterrupt:
        fim = time.time()
        tempo_total = round(fim - inicio, 2)
        print(f"\nCronômetro parado. Tempo total: {tempo_total} segundos.")

# Exemplo de uso
cronometro()

#------------------------------------------------------------------------------#

def encontrar_maior_numero(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    return max(lista)

def encontrar_menor_numero(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    return min(lista)

# Exemplo de uso
lista_de_numeros = [12, 5, 27, 8, 15, 3, 20]

maior_numero = encontrar_maior_numero(lista_de_numeros)
menor_numero = encontrar_menor_numero(lista_de_numeros)

print(f"Lista de números: {lista_de_numeros}")
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")

#------------------------------------------------------------------------------#

def fibonacci(n):
    fibonacci_sequence = [0, 1]  # Inicializa a sequência com os primeiros dois números

    for i in range(2, n):
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Calcula o próximo número Fibonacci
        fibonacci_sequence.append(next_fibonacci)  # Adiciona o próximo número à sequência

    return fibonacci_sequence[:n]  # Retorna os primeiros N números da sequência

# Exemplo de uso
n = int(input("Digite o número de termos da sequência Fibonacci que você deseja gerar: "))
sequence = fibonacci(n)
print("Sequência de Fibonacci:", sequence)

#------------------------------------------------------------------------------#

import re

def validar_email(email):
    # Verifica se o e-mail possui um único '@' e pelo menos um '.' após o '@'
    padrao = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(re.match(padrao, email))

# Exemplo de uso
endereco_email = input("Digite o endereço de e-mail para validar: ")

if validar_email(endereco_email):
    print(f"{endereco_email} é um endereço de e-mail válido.")
else:
    print(f"{endereco_email} não é um endereço de e-mail válido.")

#------------------------------------------------------------------------------#

def converter_moeda(valor, taxa_cambio):
    return valor * taxa_cambio

# Exemplo de uso
moeda_origem = input("Digite a moeda de origem: ")
moeda_destino = input("Digite a moeda de destino: ")

try:
    taxa_cambio = float(input(f"Digite a taxa de câmbio de {moeda_origem} para {moeda_destino}: "))
except ValueError:
    print("Digite uma taxa de câmbio válida.")
    exit()

quantidade = float(input(f"Digite a quantidade de {moeda_origem} a ser convertida para {moeda_destino}: "))

resultado = converter_moeda(quantidade, taxa_cambio)

print(f"{quantidade} {moeda_origem} equivalem a {resultado:.2f} {moeda_destino}")

#------------------------------------------------------------------------------#

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    for _ in range(9):  # No máximo 9 jogadas
        imprimir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1, ou 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1, ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
        else:
            print("Essa posição já está ocupada. Escolha outra.")
            continue

        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

    else:
        imprimir_tabuleiro(tabuleiro)
        print("Empate! O jogo da velha terminou sem vencedor.")

# Exemplo de uso
jogar_jogo_da_velha()








