def tablero_a_cadena(tablero):
    cadena = ""
    for fila in tablero:
        cadena += str(fila) + "\n"
    return cadena


def obtener_nombre_pieza(simbolo):
    """
    (str) -> str

    >>> obtener_nombre_pieza('p')
    'Peon blanco'
    >>> obtener_nombre_pieza('R')
    'Rey Negro'

    Retorna el nombre de la pieza del ajedrez dado su simbolo

    :param simbolo: la representacion de la pieza
     segun el enunciado
    :return: El nombre y color de la pieza
    """
    tipo = 'Negro'
    if simbolo.islower():
        tipo = 'blanco'
    retorno = simbolo.lower()
    if retorno == 'p':
        return 'Peon '+tipo
    elif retorno == 't':
        return 'Torre ' + tipo
    elif retorno == 'k':
        return 'Caballo ' + tipo
    elif retorno == 'a':
        return 'Alfil ' + tipo
    elif retorno == 'q':
        return 'Reina ' + tipo
    elif retorno == 'r':
        return 'Rey ' + tipo
    else:
        return 'No es una pieza'

def mover_rey(tablero,x_inicial,x_final,y_inicial, y_final):
    """

    Funcion que define el movimiento del rey

    :param tablero:
    :param x_inicial:
    :param x_final:
    :param y_inicial:
    :param y_final:
    :return:
    """

    pass

    esRey = True


    if (x_inicial == x_final or y_inicial == y_final):
        esRey = tablero[x_inicial][y_inicial] in 'Rr'

        if esRey:
            for x in range(x_inicial + 1, x_final):
                if (tablero[x][y_final] == ''):
                    for y in range (y_inicial, y_final):
                        print([x_inicial],[y])
                else:
                    raise ValueError("El camino esta bloqueado")
                    break
        else:
            print('No es un rey')
    else:
        print("El movimiento no es válido")
