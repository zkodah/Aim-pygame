import pygame
import random
import sys

pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 1600, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer - Score & Timer")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont('Arial', 30)

# Configuración sensibilidad y eDPI
DPI_BASE = 1600
eDPI_OBJETIVO = 800 # Ajusta a tu gusto
sensibilidad = eDPI_OBJETIVO / DPI_BASE

crosshair_pos = [WIDTH // 2, HEIGHT // 2]

# Objetivo
TARGET_RADIUS = 30
target_pos = (random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS),
              random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS))

# Contadores
score = 0
misses = 0
total_clicks = 0

# Timer
game_duration = 30  # Duración en segundos
start_ticks = pygame.time.get_ticks()

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

running = True
while running:
    dt = clock.tick(60) / 1000

    # Tiempo restante
    seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    time_left = max(0, game_duration - int(seconds_passed))

    if time_left == 0:
        running = False

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

    score_text = font.render(f"Aciertos: {score}  Fallos: {misses}  Tiempo restante: {time_left}s", True, BLACK)
    screen.blit(score_text, (20, 20))

    pygame.display.flip()

# Mostrar resultado final al terminar
screen.fill(WHITE)
result_text = font.render(f"¡Tiempo finalizado! Aciertos: {score} - Fallos: {misses} - Total Clics: {total_clicks}", True, BLACK)
screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 2))
pygame.display.flip()

pygame.time.wait(5000)
pygame.quit()
