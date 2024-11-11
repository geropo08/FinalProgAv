
import random
from typing import List, Tuple, Callable, Generator, Optional

#Decorador que cobre la funcion principal, que muestra el numero de pregunta y los puntos que tenes luego de responder
def decorador(func: Callable) -> Callable:
    
    def wrapper(*args,**kwargs):
        numero_preg=6-int(len(args[0][1])/2) #Como se quitan opciones a medida que el juego avanza, dependiendo de cuantas opciones haya es el numero de pregunta
        print(f"Pregunta: {numero_preg}")
        res= func(*args, **kwargs)
        if(numero_preg==5):
            print(f"El juego ha terminado, usted consiguio {res[1]} puntos")
        else:
            print(f"Tenes {res[1]} puntos\n")
        return res
    return wrapper

#Generador, que agarra una categoria a traves de un Send y devuelve una respuesta random de la misma
#Devuelve un generador que puede devolver un string o nada, puede recibir un string o nada(cuando se inicializa) y como el generador no tiene fin no devuelva nada al final.
def respuestas_por_categoria(preguntas:List[List[str]])->Generator[Optional[str], Optional[str], None]:

    categoria = None
    while True:
        if categoria is None:
            #Espera a recibir una categoria
            categoria=yield
        else:
            #filtra las preguntas de la categoria
            preguntas_categoria=list(filter(lambda x: x[2]==categoria,preguntas))
            
            #agarra 2 indices random
            indice=random.sample(range(0, len(preguntas_categoria)), 2)
            
            #Como son 2 preguntas random dentro de la categoria, primero pide una y despues la otra
            yield preguntas_categoria[indice[0]][1]

            yield preguntas_categoria[indice[1]][1]
            
            #Espera para que le ingresen otra categoria
            categoria=yield


def recursion_respuestas(respuestas: Generator[Optional[str], Optional[str], None] , lista_opciones: List[str], categorias:List[str], respuestas_reales:List[str]) -> List[str]:
    """
    Recursion que consigue todas las opciones de cada pregunta, EJ: si son 5 preguntas, devuelve 10 opciones, 2 por pregunta.

    Args:
        respuestas (Generator): Es el generador que filtra por categoria y se le pide cada opcion.
        lista_opciones (List[str]): Es el acumulador de la recursion, cada iteracion se le suman 2 opciones
        categorias (List[str]): Lista de categorias de este juego (5)
        respuestas_reales (List[str]): Lista de respuestas correctas de la pregunta
    Returns:
        List[str]: Devuelve una lista de las opciones
    
    """
    
    #Verifica que haya categorias para buscar las opciones si no hay, termina
    if(len(categorias)==0):
        return lista_opciones
    
    #Mueve el generador para que acepte una categoria
    next(respuestas)
    r1=respuestas.send(categorias[0]) #Se le envia la categoria y le devuelve 1 opcion
    r2=next(respuestas) #Se le pide otra opcion
    
    if(respuestas_reales[0]==r1 or respuestas_reales[0]==r2): #Verifica que las opciones no se repitan con la correcta
        return recursion_respuestas(respuestas,lista_opciones,categorias,respuestas_reales) #Si se repite vuelve a pedir 2 opciones
    else:
        #Guarda en la lista las opciones
        lista_opciones.append(r1) 
        lista_opciones.append(r2)
        #Quito la categoria y la respuesta de la pregunta para que en la siguiente iteracion haga la proxima pregunta
        categorias_nuevo=categorias[1:]
        respuestas_nuevo=respuestas_reales[1:]
        return recursion_respuestas (respuestas, lista_opciones, categorias_nuevo, respuestas_nuevo)

 
def preguntas_random(preguntas:List[List[str]]) -> Tuple[List[List[str]], List[str]]:
    """
    Toma un conjunto de preguntas y elije 5 de ellas con sus respectivas opciones para formar una terna de opciones por pregunta.

    Args:
        preguntas preguntas(List[List[str]]): Lista de preguntas, la primera columa es la pregunta la segunda la respuesta y la tercera la categoria.
        
    Returns:
        Tuple[List[List[str]], List[str]]: Devuelve una tupla la primera parte es la lista de las preguntas y la segunda la lista de las opciones
    
    """
    #Agarra 5 numeros random para usarlos de indices y buscar las preguntas
    numeros=random.sample(range(0, len(preguntas)), 5)
    preguntas_seleccionadas = [preguntas[i] for i in numeros] #Guarda las preguntas seleccionadas
    categorias=[preguntas[i][2] for i in numeros] #Crea una lista con las categorias para usar en recursion_respuestas
    correctas=[preguntas[i][1] for i in numeros] #Crea una lista con las respuestas correctas para usar en recursion_respuestas

    respuestas=respuestas_por_categoria(preguntas) #Crea el generador con todas las preguntas
    
    lista_respuestas_rand=recursion_respuestas(respuestas,[],categorias,correctas) #Elije las 10 opciones, 2 para cada pregunta



    
    return preguntas_seleccionadas, lista_respuestas_rand

#Funcion Bind de Monadas
def bind(func:Callable, tuple: Tuple[Tuple[List[List[str]], List[str]], int]) ->Tuple[Tuple[List[List[str]], List[str]], int]:
    """
    Funcion bind para que el juego ejecute una pregunta luego de la otra

    Args:
        func (callable): Recibe la funcion juego que es donde se realiza todo
        tuple: Recibe una tupla que son los mismos args que recibe juego para que se ejecute la prox
    Returns:
        Tuple[Tuple[List[List[str]], List[str]], int] 

    """
    res = func(tuple[0],tuple[1])
    return res

#Necesario para usar monadas, es el inicializador del juego
def unit(preguntas: Tuple[List[List[str]], List[str]]) -> Tuple[Tuple[List[List[str]], List[str]], int]:
    return preguntas,0

def verificador(opciones_map:dict[str, str], ingreso:str, respuesta:str)->bool:
    """
    Funcion que verifica si una respuesta dada por el jugador es correcta
    Args:
        opciones_map (dict[str, str]): Recibe un diccionario con lo que dice la opcion y a que letra corresponde
        ingreso (str): Letra que ingreso el jugador
        respuesta (str): Respuesta correcta de la pregunta
    Returns:
        bool

    """
    #Verifica lo que ingreso y lo compara con la respuesta real
    if ingreso in opciones_map and opciones_map[ingreso] == respuesta:
        return True
    else:
        return False


@decorador

def juego(preguntas:Tuple[List[List[str]], List[str]], pts:int) -> Tuple[Tuple[List[List[str]], List[str]], int]:

    """
    Funcion principal del juego, donde se imprimen las opciones y se comprueba si la respuesta es correcta

    Args:
        preguntas (Tuple[List[List[str]], List[str]]): Recibe una tupla, donde el primer elemento son las preguntas con su respuesta y el segundo elemento son las opciones
        pts: puntos acumulados del juego
    Returns:
        Tuple[Tuple[List[List[str]], List[str]], int]  Retorna la tupla quitando la pregunta y opciones ya usadas y el puntaje actualizado

    """

    #Primero calcula en que pregunta estamos
    numero_pregunta= 5 - int(len(preguntas[1])/2)
    #Crea una lista de las opciones, primero la correcta y ;uego las 2 aleatorias pero de la misma categoria.
    opciones=[preguntas[0][numero_pregunta][1],preguntas[1][0],preguntas[1][1]]
    random.shuffle(opciones) #Las cambia de orden
    print(preguntas[0][numero_pregunta][0]+"\n"+"Opciones: a-"+opciones[0]+" b-"+opciones[1]+" c-"+opciones[2]) #Imprime las opciones
    opcionesLetra = ['a', 'b', 'c']
    
     #Pide que ingrese una opcion

    # Crea mapa de respuesta (a,b,c) y les asigna las opciones
    opciones_map = {
        "a": opciones[0],
        "b": opciones[1],
        "c": opciones[2]
    }
    #consulta si ingreso a, b o c y verifica que la opcion sea correcta comparandola con la original
    if verificador(opciones_map, random.choice(opcionesLetra), preguntas[0][numero_pregunta][1]):
        #suma 10 pts
        pts += 10
        print("Respuesta Correcta!")
    else:
        print(f"Incorrecto! La respuesta era {preguntas[0][numero_pregunta][1]}")
    #Quita 2 opciones de la lista para ir con las siguientes
    nuevas_respuestas=preguntas[1][2:]
    
    #Aumenta el contador
    return (preguntas[0],nuevas_respuestas), pts

#Funcion que inicia el juego
def iniciar(datos:List[List[str]]):
    """
    Funcion que inicia el juego

    Args:
        preguntas [List[List[str]]: Datos recibidos del csv

    """
    preguntas = preguntas_random(datos)
    return bind(juego,bind(juego,bind(juego,bind(juego,bind(juego,unit(preguntas))))))
    

    


