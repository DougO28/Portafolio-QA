import unittest

# Importar aqui la funcion del modulo a utilizar
# from app.main import mi funcion # Ejemplo de importación de una función específica

# Simulación de una función a probar / Modificar a conveniencia
def sumar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


class TestFuncionesBasicas(unittest.TestCase):
    """
    Pruebas funcionales para funciones clave del sistema.
    """

    def test_suma_valores_correctos(self):
        self.assertEqual(sumar(3, 5), 8)
        self.assertEqual(sumar(-2, 2), 0)

    def test_division_valores_validos(self):
        self.assertAlmostEqual(dividir(10, 2), 5)
        self.assertAlmostEqual(dividir(7, 2), 3.5)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    # Aquí puedes seguir agregando ,mas pruebas funcionales
    # def test_nombre_funcion(self): etc.
    

if __name__ == '__main__':
    unittest.main()
