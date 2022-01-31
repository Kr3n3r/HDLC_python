# Se desea programar “el juego de la ruleta de la fortuna” en Python3(PSe Int originalmente) 
# utilizando programación modular. 
# Para ello, en el programa principal definirá una matriz de 10x10.
# Además, solicitará al Jugador1 el texto que deberá buscar el Jugador2 (la aplicación debe controlar que sea menor a 100 letras, 
# para solicitar nuevo mensaje si no lo es).
# Este mensaje, que se introducirá en la matriz original con todos los valores iniacializados a V (de Vacio), 
# se desplegará letra a letra en la matriz, sustituyendo las “V” por la letra correspondiente en mayúsculas, 
# o espacio en blanco si lo hubiera. 
# A partir de ahí, en cada movimiento del Jugador 2 (único que juega), se solicitará una consonante
# (el programa debe controlar que se consonante). 
# Tras cada consonante, el programa debe mostrar el tablero de juego, con X donde deba ir letra. 
# Este tablero de juego mostrará solo el número de líneas correspondiente al mensaje de juego, 
# mostrando V en los espacios existentes tras la finalización del mensaje.
# (p.ej.: si tiene 43 letras, contando blancos, solo mostrará 5 líneas). Consideraciones:
        #  1.1. Jugador 2 puede fallar en 3 consonantes. El cuarto error supondrá la finalización del juego.
        #  1.2. Puede solicitar una vocal. El programa controlará que no pida ninguna más.
        #  1.3. Debe aparecer en cada jugada un mensaje solicitando resolver. 
        #       Sólo la pulsación de la tecla “s” llevará a resolver.
        #       Si falla el jugador, se seguirá jugando si quedan consonantes. 
        #       El intento de resolución fallido es equivalente a fallar con una consonante.

from ast import While


def __main__():
    tablero = [[""] * 10 for i in range(10)] # Definimos el tablero de juego, por ahora vacío
    tabMens = [[""] * 10 for i in range(10)] # Definimos el tablero con el mensaje, por ahora vacío
    mensaje = str() # Definimos la variable que almacenará el mensaje a adivinar
    
    j = bool()
    entrada = str()
    
    mensaje = ''
    entrada = ''
    j = False
    
    print("Desea jugar a la Ruleta de la Fortuna (S/N): ")
    entrada = input()
    
    if entrada == 's' | entrada == 'S':
        j = True
    
    while j :
        inicializaTablero(tablero)                
        inicializaTablero(tabMens)
        mensaje = solicitaMensaje()
__main__()