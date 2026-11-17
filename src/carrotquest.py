import pygame


def main():
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Carrot Quest")
    # Set up clock
    clock = pygame.time.Clock()
    dt = 0
    # Set resolution & create screen
    resolution = ((2560, 1440))
    screen = pygame.display.set_mode(resolution)
    # Start event loop
    running = True
    while running:
        # Define key press behavior
        # Fill screen & draw appropriate level geo
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        # Flip displays
        pygame.display.flip()
        # Have clock tick
        dt = clock.tick(12)
    # Quit pygame after event loop is set to false
    pygame.quit()


    if __name__ == "__main__":
        main()
    