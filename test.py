import unittest
import libcplx

class TestComplex(unittest.TestCase):
    def test_Suma(c):
        #Prueba 1
        resultado = libcplx.sumacplx([5, -20], [-4, 2])
        c.assertEqual(resultado, (1, -18))
        #Prueba 2
        resultado = libcplx.sumacplx([-9, 8], [-12, -9])
        c.assertEqual(resultado, (-21, -1))

    def test_Resta(c):
        #Prueba 1
        resultado = libcplx.restaplx([-15,4],[18,-8])
        c.assertEqual(resultado, (-33, 12))
        #Prueba 2
        resultado = libcplx.restaplx([5,6], [-1,-9])
        c.assertEqual(resultado, (6, 15))

    def test_multi(c):
        #Prueba 1
        resultado = libcplx.multcplx([-15, 4], [18, -8])
        c.assertEqual(resultado, (-238, 192))
        #Prueba 2
        resultado = libcplx.multcplx([5, 6], [-1, -9])
        c.assertEqual(resultado, (49, -51))

    def test_divi(c):
        # Prueba 1
        resultado = libcplx.divicplx([-15, 4], [18, -8])
        c.assertEqual(resultado, (-30.2, -4.8))
        # Prueba 2
        resultado = libcplx.divicplx([5, 6], [-1, -9])
        c.assertEqual(resultado, (4.214, -2.786))

    def test_modulo(c):
        #Prueba 1
        resultado = libcplx.modulocplx([-15, 4])
        c.assertEqual(resultado, 15.524)
        #Prueba 2
        resultado = libcplx.modulocplx([18, -8])
        c.assertEqual(resultado, 19.698)

    def test_conju(c):
        # Prueba 1
        resultado = libcplx.conjugadocplx([-15, 4])
        c.assertEqual(resultado, (-15,-4))
        # Prueba 2
        resultado = libcplx.conjugadocplx([18, -8])
        c.assertEqual(resultado, (18, 8))

    def test_convertir(c):
        # Prueba 1
        resultado = libcplx.deCartesianoApolar([5, -20])
        c.assertEqual(resultado, (20.616, -1.326))
        # Prueba 2
        resultado = libcplx.deCartesianoApolar([-12, -9])
        c.assertEqual(resultado, (15, 0.644))

    def test_convertir1(c):
        # Prueba 1
        resultado = libcplx.dePolaraCartesiano( [-4, 2])
        c.assertEqual(resultado, (1.665, -3.637))
        # Prueba 2
        resultado = libcplx.dePolaraCartesiano([-9, 8])
        c.assertEqual(resultado, (1.31, -8.904))

    def test_fase(c):
        # Prueba 1
        resultado = libcplx.fasecplx([18, -8])
        c.assertEqual(resultado, -0.418)
        # Prueba 2
        resultado = libcplx.fasecplx([-1, -9])
        c.assertEqual(resultado, 1.46)

if __name__ == '__main__':
    unittest.main()