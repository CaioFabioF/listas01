lista = []
for c in range(0,5):
    lista.append(float(input('Digite um valor: ')))
print(f'A lista é {lista}')
print(f'O maior valor foi {max(lista)}')
for i, v in enumerate(lista):
    if v == max(lista) :
        print(f'O maior valor foi encontrado na posição {i}')
print(f'O menor valor foi {min(lista)}')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'O menor valor foi encontrado na posição {i}')
