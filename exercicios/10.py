while True:
    n1=float(input('\n  Primeira nota? '))
    n2=float(input('\n  Segunda  nota? '))
    ma=(n1+n2)/2
    uni=int(input('\n | Código | Universidade |\n |   1    |     PUCPR    |\n |   2    |    UNICAMP   |\n\n  Código da Univesidade? '))
    if uni==1:
        if 10>=ma>=7:
            print('\n    Aprovado(a)\n')
        elif 4<=ma<7:
            print('\n    Em exame\n')
        elif 0<=ma<4:
            print('\n    Reprovado(a)\n')
        else:
            print('\n    Nota inválida')
    elif uni==2:
        if 10>=ma>=5:
            print('\n    Aprovado(a)\n')
        elif 0<=ma<5:
            print('\n    Em exame\n')
        else:
            print('\n    Nota inválida\n')
    else:
        print('\n    Universidade inválida\n')