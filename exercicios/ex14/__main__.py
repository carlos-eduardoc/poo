from fracao import Fracao


def main():
    f1 = Fracao(3, 7)
    f2 = Fracao(4, 7)

    print(f'Fração: {f1}  Decimal: {f1.numerador/f1.denominador:.2f}')
    print(f'Fração: {f2}  Decimal: {f2.numerador/f2.denominador:.2f}')

    f3 = f1 + f2
    print(f'Fração: {f3}  Decimal: {f3.numerador/f3.denominador:.2f}')


if __name__ == '__main__':
    main()
