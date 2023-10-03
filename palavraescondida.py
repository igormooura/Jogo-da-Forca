import os 
palavra_escondida = 'professor'
letra_correta = []
tentativas_erradas = 0
letra_digitada = []
letra_errada = []

while True: 
    letra = (input("Digite aqui uma possível letra: "))

    if len(letra) > 1:
        print("Digite apenas uma letra")
        continue
    
    if letra in palavra_escondida:
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


    palavra_formada = ''
    for letra_secreta in palavra_escondida:
        if letra_secreta in letra_correta :
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print(palavra_formada)

    if tentativas_erradas == 5:
        print("Você não conseguiu!")
        break
    
    if palavra_formada == palavra_escondida:
        print(f"Parabéns! a palavra era {palavra_escondida}")
        break 