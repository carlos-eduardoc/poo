def ativar_dispositivo(obj):
    try:
        print(obj.ligar())
    except (AttributeError, TypeError) as ex:
        print(f'{ex}: O objeto não tem o metodo necesario(ligar())')
    print(obj)
