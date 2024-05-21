while True:
    print('\n\n')
    P=0
    I=0
    while True:
        print('    Para verificar se um número é par ou ímpar, escolha um que seja inteiro e diferente de zero.\n    já para exibir a soma entre os números digite 0.\n ')
        n=int(input('    Agora digite o número inteiro escolhido ou digite 0: '))
        if n%2==0 and n!=0:
            print(f'\n        O número {n} é par\n ')
            P+=n
        elif n==0:
            break
        elif n%2==1:
            print(f'\n        O número {n} é ímpar.\n ')
            I+=n
        else:
            print('    O número não é inteiro. ')
    print()
    if P!=0 and I!=0:
        print(f'        A soma dos números  pares  é {P}\n        A soma dos números ímpares é {I}\n')
    elif P!=0 and I==0:
        print(f'        A soma dos números  pares  é {P}\n        Nenhum número ímpar\n')
    elif P==0 and I!=0:
        print(f'        Nenhum número par\n        A soma dos números ímpares é {I}\n')
    elif P==0 and I==0:
        print('        Nenhum número par\n        Nenhum número ímpar')
    print()
