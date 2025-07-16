import pygame
from configuracion import WIDTH, HEIGHT
from menu import menu_configuracion
from sens_menu import pedir_configuracion
from juego import juego

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer Modular")
font = pygame.font.SysFont('Arial', 30)
clock = pygame.time.Clock()

while True:
    dpi, sensibilidad = pedir_configuracion(screen, font)
    sensibilidad_real = sensibilidad
    cantidad_objetivos = menu_configuracion(screen, font)
    juego(screen, cantidad_objetivos, sensibilidad, font, clock)
