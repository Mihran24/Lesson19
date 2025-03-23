import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("1st time on pygame")
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
display_surface = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
# Define the background color (RGB format)
background_color = (58,58,58)  # Grey
penguin_image = pygame.transform.scale(
pygame.image.load('hellopenguin.jpg').convert_alpha(), (200, 200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2,
                                              SCREEN_HEIGHT // 230))
# Initialize font, render text, and set text position
text = pygame.font. Font (None, 36).render('Hello Everyone',True, pygame.Color('black'))
text_rect = text.get_rect (center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
