from palavraforca import palavra
letras_chute = []
chances = 7
ganhou = False

while True:
    #criando a lógica do jogo
    for letra in palavra:
        if letra.lower() in letras_chute:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(" ")
    print(f"Você ainda tem {chances} chances!")
    tentativa = input("Escolha uma letra: ")
    letras_chute.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_chute:
            ganhou=False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns! Você ganhou! A palavra era: {palavra}")
else:
    print (f"Que pena! Você perdeu! A palavra era: {palavra}")

