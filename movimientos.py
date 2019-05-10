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

    :param simbolo: la representacion de la pieza segun el enunciado
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


def mover_torre(tablero, x_inicial, x_final, y_inicial, y_final):
    """
    define la movilidad de la torre en el tablero


    :param tablero: matriz que representa el tablero de juego
    :param x_inicial: posicion de la torre en x inicial
    :param y_inicial: posicion de la torre en x final
    :param x_final: posicion de la torre en y inicial
    :param y_final: posicion de la torre en y final
    :return:
    """

    #Si no hay posiciones diferentes no hay movimiento
    if x_inicial == x_final and y_inicial == y_final:
        raise ValueError("No se realizaron movimientos")

    #Valida si es movimiento en el eje X o Y
    elif x_inicial == x_final:

        #Valida que color de ficha es T o t
        if tablero[x_inicial][y_inicial] == 't'or tablero[x_inicial][y_inicial] == 'T':
            for x in range(y_inicial, y_final + 1):

                # Recorre el movimiento y valida si se puede realizar
                if tablero[x][x_inicial] != "":
                    raise ValueError("movimiento no valido")
                else:
                    return tablero
    else:

        # Valida que color de ficha es T o t
        if tablero[x_inicial][y_inicial] == 't' or tablero[x_inicial][y_inicial] == 'T':

            # Recorre el movimiento y valida si se puede realizar
            for x in range(x_inicial, x_final + 1):
                if tablero[x][y_inicial] != "":
                    raise ValueError("movimiento no valido")
                else:
                    return tablero

