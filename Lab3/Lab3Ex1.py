import pygame
import math

pygame.init()

# Ustawienia okna
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Transforms in Pygame")

# Czcionka
font = pygame.font.SysFont("Arial", 20)

def identity(x, y):
    return x, y

def trans1(x, y):
    return 0.35 * x, 0.35 * y

def trans2(x, y):
    theta = math.radians(60)
    return x * math.cos(theta) - y * math.sin(theta), x * math.sin(theta) + y * math.cos(theta)

def trans3(x, y):
    sx, sy = -0.3 * x, 0.8 * y
    return -sx, -sy  # obrót 180°

def trans4(x, y):
    return x + 0.35 * y, y

def trans5(x, y):
    sx, sy = x, 0.3 * y
    return sx, sy

def trans6(x, y):
    sh_x, sh_y = x, y - 0.3 * x
    return sh_x, -sh_y

def trans7(x, y):
    sx, sy = 0.3 * x, 0.9 * y
    return -sx, -sy

def trans8(x, y):
    theta = math.radians(45)
    rx = x * math.cos(theta) - y * math.sin(theta)
    ry = x * math.sin(theta) + y * math.cos(theta)
    tx, ty = rx, ry + 300
    return tx, 0.3 * ty

def trans9(x, y):
    rx, ry = -x, -y  # obrót 180°
    sx = rx
    sy = 0.4 * rx + ry
    return sx - 100, sy

# Mapa transformacji
transforms = {
    0: identity,
    1: trans1,
    2: trans2,
    3: trans3,
    4: trans4,
    5: trans5,
    6: trans6,
    7: trans7,
    8: trans8,
    9: trans9
}

current_transform = 0

n_sides = 18
radius = 150
polygon = []
for i in range(1, n_sides + 1):
    angle = 2 * math.pi * i / n_sides
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    polygon.append((x, y))

# Definicja 
buttons = []
button_width = 50
button_height = 30
margin = 5
start_x = margin
start_y = HEIGHT - button_height - margin
labels = ["None"] + [f"No. {i}" for i in range(1, 10)]
for i, label in enumerate(labels):
    rect = pygame.Rect(start_x + i * (button_width + margin), start_y, button_width, button_height)
    buttons.append({"rect": rect, "label": label, "transform": i})

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button["rect"].collidepoint(pos):
                    current_transform = button["transform"]

    screen.fill((255, 255, 255))
    
    transformed_points = []
    for x, y in polygon:
        tx, ty = transforms[current_transform](x, y)
        final_x = tx + 300
        final_y = ty + 300
        transformed_points.append((final_x, final_y))

    pygame.draw.polygon(screen, (0, 0, 255), transformed_points)

    for button in buttons:
        rect = button["rect"]
        if button["transform"] == current_transform:
            color = (180, 180, 250)
        else:
            color = (200, 200, 200)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)  # obrys przycisku
        label_surface = font.render(button["label"], True, (0, 0, 0))
        label_rect = label_surface.get_rect(center=rect.center)
        screen.blit(label_surface, label_rect)
    
    info_text = font.render(f"Transform: {current_transform}", True, (0, 0, 0))
    screen.blit(info_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
