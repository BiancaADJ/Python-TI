# Define o mapeamento para a codificação
# Substitua ou adicione letras conforme necessário
mapa_codificacao = {
    'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T',
    'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'T',
    'O': 'A', 'P': 'V', 'Q': 'W', 'R': 'X', 'S': 'Z', 'T': 'B', 'U': 'E',
    'V': 'C', 'W': 'D', 'X': 'F', 'Y': 'I', 'Z': 'G'
}

# Inverter o mapeamento para decodificação
mapa_decodificacao = {v: k for k, v in mapa_codificacao.items()}

def traduzir_texto(texto, mapa):
    """Traduz o texto com base no mapeamento fornecido."""
    texto_traduzido = ""
    for char in texto:
        if char.upper() in mapa:  # Verifica se o caractere está no mapeamento
            # Mantém maiúsculas e minúsculas
            texto_traduzido += mapa[char.upper()].lower() if char.islower() else mapa[char.upper()]
        else:
            # Mantém caracteres não mapeados (espaços, pontuações, etc.)
            texto_traduzido += char
    return texto_traduzido

# Menu para o usuário
while True:
    print("\n=== Tradutor Personalizado ===")
    print("1. Codificar texto")
    print("2. Decodificar texto")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        texto = input("\nDigite o texto para codificar: ")
        resultado = traduzir_texto(texto, mapa_codificacao)
        print(f"Texto codificado: {resultado}")

    elif opcao == "2":
        texto = input("\nDigite o texto para decodificar: ")
        resultado = traduzir_texto(texto, mapa_decodificacao)
        print(f"Texto decodificado: {resultado}")

    elif opcao == "3":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
