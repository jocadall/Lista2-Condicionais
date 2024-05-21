while True:
    nota = float(input('Nota do estudante (use ponto no lugar da vírgula): '))
    if nota >= 7:
        print('"Estudante aprovado"')
    elif nota >= 4 and nota < 7:
        print('"Estudante em recuperação"')
    elif nota < 4 and nota >= 0:
        print('"Estudante reprovado"')
    else:
        print('Nota inválida')
    print()