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
