

from funciones import *

import unittest
from unittest.mock import patch, MagicMock


# Suponiendo que el código de las funciones está en un archivo llamado 'juego.py'
# from juego import decorador, respuestas_por_categoria, recursion_respuestas, preguntas_random, bind, unit, juego, iniciar

class TestGameFunctions(unittest.TestCase):
    def setUp(self):
        self.preguntas = [
            # Categoria 1
            ["¿Cuál es el color del cielo?", "Azul", "Categoria 1"],
            ["¿Cuál es el color de la hierba?", "Verde", "Categoria 1"],
            ["¿Cuál es el color del sol?", "Amarillo", "Categoria 1"],
            ["¿Qué gas respiramos principalmente?", "Oxígeno", "Categoria 1"],
            ["¿Cuál es el planeta más cercano al sol?", "Mercurio", "Categoria 1"],

            # Categoria 2
            ["¿Quién escribió 'Cien años de soledad'?", "Gabriel García Márquez", "Categoria 2"],
            ["¿Quién pintó 'La última cena'?", "Leonardo da Vinci", "Categoria 2"],
            ["¿Quién es el autor de 'Don Quijote de la Mancha'?", "Miguel de Cervantes", "Categoria 2"],
            ["¿Qué obra escribió Shakespeare sobre un rey danés?", "Hamlet", "Categoria 2"],
            ["¿Cuál es el nombre del autor de '1984'?", "George Orwell", "Categoria 2"],

            # Categoria 3
            ["¿Qué es el ADN?", "Ácido desoxirribonucleico", "Categoria 3"],
            ["¿Cómo se llama la célula que transporta oxígeno en la sangre?", "Glóbulo rojo", "Categoria 3"],
            ["¿Qué organelo celular es conocido como la 'central eléctrica' de la célula?", "Mitocondria", "Categoria 3"],
            ["¿Qué tipo de enlace une los aminoácidos en una proteína?", "Enlace peptídico", "Categoria 3"],
            ["¿Qué tipo de macromolécula son los ácidos nucleicos?", "Polímeros", "Categoria 3"],

            # Categoria 4
            ["¿Cuál es la capital de Francia?", "París", "Categoria 4"],
            ["¿Cuál es la capital de Japón?", "Tokio", "Categoria 4"],
            ["¿Cuál es la capital de Egipto?", "El Cairo", "Categoria 4"],
            ["¿Cuál es la capital de Italia?", "Roma", "Categoria 4"],
            ["¿Cuál es la capital de Australia?", "Canberra", "Categoria 4"],

            # Categoria 5
            ["¿Qué es la fotosíntesis?", "Proceso por el cual las plantas producen su propio alimento", "Categoria 5"],
            ["¿Qué órgano en el cuerpo humano produce insulina?", "Páncreas", "Categoria 5"],
            ["¿Cuál es el proceso por el que las células se dividen para producir células hijas?", "Mitosis", "Categoria 5"],
            ["¿Qué es la teoría de la relatividad?", "Teoría propuesta por Einstein sobre la relatividad del tiempo y el espacio", "Categoria 5"],
            ["¿Qué molécula es conocida como la 'moneda energética' de la célula?", "ATP", "Categoria 5"]
        ]
        self.preguntasJuego =  [["¿Qué es la fotosíntesis?", "Proceso por el cual las plantas producen su propio alimento", "Categoria 5"],
            ["¿Qué órgano en el cuerpo humano produce insulina?", "Páncreas", "Categoria 5"],
            ["¿Cuál es el proceso por el que las células se dividen para producir células hijas?", "Mitosis", "Categoria 5"],
            ["¿Qué es la teoría de la relatividad?", "Teoría propuesta por Einstein sobre la relatividad del tiempo y el espacio", "Categoria 5"],
            ["¿Qué molécula es conocida como la 'moneda energética' de la célula?", "ATP", "Categoria 5"]]
        self.mapa = {
            "a":"ATP",
            "b":"Páncreas",
            "c":"Mitosis"
        }
    
    def test_respuestas_por_categoria(self):
        gen = respuestas_por_categoria(self.preguntas)
        next(gen)  # Initialize generator
        r1=gen.send("Categoria 1")
        r2 = next(gen)
        
        self.assertIn(r1, ["Azul", "Verde", "Amarillo", "Mercurio", "Oxígeno"])
        self.assertIn(r2, ["Azul", "Verde", "Amarillo", "Mercurio", "Oxígeno"])
        self.assertNotEqual(r1, r2)

    def test_recursion_respuestas(self):
        gen = respuestas_por_categoria(self.preguntas)
        
        respuestas = recursion_respuestas(gen, [], ["Categoria 1", "Categoria 2", "Categoria 3"], ["Azul", "Gabriel García Márquez", "Ácido desoxirribonucleico"])
        self.assertEqual(len(respuestas), 6)
        self.assertIn(respuestas[0],["Azul", "Verde", "Amarillo", "Mercurio", "Oxígeno"])
        self.assertIn(respuestas[1],["Azul", "Verde", "Amarillo", "Mercurio", "Oxígeno"])
        self.assertNotEqual(respuestas[0], respuestas[1])
        self.assertIn(respuestas[2],["Gabriel García Márquez", "Leonardo da Vinci", "Miguel de Cervantes","Hamlet","George Orwell"])
        self.assertIn(respuestas[3],["Gabriel García Márquez", "Leonardo da Vinci", "Miguel de Cervantes","Hamlet","George Orwell"])
        self.assertNotEqual(respuestas[2], respuestas[3])
        self.assertIn(respuestas[4],["Ácido desoxirribonucleico", "Glóbulo rojo", "Mitocondria", "Enlace peptídico", "Polímeros"])
        self.assertIn(respuestas[5],["Ácido desoxirribonucleico", "Glóbulo rojo", "Mitocondria", "Enlace peptídico", "Polímeros"])
        self.assertNotEqual(respuestas[4], respuestas[5])
        

    def test_preguntas_random(self):
        preguntas, opciones = preguntas_random(self.preguntas)
        self.assertEqual(len(preguntas), 5)
        self.assertEqual(len(opciones), 10)
        self.assertTrue(all(opcion in [p[1] for p in self.preguntas] for opcion in opciones))

    def test_bind(self):
        def mock_game(preguntas, pts):
            return preguntas, pts + 10
        
        result = bind(mock_game, ((self.preguntas, ["Azul", "Verde", "Amarillo"]), 10))
        self.assertEqual(result, ((self.preguntas, ["Azul", "Verde", "Amarillo"]), 20))

    def test_unit(self):
        result = unit((self.preguntas, ["Azul", "Verde", "Amarillo"]))
        self.assertEqual(result, ((self.preguntas, ["Azul", "Verde", "Amarillo"]), 0))
    
    
    
    def test_verificar_correcto(self):
        result = verificador(self.mapa, "a", "ATP")
        self.assertEqual(result, True)  # Assuming the input matches the correct answer
    def test_verificar_incorrecto(self):
        result = verificador(self.mapa, "a", "Mitosis")
        self.assertEqual(result, False)  # Assuming the input matches the correct answer


if __name__ == '__main__':
    unittest.main()
