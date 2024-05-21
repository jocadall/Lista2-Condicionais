while True:
    temperatura = int(input('Temperatura (em °C): '))
    if temperatura < 15:
        print('"está frio !!"')
    elif temperatura > 25:
        print('"Está calor !"')
    else:
        print('"temperatura agradável !')
    print()