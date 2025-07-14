import pygame
from configuracion import WIDTH, BLACK, FONT_SIZE

pygame.font.init()
font = pygame.font.SysFont('Arial', FONT_SIZE)

def draw_text(screen, text, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, y))
