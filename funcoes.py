def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_posicoes = []
    for i in range(tamanho):
        if orientacao == "vertical":
            lista_posicoes.append([linha + i, coluna])
        else:
            lista_posicoes.append([linha, coluna + i])
    
    return lista_posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha,coluna,orientacao,tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = []
        frota[nome_navio].append(posicoes)
    
    return frota 
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
         
    return tabuleiro
def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha = [0]*10
        tabuleiro.append(linha)
    for navio in frota:
        for posicao in frota[navio]:
            for coordenada in posicao:
                linha = coordenada[0]
                coluna = coordenada[1]
                tabuleiro[linha][coluna] = 1
    
    return tabuleiro

        
