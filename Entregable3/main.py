
from traductorSQL import conectar_db, dar_vuelta, parser
from DSL import *
if __name__ == "__main__":\

    conn=conectar_db()
    cursor=conn.cursor()

    print("1- Traductor de SQL")
    print("2- Fluent API")
    trabajo=input('Ingrese opcion: ')
    if trabajo=="1" :

        idioma = input('Ingrese el idioma al cual traducir: ')
        if idioma.lower()=='español':
            dar_vuelta()
        while True:
            try:
                if idioma.lower()=="español":
                    s = input('Consulta SQL en ingles: ')
                else:
                    s = input('Consulta SQL en español: ')
            except EOFError:
                break
            if not s:
                print("Error:query vacia")
                continue
            result = parser.parse(s)
            print("Consulta traducida:", result)
            try:
                if idioma.lower()=='español':
                    resp=cursor.execute(s)
                else:
                    resp=cursor.execute(result)
                
                for fila in resp:
                        print(fila)
            except Exception as e:
                if "no such table" in str(e):
                    print("Alguna tabla no existe")
                elif "no such colum" in str(e):
                    print("Algun atributo no existe")
                else:
                    print("Consulta no valida")
    elif trabajo=="2":
        "Se debe crear"
        
        consulta1 = Consulta(idioma="en")
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
        print(query1)
        try:
            resp=cursor.execute(query1)
                
            for fila in resp:
                print(fila)
        except Exception as e:
            if "no such table" in str(e):
                print("Alguna tabla no existe")
            elif "no such colum" in str(e):
                print("Algun atributo no existe")
            else:
                print("Consulta no valida")


    else:
        print("Opcion invalida")