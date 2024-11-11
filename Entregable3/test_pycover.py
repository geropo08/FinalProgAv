import pytest
from DSL import Consulta  

def test_select_all_from_usuarios():
    consulta1 = Consulta(idioma="es")
    query1 = (consulta1
              .select()
              .everything()
              .from_table()
              .nombre("usuarios")
              .where()
              .nombre("edad")
              .gr_op()
              .ls_params("18")
              .get_query())
    assert query1 == "SELECT * FROM usuarios WHERE edad > 18"

def test_init_query():
    consulta1 = Consulta(idioma="es", query="SELECT ")
    query1 = (consulta1
              .everything()
              .from_table()
              .nombre("usuarios")
              .where()
              .nombre("edad")
              .ls_op()
              .ls_params("18")  
              .or_op()
              .nombre("edad")
              .is_null()
              .get_query())
    assert query1 == "SELECT * FROM usuarios WHERE edad < 18 OR edad IS NULL"

def test_select_distinct_nombre_from_clientes():
    consulta2 = Consulta(idioma="es")
    query2 = (consulta2
              .select()
              .distinct()
              .nombre("nombre")
              .from_table()
              .nombre("clientes")
              .where()
              .nombre("ciudad")
              .eq_op()
              .ls_params("'Madrid'")
              .get_query())
    assert query2 == "SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid'"

def test_insert_into_usuarios():
    consulta3 = Consulta(idioma="es")
    query3 = (consulta3
              .insert_into()
              .nombre("usuarios")
              .ls_params("(nombre, edad)")
              .values()
              .ls_params("('Juan', 25)")
              .get_query())
    assert query3 == "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25)"

def test_update_empleados():
    consulta4 = Consulta(idioma="es")
    query4 = (consulta4
              .update()
              .nombre("empleados")
              .set()
              .nombre("salario")
              .eq_op()
              .ls_params("3000")
              .where()
              .nombre("puesto")
              .eq_op()
              .ls_params("'ingeniero'")
              .get_query())
    assert query4 == "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero'"

def test_delete_from_clientes():
    consulta5 = Consulta(idioma="es")
    query5 = (consulta5
              .delete()
              .from_table()
              .nombre("clientes")
              .where()
              .nombre("edad")
              .between()
              .ls_params("18 AND 25")
              .get_query())
    assert query5 == "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25"

def test_select_join_pedidos_clientes():
    consulta6 = Consulta(idioma="es")
    query6 = (consulta6
              .select()
              .everything()
              .from_table()
              .nombre("pedidos")
              .join()
              .nombre("clientes")
              .on()
              .nombre("pedidos.cliente_id")
              .eq_op()
              .nombre("clientes.id")
              .where()
              .nombre("clientes.ciudad")
              .eq_op()
              .ls_params("'Barcelona'")
              .get_query())
    assert query6 == "SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = 'Barcelona'"

def test_select_like_from_clientes():
    consulta7 = Consulta(idioma="es")
    query7 = (consulta7
              .select()
              .everything()
              .from_table()
              .nombre("clientes")
              .where()
              .nombre("nombre")
              .like()
              .ls_params("'Juan%'")
              .get_query())
    assert query7 == "SELECT * FROM clientes WHERE nombre LIKE 'Juan%'"

def test_select_count_group_by():
    consulta8 = Consulta(idioma="es")
    query8 = (consulta8
              .select()
              .count()
              .ls_params("(*)")
              .from_table()
              .nombre("ventas")
              .group_by()
              .nombre("producto")
              .having()
              .count()
              .ls_params("(*)")
              .gr_op()
              .ls_params("5")
              .get_query())
    assert query8 == "SELECT COUNT (*) FROM ventas GROUP BY producto HAVING COUNT (*) > 5"

def test_select_limit_from_usuarios():
    consulta9 = Consulta(idioma="es")
    query9 = (consulta9
                   .select()
                   .everything()
                   .from_table()
                   .nombre("usuarios")
                   .limit()
                   .ls_params("10")
                   .get_query())
    assert query9 == "SELECT * FROM usuarios LIMIT 10"

def test_query_cast():
    consulta_cast = Consulta(idioma="es")
    query_cast = (consulta_cast
                  .select()
                  .ls_params("CAST(edad AS VARCHAR)")
                  .from_table()
                  .nombre("usuarios")
                  .where()
                  .nombre("nombre")
                  .eq_op()
                  .ls_params("'Juan'")
                  .get_query())

    assert query_cast == "SELECT CAST(edad AS VARCHAR) FROM usuarios WHERE nombre = 'Juan'"


def test_query_and():
    consulta_and = Consulta(idioma="es")
    query_and = (consulta_and
                 .select()
                 .everything()
                 .from_table()
                 .nombre("empleados")
                 .where()
                 .nombre("puesto")
                 .eq_op()
                 .ls_params("'ingeniero'")
                 .and_op()
                 .nombre("salario")
                 .gr_op()
                 .ls_params("3000")
                 .get_query())

    assert query_and == "SELECT * FROM empleados WHERE puesto = 'ingeniero' AND salario > 3000"


def test_query_not_null():
    consulta_not_null = Consulta(idioma="es")
    query_not_null = (consulta_not_null
                      .select()
                      .everything()
                      .from_table()
                      .nombre("usuarios")
                      .where()
                      .nombre("nombre")
                      .not_null()
                      .get_query())

    assert query_not_null == "SELECT * FROM usuarios WHERE nombre NOT NULL"

def test_query_group_by():
    consulta = Consulta(idioma="es")

    query = (consulta
            .select()
            .everything()
            .from_table()
            .nombre("mi_tabla")
            .where()
            .exists()
            .nombre("(SELECT 1 FROM otra_tabla")
            .where()
            .nombre("otra_tabla.campo")
            .eq_op()
            .nombre("mi_tabla.campo)")
            .group_by()
            .nombre("mi_tabla.campo")
            .get_query())

    assert query == "SELECT * FROM mi_tabla WHERE EXISTS (SELECT 1 FROM otra_tabla WHERE otra_tabla.campo = mi_tabla.campo) GROUP BY mi_tabla.campo"


def test_query_foreign_key():
    consulta_foreign_key = Consulta(idioma="es")
    query_foreign_key = (consulta_foreign_key
                         .create_table()
                         .nombre("pedidos")
                         .ls_params("(id SERIAL PRIMARY KEY, cliente_id INT NOT NULL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))")
                         .get_query())

    assert query_foreign_key == "CREATE TABLE pedidos (id SERIAL PRIMARY KEY, cliente_id INT NOT NULL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))"


def test_query_primary_unique():
    consulta_primary_unique = Consulta(idioma="es")
    query_primary_unique = (consulta_primary_unique
                            .create_table()
                            .nombre("productos")
                            .ls_params("(id SERIAL PRIMARY KEY, nombre VARCHAR(255) UNIQUE NOT NULL)")
                            .get_query())

    assert query_primary_unique == "CREATE TABLE productos (id SERIAL PRIMARY KEY, nombre VARCHAR(255) UNIQUE NOT NULL)"

def test_query_default():
    consulta_default = Consulta(idioma="es")
    query_default = (consulta_default
                        .create_table()
                        .nombre("productos")
                        .ls_params("(id SERIAL PRIMARY KEY, nombre VARCHAR(255) NOT NULL, precio DECIMAL DEFAULT 0.0)")
                        .get_query())

    assert query_default == "CREATE TABLE productos (id SERIAL PRIMARY KEY, nombre VARCHAR(255) NOT NULL, precio DECIMAL DEFAULT 0.0)"


def test_query_drop_table():
    consulta_drop_table = Consulta(idioma="es")
    query_drop_table = (consulta_drop_table
                        .drop_table()
                        .nombre("productos")
                        .get_query())

    assert query_drop_table == "DROP TABLE productos"


def test_query_drop_column():
    consulta_drop_column = Consulta(idioma="es")
    query_drop_column = (consulta_drop_column
                            .alter_table()
                            .nombre("productos")
                            .drop_column()
                            .nombre("precio")
                            .get_query())

    assert query_drop_column == "ALTER TABLE productos DROP COLUMN precio"


def test_query_add_column():
    consulta_add_column = Consulta(idioma="es")
    query_add_column = (consulta_add_column
                        .alter_table()
                        .nombre("productos")
                        .add_column()
                        .nombre("stock INT DEFAULT 0")
                        .get_query())

    assert query_add_column == "ALTER TABLE productos ADD COLUMN stock INT DEFAULT 0"
