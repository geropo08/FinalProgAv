import pytest
from unittest.mock import patch
#from traductorSQL import parser, sql_mapping, lexer, dar_vuelta
import ply.lex as lex
import traductorSQL



@pytest.mark.parametrize("input_query,expected_output", [
    ("TRAEME TODO DE LA TABLA usuarios DONDE edad > 18", "SELECT * FROM usuarios WHERE edad > 18"),
    ("TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid'", "SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid'"),
    ("METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25)", "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25)"),
    ("ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero'", "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero'"),
    ("BORRA DE LA TABLA clientes DONDE edad ENTRE 18 Y 25", "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25"),
    
    ("TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona'", "SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = 'Barcelona'"),

    ("TRAEME TODO DE LA TABLA clientes DONDE nombre PARECIDO A 'Juan%'", "SELECT * FROM clientes WHERE nombre LIKE 'Juan%'"),
    ("TRAEME CONTANDO (TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY COUNT (*) > 5", "SELECT COUNT (*) FROM ventas GROUP BY producto HAVING COUNT (*) > 5")


])

def test_sql_translation(input_query, expected_output):
    result = traductorSQL.parser.parse(input_query)
    assert result == expected_output

def test_t_number_valid():
    traductorSQL.lexer.input('12345')
    token = traductorSQL.lexer.token()  
    assert token.type == 'NUMBER'
    assert token.value == 12345

def test_t_number_large_integer():
    traductorSQL.lexer.input('99999999999999999999999999999999999999999999999999999')  
    token = traductorSQL.lexer.token()
    assert token.type == 'NUMBER'
    assert token.value == 0  
        











