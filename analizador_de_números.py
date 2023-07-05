from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''            [ 1 ] somar
            [ 2 ] multiplicar
            [ 3 ] maior
            [ 4 ] novos números
            [ 5 ] sair do programa''')
    op = int(input('>>>> Qual a sua opção: '))
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
    elif op == 2:
        mt = n1 * n2
        print('A multiplicação entre {} x {} é {}.'.format(n1, n2, mt))
    elif op == 3:
        if n1 > n2:
            print('Entre  {} e {} o  MAIOR é {}.'.format(n1, n2, n1))
        if n2 > n1:
            print('Entre  {} e {} o  MAIOR é {}.'.format(n1, n2, n2))
        else:
            print('Os valores são iguais.')
    elif op == 4:
        print('Quais são os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('OPÇÃO INVALIDA! TENTE NOVAMENTE.')
print('FINALIZANDO...')
sleep(1)
print('FIM DO PROGRAMA! Volte sempre.')
