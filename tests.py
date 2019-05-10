from unittest import TestCase
from movimientos import *

class Test_movimientos(TestCase):

    def test_tablero_a_cadena(self):
        dado = []
        espero = ""
        obtengo = tablero_a_cadena(dado)
        self.assertEquals(espero, obtengo)

    def test_obtener_nombre_pieza(self):
        dado = []
        espero = ""
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)
    from unittest import TestCase
from movimientos import *

class Test_movimientos(TestCase):

    def test_tablero_a_cadena(self):
        dado = []
        espero = ""
        obtengo = tablero_a_cadena(dado)
        self.assertEquals(espero, obtengo)


    def test_obtener_nombre_pieza(self):
        dado = 'R'
        espero = "Rey Negro"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEqual(espero, obtengo)
        dado = 'Q'
        espero = "Reina Negra"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)
        self.assertEquals(espero, obtengo)
        dado = 'P'
        espero = "Peon Negro"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)
        dado = 'T'
        espero = "Torre Negro"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)
        dado = 'A'
        espero = "Alfil Negro"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)
        dado = 'K'
        espero = "Caballo Negro"
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)


    def test_mover_torre(self):
        dado = [
            [['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
             [' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']],
            0, 0, 5, 0
        ]
        espero = [
            [' ', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
            [' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['t', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
        ]
        obtengo = mover_torre(dado[0], dado[0], dado[0], dado[0], dado[5])
        self.assertEquals(espero, obtengo)
        self.assertRaises(ValueError)

        dado = [
            [['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
             ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']],
            0, 0, 0, 0
        ]
        espero = [
             ['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
             ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
        ]
        obtengo = mover_torre(dado[0], dado[0], dado[0], dado[0], dado[0])
        self.assertEquals(espero, obtengo)
        self.assertEqual(ValueError)
