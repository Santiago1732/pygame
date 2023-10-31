from typing import Any

import pygame
import random
import propiedades.colores

class Dona:

    def __init__(self, superficie=None, rectangulo=None, visible=None, speed=None):
        self.superficie = superficie
        self.rectangulo = rectangulo
        self.visible = visible
        self.speed = speed

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
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, visible):
        self._visible = visible

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    def actualizar_pantalla(lista_donas, personaje, ventana_ppal):
        for dona in lista_donas:
            if (personaje.rectangulo_boca.colliderect(dona.rectangulo)):
                personaje.score = personaje.score + 1
                lista_donas.restar_dona(dona)

            if (dona.rectangulo.y > 800):
                lista_donas.restar_dona(dona)
            ventana_ppal.blit(dona.superficie, dona.rectangulo)
            # pygame.draw.rect(ventana_ppal,colores.ROJO,dona["rect"])

        font = pygame.font.SysFont("Courier new", 50, False, True)
        text = font.render("Score: {0}".format(personaje.score), True, propiedades.colores.NEGRO)
        ventana_ppal.blit(text, (0, 0))


def crear(x, y, ancho, alto):
    # Leer una imagen
    imagen_dona = pygame.image.load("imagenes/00.png")
    imagen_dona = pygame.transform.scale(imagen_dona, (ancho, alto))
    rect_dona = imagen_dona.get_rect()
    rect_dona.x = x
    rect_dona.y = y

    dona = Dona()
    dona.superficie = imagen_dona
    dona.rectangulo = rect_dona
    dona.visible = True
    dona.speed = random.randrange(10, 20, 1)
    return dona


def update(lista_donas):
    for dona in lista_donas:
        rect_dona = dona.rectangulo
        rect_dona.y = rect_dona.y + dona.speed





def crear_lista_donas(cantidad):
    lista_donas = []
    for i in range(cantidad):
        y = random.randrange(-1000, 0, 60)
        x = random.randrange(0, 740, 60)
        lista_donas.append(crear(x, y, 60, 60))
    return lista_donas


def restar_dona(dona):
    dona.rectangulo.x = random.randrange(0, 740, 60)
    dona.rectangulo.y = random.randrange(-1000, 0, 60)
