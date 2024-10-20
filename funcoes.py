def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_posicoes = []
    for i in range(tamanho):
        if orientacao == "vertical":
            lista_posicoes.append([linha + i, coluna])
        else:
            lista_posicoes.append([linha, coluna + i])
    
    return lista_posicoes