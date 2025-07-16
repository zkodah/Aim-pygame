import pygame
import sys
from configuracion import WIDTH, HEIGHT, WHITE, BLACK
from Funciones import draw_text


def pedir_configuracion(screen, font):
    user_dpi = ""
    user_sens = ""
    etapa = "dpi"  # Cambia a 'sens' después del DPI

    while True:
        screen.fill(WHITE)
        draw_text(screen, "Configuración de Sensibilidad", 50)

        draw_text(screen, f"DPI de Mouse: {user_dpi}", 200)
        draw_text(screen, f"Sensibilidad en Juego: {user_sens}", 300)

        if etapa == "dpi":
            draw_text(screen, "↳ Ingrese su DPI y presione ENTER", 400)
        else:
            draw_text(screen, "↳ Ingrese su Sensibilidad y presione ENTER", 400)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if etapa == "dpi" and user_dpi != "":
                        etapa = "sens"
                    elif etapa == "sens" and user_sens != "":
                        try:
                            dpi = int(user_dpi)
                            sens = float(user_sens)
                            return dpi, sens
                        except ValueError:
                            user_dpi = ""
                            user_sens = ""
                            etapa = "dpi"
                elif event.key == pygame.K_BACKSPACE:
                    if etapa == "dpi":
                        user_dpi = user_dpi[:-1]
                    elif etapa == "sens":
                        user_sens = user_sens[:-1]
                elif event.unicode.isdigit() or (event.unicode == '.' and etapa == "sens"):
                    if etapa == "dpi":
                        user_dpi += event.unicode
                    elif etapa == "sens":
                        user_sens += event.unicode
