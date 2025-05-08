from collections import deque

# Estado: (missionários esquerda, canibais esquerda, barco à esquerda?)
# O resto é implícito: missionários e canibais na direita = 3 - esquerda
def estado_valido(m, c):
    return (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c) and 0 <= m <= 3 and 0 <= c <= 3

def sucessores(estado):
    m, c, lado = estado
    movimentos = [
        (1, 0), (2, 0), (0, 1), (0, 2), (1, 1)
    ]
    res = []
    for mm, cc in movimentos:
        if lado == 'esquerda':
            novo_m, novo_c = m - mm, c - cc
            novo_lado = 'direita'
        else:
            novo_m, novo_c = m + mm, c + cc
            novo_lado = 'esquerda'
        
        if estado_valido(novo_m, novo_c):
            res.append((novo_m, novo_c, novo_lado))
    return res

def bfs():
    inicial = (3, 3, 'esquerda')
    final = (0, 0, 'direita')
    fila = deque()
    fila.append((inicial, [inicial]))
    visitados = set()
    
    while fila:
        estado, caminho = fila.popleft()
        if estado == final:
            return caminho
        for s in sucessores(estado):
            if s not in visitados:
                visitados.add(s)
                fila.append((s, caminho + [s]))
    return None

# Executar
solucao = bfs()
if solucao:
    print("Solução encontrada:")
    for passo in solucao:
        print(passo)
else:
    print("Nenhuma solução encontrada.")
