import pygame

# Ustawienia okna
display_size = (600, 600)
center = (display_size[0] // 2, display_size[1] // 2)

pygame.init()
screen = pygame.display.set_mode(display_size)
pygame.display.set_caption("Custom Shape in Pygame")

# Kolory
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Figury
def draw_custom_shape(surface, position):
    rect_width, rect_height = 300, 300
    tri_width, tri_height = 300, 150
    
    # prostokąt
    rect_x = position[0] - rect_width // 2
    rect_y = position[1] - rect_height // 2
    pygame.draw.rect(surface, GREEN, (rect_x, rect_y, rect_width, rect_height))
    
    # trójkąt
    triangle_points = [
        (position[0] - tri_width // 2, position[1] + rect_height // 2),
        (position[0] + tri_width // 2, position[1] + rect_height // 2),
        (position[0], position[1] + rect_height // 2 - tri_height)
    ]
    pygame.draw.polygon(surface, WHITE, triangle_points)


running = True
while running:
    screen.fill(WHITE)
    
    draw_custom_shape(screen, center)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()