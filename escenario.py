import pygame
import random
from configuracion import WIDTH, HEIGHT, WHITE, BLACK

# ---------- Fondo dinámico (líneas) ----------
class LineaFondo:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.length = random.randint(50, 150)
        self.speed = random.uniform(1, 3)

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-HEIGHT, 0)
            self.x = random.randint(0, WIDTH)

    def draw(self, screen):
        pygame.draw.line(screen, (50, 50, 255), (self.x, self.y), (self.x, self.y + self.length), 1)


# ---------- Partículas de impacto ----------
class Particula:
    def __init__(self, pos):
        self.x, self.y = pos
        self.size = random.randint(2, 4)
        self.color = (255, 100, 100)
        self.vel = [random.uniform(-2, 2), random.uniform(-2, 2)]
        self.life = 30

    def update(self):
        self.x += self.vel[0]
        self.y += self.vel[1]
        self.size *= 0.95
        self.life -= 1

    def draw(self, screen):
        if self.life > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))


# ---------- Estructura del campo de tiro ----------
def draw_escenario_3d_fake(screen):
    # Fondo general
    screen.fill((200, 200, 200))

    # Pared trasera
    pygame.draw.rect(screen, (160, 160, 160), (150, 100, WIDTH - 300, HEIGHT - 300))

    # Suelo
    pygame.draw.rect(screen, (120, 120, 120), (0, HEIGHT - 200, WIDTH, 200))

    # Techo
    pygame.draw.rect(screen, (120, 120, 120), (0, 0, WIDTH, 100))

    # Laterales
    pygame.draw.rect(screen, (100, 100, 100), (0, 0, 150, HEIGHT))
    pygame.draw.rect(screen, (100, 100, 100), (WIDTH - 150, 0, 150, HEIGHT))

    # Bloques al fondo
    pygame.draw.rect(screen, (80, 80, 80), (WIDTH - 300, HEIGHT - 400, 80, 80))
    pygame.draw.rect(screen, (80, 80, 80), (WIDTH - 380, HEIGHT - 500, 100, 100))


# ---------- HUD con transparencia ----------
def draw_hud(screen, score, misses, objetivos_restantes, elapsed_time, font):
    hud_surface = pygame.Surface((420, 110), pygame.SRCALPHA)
    hud_surface.fill((0, 0, 0, 150))
    screen.blit(hud_surface, (10, 10))
    pygame.draw.rect(screen, (0, 255, 255), (10, 10, 420, 110), 2)

    texto1 = font.render(f"Aciertos: {score}  Fallos: {misses}", True, WHITE)
    texto2 = font.render(f"Restantes: {objetivos_restantes}  Tiempo: {elapsed_time:.2f}s", True, WHITE)
    screen.blit(texto1, (20, 20))
    screen.blit(texto2, (20, 70))
