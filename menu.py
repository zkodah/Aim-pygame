import pygame
import sys
from configuracion import WIDTH, HEIGHT, WHITE, RED, BLACK
from Funciones import draw_text

def menu_configuracion(screen, font):
    opciones = [50, 100, 200]
    seleccion = 0

    while True:
        screen.fill(WHITE)
        draw_text(screen, "Selecciona la cantidad de objetivos", 100)

        for i, cantidad in enumerate(opciones):
            color = RED if i == seleccion else BLACK
            opcion_text = font.render(f"{cantidad} objetivos", True, color)
            screen.blit(opcion_text, (WIDTH // 2 - opcion_text.get_width() // 2, 200 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and seleccion > 0:
                    seleccion -= 1
                if event.key == pygame.K_DOWN and seleccion < len(opciones) - 1:
                    seleccion += 1
                if event.key == pygame.K_RETURN:
                    return opciones[seleccion]
