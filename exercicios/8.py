while True:
    age=int(input('\n  Quantos anos você tem? '))
    if age<0 or age>120:
        print('    Idade inválida\n')
    elif age<16 and age>=0:
        print('    Não eleitor\n')
    elif age>=16 and age<18:
        print('    Eleitor facultativo\n')
    elif age>65 and age<=120:
        print('    Eleitor facultativo\n')
    elif age>=18 and age<=64:
        print('    Eleitor obrigatório\n')
