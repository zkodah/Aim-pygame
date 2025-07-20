import pygame
import random
import sys
from configuracion import *
from Funciones import draw_text
from pausa import mostrar_menu_pausa
from sens_menu import pedir_configuracion
from escenario import draw_hud, Particula

def juego(screen, cantidad_objetivos, sensibilidad, font, clock):
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    crosshair_pos = [WIDTH // 2, HEIGHT // 2]
    target_pos = (random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS),
                  random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS))

    score = 0
    misses = 0
    total_clicks = 0
    start_time = pygame.time.get_ticks()

    particulas = []

    running = True
    while running:
        dt = clock.tick(60) / 1000
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    opcion = mostrar_menu_pausa(screen, font)
                    if opcion == 0:  # Reanudar
                        continue
                    elif opcion == 1:  # Cambiar sensibilidad
                        _, nueva_sens = pedir_configuracion(screen, font)
                        sensibilidad = nueva_sens
                    elif opcion == 2:  # Salir al menú principal
                        return

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                total_clicks += 1
                distance = ((crosshair_pos[0] - target_pos[0]) ** 2 + (crosshair_pos[1] - target_pos[1]) ** 2) ** 0.5
                if distance <= TARGET_RADIUS:
                    score += 1
                    target_pos = (random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS),
                                  random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS))
                    for _ in range(8):  # Crea partículas de impacto
                        particulas.append(Particula(target_pos))
                    if score >= cantidad_objetivos:
                        running = False
                else:
                    misses += 1

        rel = pygame.mouse.get_rel()
        crosshair_pos[0] += rel[0] * sensibilidad
        crosshair_pos[1] += rel[1] * sensibilidad

        crosshair_pos[0] = max(0, min(WIDTH, crosshair_pos[0]))
        crosshair_pos[1] = max(0, min(HEIGHT, crosshair_pos[1]))

        # Dibujo en pantalla
        screen.fill(WHITE)

        for p in particulas[:]:
            p.update()
            p.draw(screen)
            if p.life <= 0:
                particulas.remove(p)

        pygame.draw.circle(screen, RED, target_pos, TARGET_RADIUS)
        pygame.draw.circle(screen, BLACK, (int(crosshair_pos[0]), int(crosshair_pos[1])), 5)

        draw_hud(screen, score, misses, cantidad_objetivos - score, elapsed_time, font)

        pygame.display.flip()

    pygame.mouse.set_visible(True)
    pygame.event.set_grab(False)
    mostrar_resultado(screen, score, misses, total_clicks, elapsed_time, font)

def mostrar_resultado(screen, score, misses, total_clicks, tiempo_total, font):
    precision = (score / total_clicks) * 100 if total_clicks > 0 else 0
    screen.fill(WHITE)
    draw_text(screen, f"¡Completado!", 100)
    draw_text(screen, f"Aciertos: {score} - Fallos: {misses} - Total Clicks: {total_clicks}", 200)
    draw_text(screen, f"Precisión: {precision:.2f}% - Tiempo: {tiempo_total:.2f}s", 300)
    draw_text(screen, "Pulsa [ESC] para salir o [ENTER] para volver al menú", 400)
    pygame.display.flip()

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    esperando = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
