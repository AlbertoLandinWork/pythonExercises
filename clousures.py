def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo puedes ingresar cadenas de texto'
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hola'))
    repeat_ten = make_repeater_of(10)
    print(repeat_ten('Platzi'))

if __name__ == '__main__':
    run()

def make_division_stop(divisor):
    def division(dividendo):
        assert type(dividendo) == int, "Solo puedes dividir enteros"
        return dividendo // divisor
    return division

def run(): 
    divide_3 = make_division_stop(3)
    print(divide_3(18))
    divide_5 = make_division_stop(5)
    print(divide_5(100))
    divide_18 = make_division_stop(18)
    print(divide_18(54))


if __name__ == '__main__':
    run()