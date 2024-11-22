import random

def tabuleiro(jogo_tabuleiro):

    for i in range(len(jogo_tabuleiro)):
        for j in range(len(jogo_tabuleiro[i])):
            print(f"{jogo_tabuleiro[i][j]} ", end=" ")
            if j < len(jogo_tabuleiro[i]) - 1:
                print("|", end=" ")
        print()
        if i < len(jogo_tabuleiro) - 1:
            print("---+----+---")

    return jogo_tabuleiro

def players():
    player1_name = input("PLAYER 1\n"
                         "Digite seu nome: ")
    player2_name = input("PLAYER 2\n"
                         "Digite seu nome: ")

    turn = random.choice([1, 2])

    return player1_name, player2_name, turn

def game(jogo_tabuleiro, player1_name, player2_name, turn):
    while True:
        if turn == 1:
            current_player = player1_name
            symbol = 'X'
        else:
            current_player = player2_name
            symbol = 'O'

        print(f"Agora é a vez de {current_player} ({symbol})")

        while True:
            try:
                jogada = input(f"{current_player}, escolha sua jogada (linha-coluna): ")
                linha, coluna = jogada.split("-")
                linha, coluna = int(linha), int(coluna)
            except ValueError:
                print("Formato inválido! Utilize linha-coluna, como 0-1.")
                continue

            if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                print("Jogada inválida! Tente novamente.")
                continue

            if jogo_tabuleiro[linha][coluna] != " ":
                print("Posição já ocupada! Escolha outra.")
                continue

            jogo_tabuleiro[linha][coluna] = symbol
            tabuleiro(jogo_tabuleiro)

            if verifica_vencedor(jogo_tabuleiro, symbol):
                print()
                print(f"{current_player} ganhou!")
                tabuleiro(jogo_tabuleiro)
                return

            if all(celula != " " for linhas in jogo_tabuleiro for celula in linhas):
                tabuleiro(jogo_tabuleiro)
                print("Empate!")
                return

            break

        # Alternar a vez
        turn = 2 if turn == 1 else 1

def verifica_vencedor(tabuleiro, symbol):

    for linhas in tabuleiro:
        if all(celula == symbol for celula in linhas):
            return True

    for colunas in range(3):
        if all(tabuleiro[linhas][colunas] == symbol for linhas in range(3)):
            return True

    if all(tabuleiro[i][i] == symbol for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == symbol for i in range(3)):
        return True

    return False

def explicacao():
    print("Para jogar, escolha a posição do símbolo. Linha 0 1 2, coluna 0 1 2. Exemplo: 0-1")
    print("   |  O  |\n"
          "---+----+---\n"
          "   |    |\n"
          "---+----+---\n"
          "   |    |\n"
          "********************")
jogo_tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
explicacao()
player1_name, player2_name, turn = players()
game(jogo_tabuleiro, player1_name, player2_name, turn)