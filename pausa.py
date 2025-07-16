import pygame
import sys
from configuracion import WHITE, BLACK, WIDTH, HEIGHT
from Funciones import draw_text


def mostrar_menu_pausa(screen, font):
    opciones = ["Reanudar", "Cambiar Sensibilidad", "Salir al Menú Principal"]
    seleccion = 0

    while True:
        screen.fill(WHITE)
        draw_text(screen, "PAUSA - Selecciona una opción", 100)

        for i, opcion in enumerate(opciones):
            color = (255, 0, 0) if i == seleccion else BLACK
            opcion_text = font.render(opcion, True, color)
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
                    return seleccion  # Devuelve el índice de la opción seleccionada
