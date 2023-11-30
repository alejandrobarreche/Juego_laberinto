## LABERINTO ##

# Variables GLOBALES
muro = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))
empezar = ((0, 0),)
salida = ((4, 4),)
ICONO_MURO = "X"
ICONO_ENTRADA = "E"
ICONO_SALIDA = "S"
ESPACIO = " "


'''
La clase Laberinto se encarga de crear el laberinto, es decir, de rellenarlo con los iconos de muro, entrada y salida
así como también se encarga de mostrar por pantalla esta versión inicial del laberinto
'''
class Laberinto:
    # Inicializa variables de instancia
    def __init__(self, muro, empezar, salida, filas, columnas):
        self.laberinto = []
        self.muro = muro
        self.empezar = empezar
        self.salida = salida
        self.filas = filas
        self.columnas = columnas
        
    '''
    self.laberinto : list
    muro : tuple
    empezar : tuple
    salida : tuple
    filas : int
    columnas : int
    '''

    # Esta función rellena la lista laberinto con los símbolos del muro, la entrada y la salida
    def crear_laberinto(self):
        for i in range(self.filas):
            x = []
            for j in range(self.columnas):
                if (i, j) in self.muro:
                    x.append(ICONO_MURO)
                elif (i, j) in self.empezar:
                    x.append(ICONO_ENTRADA)
                elif (i, j) in self.salida:
                    x.append(ICONO_SALIDA)
                else:
                    x.append(ESPACIO)
            self.laberinto.append(x)

    # Esta función muestra por pantalla el laberinto sin el jugador, únicamente para ver el laberinto
    def mostrar_laberinto(self):
        for i in range(len(self.laberinto)):
            for j in range(len(self.laberinto[i])):
                print(self.laberinto[i][j], end=' ')
            print()


'''
Esta clase permite el movimiento, así como muestra por pantalla el laberinto con el icono del jugador en la 
posición en la que se encuentre en dicho momento
'''

class MovimientoLab(Laberinto):

    def __init__(self, muro, empezar, salida, filas, columnas):
        super().__init__(muro, empezar, salida, filas, columnas)
        self.x = 0
        self.y = 0
        self.icono_jugador = "■"
        self.movimientos = []
        
    '''
    self.x : int
    self.y : int
    self.icono_jugador : str
    self.movimientos : list
    '''

    # Vuelve a hacer el laberinto pero añadiendo el icono de jugador donde esté su posición que está dada por (self.x, self.y)
    def cambiar_laberinto(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if (i, j) == (self.x, self.y):
                    self.laberinto[i][j] = self.icono_jugador
                elif (i, j) in self.empezar:
                    self.laberinto[i][j] = ICONO_ENTRADA
                elif (i, j) in self.salida:
                    self.laberinto[i][j] = ICONO_SALIDA
                elif (i, j) in self.muro:
                    self.laberinto[i][j] = ICONO_MURO
                else:
                    self.laberinto[i][j] = ESPACIO


    # Esta función muestra por consola la lista de movimientos que hayas realizado para llegar a la salida
    def mostrar_movimientos(self):
        print("Lista de movimientos:")
        print("[", end="")
        for i, movimiento in enumerate(self.movimientos):
            print(f"{movimiento}", end="")
            if i < len(self.movimientos) - 1:
                print(", ", end="")
        print("]")
        print()
        print("Número de movimientos: ", len(self.movimientos))
            

    # Esta función pregunta hacia dónde quiere ir el jugador y añade a la lista de movimientos hacia dónde se ha movido
    def pedir_donde_mover(self):
        while True:
            direc = input(": ")
            if direc in ["w", "a", "s", "d"]:
                if direc == "w":
                    self.movimientos.append("Arriba")
                elif direc == "a":
                    self.movimientos.append("Izquierda")
                elif direc == "s":
                    self.movimientos.append("Abajo")
                elif direc == "d":
                    self.movimientos.append("Derecha")
                return direc
            else:
                print("Entrada no válida. Introduce 'w', 'a', 's' o 'd'.")

    # Mueve hacia arriba el icono del jugador
    def mover_arriba(self):
        if self.x > 0 and (self.x - 1, self.y) not in self.muro:
            self.x -= 1

    # Mueve hacia abajo el icono del jugador
    def mover_abajo(self):
        if self.x < self.filas - 1 and (self.x + 1, self.y) not in self.muro:
            self.x += 1

    # Mueve hacia la izquierda el icono del jugador
    def mover_izquierda(self):
        if self.y > 0 and (self.x, self.y - 1) not in self.muro:
            self.y -= 1

    # Mueve hacia la derecha el icono del jugador
    def mover_derecha(self):
        if self.y < self.columnas - 1 and (self.x, self.y + 1) not in self.muro:
            self.y += 1

    # Esta función pregunta hacia donde se quiere mover, y en tal caso se mueve. Después  cambia el laberinto y lo muestra por pantalla
    def mover(self):
        while (self.x, self.y) != self.salida[0]:
            direc = self.pedir_donde_mover()
            if direc == "w":
                self.mover_arriba()
            elif direc == "a":
                self.mover_izquierda()
            elif direc == "s":
                self.mover_abajo()
            elif direc == "d":
                self.mover_derecha()
            self.cambiar_laberinto()
            self.mostrar_laberinto()
        
        return (self.x, self.y)

# Esta función la creamos fuera de la clase porque la utilizamos para poner el mensaje de inicio del juego
def empezar_juego():
    print("Vamos a empezar a jugar")
    print("Para moverte usas las teclas w (arriba), a (izquierda), s (abajo), d (derecha).")
    print()
    while True:
        cont = input("Pulsa enter para comenzar y ver el laberinto: ")
        try:
            cont = str(cont)
            if cont == "":
                break
            else:
                print("Pulsa enter para comenzar y ver el laberinto: ")
        except:
            ("Pulsa enter para comenzar y ver el laberinto: ")  
            

# Esta función la creamos fuera de la clase de igual manera porque la utilizamos para acabar el juego
def acabar_juego():
    print("¡ Enhorabuena, has completado el laberinto !")   
    print()


# Esta función es el juego completo
def main():
    lab1 = MovimientoLab(muro, empezar, salida, 5, 5)
    lab1.crear_laberinto()
    empezar_juego()
    lab1.mostrar_laberinto()
    lab1.mover()
    acabar_juego()
    lab1.mostrar_movimientos()

'''
Primero creamos la instancia de la segunda clase
Creamos el laberinto
Muestra el mensaje de inicio del juego
Muestra el primer tablero
Mueve el icono del jugador por el tablero 
Muestra el mensaje al acabar el juego
Muestra la lista de los movimientos
'''

# Llamar a la función main()
if __name__ == "__main__":
    main()