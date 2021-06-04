lojas = []
final = []
casos = int(input())
i = 0

while(i < casos):
    num_lojas = int(input())
    j = 0
    while(j < num_lojas):
        elemento = int(input())
        lojas.append(elemento)
        j += 1
    maior = max(lojas, key=int)
    menor = min(lojas, key=int)
    aux = (maior - menor) * 2
    final.append(aux)
    i += 1
print (final)