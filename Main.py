import pygame

import clases.Dona
import propiedades.colores
from clases.Dona import *
from propiedades.colores import *
from clases.Dona import Dona
from clases.Personaje import Personaje

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()

# TAMAO DE LA VENTANA
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

# TITULO DE LA VENTANA
pygame.display.set_caption("PYGAME HOMERO COME DONAS")

# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer, 100)

# CREACIN DE ELEMENTOS
personaje = Personaje()
dona = Dona()
player = personaje.crear_personaje(ANCHO_VENTANA / 2, ALTO_VENTANA - 200, 200, 200)
lista_donas = clases.Dona.crear_lista_donas(20)

# LGICA DEL JUEGO
flag_run = True
while flag_run:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                dona.update(lista_donas)

    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_LEFT]:
        personaje.update(player, -2)
    if lista_teclas[pygame.K_RIGHT]:
        personaje.update(player, 2)

    # VOLCAR CAMBIOS
    ventana_ppal.fill(propiedades.colores.BLANCO)
    clases.Personaje.actualizar_pantalla(player, ventana_ppal)
    dona.actualizar_pantalla(lista_donas, player, ventana_ppal)

    pygame.display.flip()
pygame.quit()