import random
import string

def gerar_senha(comprimento, maiusculas=True, minusculas=True, numeros=True, especiais=True):
    caracteres = ""
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if especiais:
        caracteres += string.punctuation
    
    if not caracteres:
        return "Erro: Nenhum conjunto de caracteres selecionado."
    
    senha = "".join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Exemplo de uso:
if __name__ == "__main__":
    print("Gerador de Senhas")
    comprimento = int(input("Digite o tamanho da senha: "))
    maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == "s"
    minusculas = input("Incluir letras minúsculas? (s/n): ").strip().lower() == "s"
    numeros = input("Incluir números? (s/n): ").strip().lower() == "s"
    especiais = input("Incluir caracteres especiais? (s/n): ").strip().lower() == "s"
    senha = gerar_senha(comprimento, maiusculas, minusculas, numeros, especiais)
    print(f"Senha gerada: {senha}")
