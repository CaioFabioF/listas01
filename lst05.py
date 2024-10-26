lista1 = []
lista2 = []
lista3 = []
while True:
    lista1.append(int(input('Digite um número: ')))
    a = str(input('Deseja continuar[S/N] '))
    if a in 'Nn':
        break
for c in lista1:
    if c % 2 == 0 :
        lista2.append(c)
    else :
        lista3.append(c)
print('-='*50)
print(f'A lista dos númros foi: {lista1}')
print(f'A lista de números pares foi: {lista2}')
print(f'A lista de número ímpares foi: {lista3}')
