import pygame

class Personaje:

    def __init__(self, nombre=None, superficie=None, rectangulo=None ,score=None, rectangulo_boca=None):
        self.nombre = nombre
        self.superficie = superficie
        self.rectangulo = rectangulo
        self.score = score
        self.rectangulo_boca = rectangulo_boca

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
            self._nombre = nombre

    @property
    def superficie(self):
        return self._superficie

    @superficie.setter
    def superficie(self, superficie):
        self._superficie = superficie

    @property
    def rectangulo(self):
        return self._rectangulo

    @rectangulo.setter
    def rectangulo(self, rectangulo):
        self._rectangulo = rectangulo

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score



    def crear_personaje(self, x, y, ancho, alto):
        self.personaje = Personaje()
        imagen = pygame.image.load("imagenes/01.png")
        imagen = pygame.transform.scale(imagen, (ancho, alto))
        self.personaje.superficie = imagen
        self.personaje.rectangulo = pygame.Rect(x, y, ancho, alto)
        self.personaje.rectangulo_boca = pygame.Rect((x + ancho / 2) - 10, y + 90, 40, 20)
        self.personaje.score = 0

def actualizar_pantalla(self,ventana_ppal):
    ventana_ppal.blit(self.personaje.superficie,self. personaje.rectangulo)
    #pygame.draw.rect(ventana_ppal,colores.ROJO,personaje["rect_homero"])
    #pygame.draw.rect(ventana_ppal,colores.AZUL,personaje["rect_boca"])

def update(personaje,incremento_x):
    nueva_x = personaje.rectangulo.x + incremento_x
    if(nueva_x > 0 and nueva_x < 600):
        personaje.rectangulo.x = personaje.rectangulo.x + incremento_x
        personaje.rectangulo_boca.x = personaje.rectangulo_boca.x + incremento_x

