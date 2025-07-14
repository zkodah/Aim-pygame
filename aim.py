import pygame
import random
import sys

pygame.init()

# Pantalla y colores
WIDTH, HEIGHT = 1600, 1000
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer - Modo Objetivos + Timer")

font = pygame.font.SysFont('Arial', 30)
clock = pygame.time.Clock()

# Configuración sensibilidad y eDPI
DPI_BASE = 1600
eDPI_OBJETIVO = 800
sensibilidad = eDPI_OBJETIVO / DPI_BASE

TARGET_RADIUS = 30


def draw_text(text, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, y))


def menu_configuracion():
    opciones = [50, 100, 200]
    seleccion = 0

    while True:
        screen.fill(WHITE)
        draw_text("Selecciona la cantidad de objetivos", 100)

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


def juego(cantidad_objetivos):
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    crosshair_pos = [WIDTH // 2, HEIGHT // 2]
    target_pos = (random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS),
                  random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS))

    score = 0
    misses = 0
    total_clicks = 0

    start_time = pygame.time.get_ticks()

    running = True
    while running:
        dt = clock.tick(60) / 1000

        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # en segundos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                total_clicks += 1
                distance = ((crosshair_pos[0] - target_pos[0]) ** 2 + (crosshair_pos[1] - target_pos[1]) ** 2) ** 0.5
                if distance <= TARGET_RADIUS:
                    score += 1
                    target_pos = (random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS),
                                  random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS))
                    if score >= cantidad_objetivos:
                        running = False
                else:
                    misses += 1

        rel = pygame.mouse.get_rel()
        crosshair_pos[0] += rel[0] * sensibilidad
        crosshair_pos[1] += rel[1] * sensibilidad

        crosshair_pos[0] = max(0, min(WIDTH, crosshair_pos[0]))
        crosshair_pos[1] = max(0, min(HEIGHT, crosshair_pos[1]))

        screen.fill(WHITE)
        pygame.draw.circle(screen, RED, target_pos, TARGET_RADIUS)
        pygame.draw.circle(screen, BLACK, (int(crosshair_pos[0]), int(crosshair_pos[1])), 5)

        draw_text(f"Aciertos: {score}  Fallos: {misses}  Objetivos restantes: {cantidad_objetivos - score}", 20)
        draw_text(f"Tiempo: {elapsed_time:.2f}s", 60)
        pygame.display.flip()

    pygame.mouse.set_visible(True)
    pygame.event.set_grab(False)

    mostrar_resultado(score, misses, total_clicks, elapsed_time)


def mostrar_resultado(score, misses, total_clicks, tiempo_total):
    precision = (score / total_clicks) * 100 if total_clicks > 0 else 0
    screen.fill(WHITE)
    draw_text(f"¡Completado!", 100)
    draw_text(f"Aciertos: {score} - Fallos: {misses} - Total Clicks: {total_clicks}", 200)
    draw_text(f"Precisión: {precision:.2f}%  -  Tiempo total: {tiempo_total:.2f}s", 300)
    draw_text("Pulsa [ESC] para salir o [ENTER] para volver al menú", 400)
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


# Bucle Principal
while True:
    cantidad_objetivos = menu_configuracion()
    juego(cantidad_objetivos)
