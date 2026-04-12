import unittest
from tp1_1 import main as turnos
from tp1_3 import main as cajas

class TestTurnos(unittest.TestCase):
    def test_turnos_1(self):
        # Caso facil: no hay superposiciones, puedo atender primero al primer turno y luego al segundo
        orden, ganancia = turnos([(1, 10), (2, 10)])
        self.assertEqual(orden, [0, 1])
        self.assertEqual(ganancia, 20)
        
        # Caso inverso
        orden, ganancia = turnos([(1, 10), (2, 20)])
        self.assertEqual(orden, [0, 1])
        self.assertEqual(ganancia, 30)
        
        # Caso dificil.
        orden, ganancia = turnos([(1, 20),(1, 10),(5, 30),(5, 30),(5, 30),(5, 30)])
        self.assertEqual(orden, [0, 2, 3, 4, 5])
        self.assertEqual(ganancia, 140)

        # Caso raro 
        orden, ganancia = turnos([(1, 30),(1000, 300)])
        self.assertEqual(orden, [0, 1])
        self.assertEqual(ganancia, 330)

class TestCajas(unittest.TestCase):
    def test_cajas_1(self):
        # Caso facil: una sola caja, tiene altura 1, el orden es la unica caja con base 1 y altura 1
        altura, orden = cajas([(1, 1, 1)])
        self.assertEqual(altura, 1)
        self.assertEqual(orden, [0, (1, 1)])

if __name__ == "__main__":
    unittest.main()
