import pygame
from configuracion import WIDTH, HEIGHT
from menu import menu_configuracion
from juego import juego

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer Modular")
font = pygame.font.SysFont('Arial', 30)
clock = pygame.time.Clock()

while True:
    cantidad_objetivos = menu_configuracion(screen, font)
    juego(screen, cantidad_objetivos, font, clock)
