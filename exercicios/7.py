while True:
    name=input('\n    Visitante do Hopi Hari: ')
    time=int(input('\n    Quantos anos você tem? '))
    kg=int(input('\n    Quantos kg você tem? '))
    if time>15 and kg<=120:
        print(f'\nO visitante {name} está liberado para andar na montanha russa do parque.\n ')
    else:
        print(f'\nO visitante {name} está proibido de andar na montanha russa do parque.\n ')
