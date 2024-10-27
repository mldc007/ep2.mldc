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
def afundados(frota,tabuleiro):
    navio_afundado = 0 
    for navio in frota:
        for posicoes in frota[navio]:
            afundou =  True
            for coordenada in posicoes:
                linha = coordenada[0]
                coluna = coordenada[1]
                if tabuleiro[linha][coluna] != 'X':
                    afundou =  False
                    break 
            if afundou == True:
                navio_afundado += 1
            
    return navio_afundado

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_novas = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes_novas:
            if posicao[0] < 0 or posicao[0] >= 10 or posicao[1] < 0 or posicao[1] >= 10:
                return False
#posicao[o]=linha,posicao[1]=coluna           
    posicoes_ocupadas = []
    for navios in frota.values():
        for navio in navios:
            posicoes_ocupadas.extend(navio) #lista pronta e add de uma vez>>>> add termo a termo com append
    for posicao in posicoes_novas:
        if posicao in posicoes_ocupadas:
            return False  #ocupada
    return True 