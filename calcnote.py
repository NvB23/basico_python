print('\033[1;35m-' * 40)
print(f'{"CALCULE SUA NOTA":^40}')
print('\033[1;35m-\033[m' * 40)
op = 0

while op != 3:
    print(' ')
    print('''\033[1;36mEscolha uma opção:
    [ 1 ] Calcular a nota do Bimestre.
    [ 2 ] Calcular a se dá pra passar.
    [ 3 [ Sair do programa.''')
    print(' ')
    op = int(input('>>>>> Qual a sua opção: \033[m'))

    if op == 1:
        from time import sleep

        print(' ')
        print('\033[0;32m-=-*' * 30)
        n1 = float(input('{}Qual a sua nota parcial?{} '.format('\033[1;4;34m', '\033[m')))
        print(' ')
        n2 = float(input('{}Qual a sua nota global?{} '.format('\033[1;4;34m', '\033[m')))
        print(' ')
        n3 = float(input('{}Qual a sua qualitativa?{} '.format('\033[1;4;34m', '\033[m')))
        print('\033[0;32m-=-*' * 30)
        print(' ')
        m = (n1 + n2 + n3) / 3
        print('{}PROCESSANDO INFORMAÇÕES'.format('\033[1;36m'))
        sleep(3)
        print(' ')
        print('{}A sua média é {}{:.1f}'.format('\033[1;33m', '\033[4m', m))
        if m >= 7 or m == 7:
            print(f'\033[1;32mPARABÉNS! Dá pra passar com média \033[4m{m:.1f}\033[m')

        else:
            print(f'\033[1;31mQUE PENA! Não dá pra passar com média \033[4;31m{m:.1f}\033[m')

    elif op == 2:
        from time import sleep

        n1 = float(input('\033[1;4;34mQual a nota do 1º Bimestre: '))
        n2 = float(input('Qual a nota do 2º Bimestre: '))
        n3 = float(input('Qual a nota do 3º Bimestre: '))
        n4 = float(input('Qual a nota do 4º Bimestre: \033[m'))
        s = (n1 + n2 + n3 + n4)
        print('\033[1;36mPROCESSANDO\033[m')
        sleep(3)
        print('A soma é: \033[1;36m{}\033[m'.format(s))
        if s > 28:
            print('\033[1;32mPARABÉNS! Dá pra passar.\033[m')
        else:
            print('\033[1;31mQUE PENA! Não dá pra passar.\033[m')
    elif op == 3:
        break

print('\033[1;35mFIM DO PROGRAMA! ATÉ MAIS.')
