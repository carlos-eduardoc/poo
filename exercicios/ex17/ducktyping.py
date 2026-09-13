def ativar_dispositivo(obj):
    try:
        obj.ligar()
        print(obj)
    except (AttributeError, TypeError) as ex:
        print(f'{ex}: O objeto não tem o metodo necesario(ligar())')