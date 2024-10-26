lista = []
contador = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    contador += 1
    s = str(input('Deseja continuar[S/N] ')).strip().upper()
    if s in 'Nn':
        break
print(f'Foi digitado {contador} números.')
lista.sort(reverse=True)
print(lista)
if 5 in lista :
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista')
    