import random

def desenhar_forca(tentativas_erradas):
    stages = [  # estágio 0
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """,
        # erro 1
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # erro 2
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
           -
        """,
        #erro 3
        """
        --------
        |      |
        |      O
        |      |
        |      |
        |      
        |     
        -
        """,
        # erro 4
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        
        # erro 5 (final)
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """
    ]
    if tentativas_erradas < len(stages):
        print(stages[tentativas_erradas])

with open('palavras.txt', 'r') as file:
    possiveis_palavras = [word.strip() for word in file.readlines()]

palavra_escondida = random.choice(possiveis_palavras)
letra_correta = []
tentativas_erradas = 0
letra_digitada = []
letra_errada = []

while True: 
    print("\n")
    letra = input("Digite aqui uma possível letra: ").lower()

    if len(letra) > 1:
        print("Digite apenas uma letra")
        continue

    palavra_escondida_minuscula = palavra_escondida.lower()
    
    if letra in palavra_escondida_minuscula:
        if letra in letra_correta:
            print("Você já digitou essa letra")
        else:
            letra_correta.append(letra)
    else:
        if letra in letra_errada:
            print("Você já digitou essa letra")
        else: 
            letra_errada.append(letra)
            tentativas_erradas += 1
            chances = 5 - tentativas_erradas
            print(f"As letras erradas: {letra_errada}")
            print(f"Você tem mais {chances} chances")

    desenhar_forca(tentativas_erradas)

    palavra_formada = ''
    for letra_secreta in palavra_escondida:
        if letra_secreta.lower() in letra_correta:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print(palavra_formada)
    print("\n")
    print("============================================================")
    if tentativas_erradas == 5:
        print(f"Você não conseguiu! A palavra era {palavra_escondida}")
        break
    
    if palavra_formada == palavra_escondida:
        print(f"Parabéns!")
        break
