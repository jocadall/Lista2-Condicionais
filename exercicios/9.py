while True:
    age =int(input('\n  Quantos anos de  idade  você tem? '))
    time=int(input('\n  Quantos anos de serviço você tem? '))
    if age<0 or age>122:
        print('\n    Idade inválida\n')
    elif age>=65 and age<123 and age-16>=time:
        print('\n    Já pode se aposentar\n')
    elif age>=46 and age<123 and time>=30 and age-16>=time:
        print('\n    Já pode se aposentar\n')
    elif age>=60 and age<123 and time>=25 and age-16>=time:
        print('\n    Já pode se aposentar\n')
    elif time>age-16 or time<0:
        print('\n    Tempo de serviço inválido\n')
    else:
        print('\n    Ainda não pode se aposentar\n')
