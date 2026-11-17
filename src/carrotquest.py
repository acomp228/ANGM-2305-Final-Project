import pygame
import sys


def main():
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Carrot Quest")
    # Set up clock
    clock = pygame.time.Clock()
    dt = 0
    # Set resolution & create screen
    resolution = ((1000, 1000))
    screen = pygame.display.set_mode(resolution)
    # Start event loop
    running = True
    while running:
        # Define key press behavior
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Fill screen & draw appropriate level geo
        black = pygame.Color(0, 0, 0)
        white = pygame.Color(255, 255, 255)
        screen.fill(black)
        for x in range(0, 1000, 100):
            pygame.draw.line(screen, white, (x, 0), (x, 1000), 1)
        for y in range(0, 1000, 100):
            pygame.draw.line(screen, white, (0, y), (1000, y), 1)
        # Flip displays
        pygame.display.flip()
        # Have clock tick
        clock.tick(12)
    # Quit pygame after event loop is set to false
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
    