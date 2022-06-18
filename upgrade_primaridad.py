import math   
def es_primo(numero):
    factorial = 1
    for i in range(1, numero):
        factorial=factorial*i
    if ( factorial + 1 ) % numero == 0:
        return "Es primo"
    else:
        return "No es primo"

def run():
     numero = int(input('Escribe un numero: '))
     respuesta = es_primo(numero)
     print(respuesta)
    #  y = math.sqrt(numero)

    
    #  print(y)



if __name__ == '__main__':
    run()