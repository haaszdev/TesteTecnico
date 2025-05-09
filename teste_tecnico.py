
import json
import xml.etree.ElementTree as ET

# -------------------------------
# Questão 1: Soma de 1 a 13
# -------------------------------
def questao_1():
    INDICE = 13
    SOMA = 0
    K = 0
    while K < INDICE:
        K += 1
        SOMA += K
    return SOMA

# -------------------------------
# Questão 2: Verifica se número pertence à sequência de Fibonacci
# -------------------------------
def questao_2(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return numero == 0 or b == numero

# -------------------------------
# Questão 3: Análise de faturamento diário (usando JSON)
# -------------------------------

def questao_3_json(caminho_arquivo):
    with open(caminho_arquivo, encoding='utf-8') as f:
        dados = json.load(f)

    valores = [dia["valor"] for dia in dados if dia["valor"] > 0]
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    acima_media = sum(1 for v in valores if v > media)

    return menor, maior, acima_media

# -------------------------------
# Questão 4: Percentual de representação por estado
# -------------------------------

def questao_4():
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    total = sum(faturamento.values())
    return {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

# -------------------------------
# Questão 5: Inversão de string
# -------------------------------

def questao_5(s):
    invertida = ''
    for char in s:
        invertida = char + invertida
    return invertida

# -------------------------------
# Execução dos testes
# -------------------------------

if __name__ == "__main__":
    print("Questão 1:", questao_1())

    num = 21
    print(f"Questão 2: {num} pertence à Fibonacci?", "Sim" if questao_2(num) else "Não")

    print("\nQuestão 3 com JSON:")
    menor, maior, acima_media = questao_3_json("dados.json")
    print(f"Menor: {menor:.2f}, Maior: {maior:.2f}, Dias acima da média: {acima_media}")

    print("\nQuestão 4:")
    for estado, perc in questao_4().items():
        print(f"{estado}: {perc:.2f}%")

    texto = "exemplo"
    print("\nQuestão 5: Invertendo", texto, "->", questao_5(texto))
