def partida():
    pecas = int(input("Quantas peças? "))
    limite = int(input("Limite de peças por jogada? "))
  
    if (pecas % (limite + 1)) == 0 :
        print("Você começa")
        vez_jogador = True
        vez_computador = False

    else:
        print("Computador começa")
        vez_jogador = False
        vez_computador = True

    while pecas > 0:
        if vez_jogador and not vez_computador:
            jogada = usuario_escolhe_jogada(pecas,limite)
            pecas = pecas - jogada
            if pecas == 0:
                jogador_ganha = True
                computador_ganha = False
            else:
                print("Você tirou", jogada ,"peças.")
                print("Agora restam", pecas ,"peças no tabuleiro.")
                vez_jogador = False
                vez_computador = True

        else:
            jogada = computador_escolhe_jogada(pecas,limite)
            pecas = pecas - jogada
            if pecas == 0:
                computador_ganha = True
                jogador_ganha = False
            else:
                print("O computador tirou", jogada ,"peças.")
                print("Agora restam", pecas ,"peças no tabuleiro.")
                vez_jogador = True
                vez_computador = False

    if computador_ganha :
        print("Fim do jogo! O computador ganhou!")
        return computador_ganha

    else:
        print("Fim do jogo! Você ganhou!")
        return jogador_ganha




def computador_escolhe_jogada(n,m):

    #
    # Função que executa a jogada do computador,
    # calculando de acordo com a estratégia vencedora qual será a jogada.
    #

    if n <= m:                                                  # Computador ganha o jogo.
        pecas_a_retirar_computador = n                          #

    elif (n-m) > m:                                             # Computador pode retirar o máximo de peças sem perder o jogo
        pecas_a_retirar_computador = m                          # na próxima rodada.

    elif n<(2*m) and ((n-(n//(m+1))) <= m):                     # Computador vai perder o jogo de qualquer maneira, então deve escolher
        pecas_a_retirar_computador = m                          # o máximo de peças possíveis.

    else:                                                       # Computador precisa executar a jogada calculada para
        pecas_a_retirar_computador = m-(n//(m+1))               # o oponente não ganhar.

    return pecas_a_retirar_computador                           # Peças a serem retiradas pelo computador.

def usuario_escolhe_jogada(n,m):
    
    #
    # Função que executa a jogada do jogador, solicitando uma entrada,
    # validando essa entrada e quando válida retornando essa entrada.
    #     

    numero_valido = False                                       # Condição para terminar o laço a seguir
    while not numero_valido :
        pecas_a_retirar_jogador = int(input("Quantas peças você vai tirar?"))
        if (pecas_a_retirar_jogador <= m) and (pecas_a_retirar_jogador <= n):
            numero_valido = True
        else:
            print("Oops! Jogada inválida! Tente de novo.")
            numero_valido = False
    return pecas_a_retirar_jogador                              # Retorna o um valor escolhido válido


partida()
