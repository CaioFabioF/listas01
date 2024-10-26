exp = str(input('Digite a sua expressão matemática: '))
lista = []
for c in exp :
    if c == '(' :
        lista.append('(')
    elif c == ')' :
        if len(lista) > 0 :
            lista.pop()
        else :
            lista.append(')')
if len(lista) > 0 :
    print('Expressão inválida')
else :
    print('Expressão válida')
    