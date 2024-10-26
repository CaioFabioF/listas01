lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    else: 
        print('Número já existente, este número não será adicionado.')
    a = str(input('Deseja continuar[S/N]? ')).strip().upper()
    if a in 'Nn':
        break
lista.sort()
print(lista)