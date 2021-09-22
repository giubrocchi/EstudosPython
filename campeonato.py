def computador_escolhe_jogada(n, m):
    k = 1
    while(k < m and k < n):
        if((n - k)%(m+1) == 0):
            return k
        k += 1
    return k


def usuario_escolhe_jogada(n, m):
    k = 0
    while(k <= 0 or k > m and k >= n):
        print()
        k = int(input("Quantas peças você vai tirar? "))
        if(k <= 0 or k > m or k > n):
            print()
            print("Oops! Jogada inválida! Tente de novo")
        else:
            return k

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()
    if(n%(m+1) == 0):
        print("Você começa!")
        print()
        k = usuario_escolhe_jogada(n, m)
        if(k == 1):
            print("Você tirou uma peça")
        else:
            print("Você tirou", k, "peças.")
        n = n-k
        if(n == 1):
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam", n, "peças no tabuleiro.")
    else:
        print("Computador começa!")
    while(n>0):
        print()
        k = computador_escolhe_jogada(n, m)
        if(k == 1):
            print("O computador tirou uma peça.")
        else:
            print("O computador tirou", k, "peças.")
        n = n-k
        if(n == 0):
            print("Fim do jogo! O computador ganhou!")
            return 1
        elif(n == 1):
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam", n, "peças no tabuleiro.")
        k = usuario_escolhe_jogada(n, m)
        print()
        if(k == 1):
            print("Você tirou uma peça.")
        else:
            print("Você tirou", k, "peças.")
        n = n-k
        if(n == 0):
            print("Fim do jogo! Você ganhou!")
            return 0
        elif(n == 1):
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam", n, "peças no tabuleiro.")
        

def campeonato():
    rodada = 1
    comp = 0
    voce = 0
    while(rodada <= 3):
        print()
        print("**** Rodada", rodada, "****")
        print()
        v = partida()
        if(v == 1):
            comp += 1
        else:
            voce += 1
        rodada += 1
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você", voce, "X", comp, "Computador")

print("Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada")
opcao = int(input("2 - para jogar um campeonato "))
print()
if(opcao == 1):
    print("Você escolheu uma partida")
    partida()
else:
    print("Você escolheu um campeonato")
    campeonato()
    
