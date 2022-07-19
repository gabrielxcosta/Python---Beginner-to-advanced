# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois conjuntos)
# difference - (elementos apenas no conjunto da esquerda)
# symmetric difference ^ (elementos que estão nos dois conjuntos, mas não em ambos)
s1 = {1, 2, 3, 4, 5}
s2 = {5, 6, 7, 8, 9}

uniao = s1 | s2
inters = s1 & s2
dif = s1 - s2
s_dif = s1 ^ s2

print('s1:', s1)
print('s2:', s2)
print('Conjunto união:', uniao)
print('Conjunto intersecção:', inters)
print('Conjunto diferença:', dif)
print('Conjunto diferença simétrica:', s_dif)