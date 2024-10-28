from funcoes import preenche_frota,posicao_valida

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}        

pedidos = [
    ["porta-aviões",4,1],
    ["navio-tanque",3,2],
    ["contratorpedeiro",2,3],
    ["submarino",1,4],
]     
    
for nome_navio,tamanho,quantidade in pedidos:
    for i in range(quantidade):
        while True:
            print(f'Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            orientacao = 'vertical'
            if tamanho != 1:
                orientacao_int = int(input("[1] Vertical [2] Horizontal >"))
                if orientacao_int == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                break 
            else:
                print('Esta posição não está válida!')
        preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)

print(frota)