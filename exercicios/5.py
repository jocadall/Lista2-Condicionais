while True:
    print()
    h = float(input(' Digite a altura em metros (ponha ponto ao invés de vírgula): '))
    print()
    sexo = input(' Digite 1 se for Homen\n Digite 0 se for Mulher\n ')
    print()
    if sexo == "1":
        peso = (72.7*h) - 58
        print(f'    Peso ideal: {peso}kg')
    elif sexo == "0":
        peso = (62.1*h)-44.7
        print(f'    Peso ideal: {peso}kg')
    else:
        print('   Sexo inexistente')
    print()
