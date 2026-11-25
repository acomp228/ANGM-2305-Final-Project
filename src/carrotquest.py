import pygame
import sys
import itertools


class Character():

    def __init__(self, pos=(437, 950), size=30):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(255, 255, 0)
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf

    def draw(self, surface):
        surface.blit(self.surface, self.pos)

    def _update_pos_right(self, surface):
        x, y = self.pos
        x += 100
        self.pos = (x, y)
        surface.blit(self.surface, self.pos)

    def _update_pos_up(self,surface):
        x, y = self.pos
        y -= 100
        self.pos = (x, y)
        surface.blit(self.surface, self.pos)

    def _update_pos_left(self, surface):
        x, y = self.pos
        x -= 100
        self.pos = (x, y)
        surface.blit(self.surface, self.pos)

    def _update_pos_down(self, surface):
        x, y = self.pos
        y += 100
        self.pos = (x, y)
        surface.blit(self.surface, self.pos)


class Enemy():

    def __init__(self, pos=(0,0), size=30):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(255, 0, 0)
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

    def update_position(self, pos, surface):
        self.pos = pos
        surface.blit(self.surface, self.pos)


class EnemyMovement():
    def __init__(self, path):
        self.cycler = itertools.cycle(path)

    def get_next_path(self):
        return next(self.cycler)

class Collectible():
    def __init__(self, pos=(0, 0), size=30):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(255, 165, 0)
        self.surface = self.update_surface()
        

def create_level_geo(screen):
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    green = pygame.Color(0, 150, 0)
    screen.fill(black)
    surf1 = pygame.Surface((200, 400))
    surf1.fill(green)
    surf2 = pygame.Surface((100, 200))
    surf2.fill(green)
    surf3 = pygame.Surface((100, 500))
    surf3.fill(green)
    surf4 = pygame.Surface((100, 300))
    surf4.fill(green)
    surf5 = pygame.Surface((400, 200))
    surf5.fill(green)
    screen.blit(surf1, (400, 600))
    screen.blit(surf2, (300, 600))
    screen.blit(surf2, (600, 600))
    screen.blit(surf3, (200, 200))
    screen.blit(surf3, (700, 200))
    screen.blit(surf4, (100, 300))
    screen.blit(surf4, (800, 300))
    screen.blit(surf5, (300, 100))
    for x in range(0, 1000, 100):
        pygame.draw.line(screen, white, (x, 0), (x, 1000), 1)
    for y in range(0, 1000, 100):
        pygame.draw.line(screen, white, (0, y), (1000, y), 1)


def main():
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Carrot Quest")
    character = Character()
    enemy1 = Enemy((237, 650))
    path1 = [(237, 550), (237, 450), (237, 350), (237, 450), (237, 550), (237, 650)]
    enemypath1 = EnemyMovement(path1)
    enemy2 = Enemy((237, 250))
    path2 = [(337, 250), (437, 250), (537, 250), (637, 250), (737, 250), (637,250),
             (537, 250), (437, 250), (337, 250), (237, 250)]
    enemypath2 = EnemyMovement(path2)
    enemy3 = Enemy((737, 350))
    path3 = [(737, 450), (737, 550), (737, 650), (737, 550), (737, 450), (737, 350)]
    enemypath3 = EnemyMovement(path3)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    character._update_pos_right(screen)
                    new_pos = enemypath1.get_next_path()
                    enemy1.update_position(new_pos, screen)
                    new_pos1 = enemypath2.get_next_path()
                    enemy2.update_position(new_pos1, screen)
                    new_pos2 = enemypath3.get_next_path()
                    enemy3.update_position(new_pos2, screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    character._update_pos_up(screen)
                    new_pos = enemypath1.get_next_path()
                    enemy1.update_position(new_pos, screen)
                    new_pos1 = enemypath2.get_next_path()
                    enemy2.update_position(new_pos1, screen)
                    new_pos2 = enemypath3.get_next_path()
                    enemy3.update_position(new_pos2, screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    character._update_pos_left(screen)
                    new_pos = enemypath1.get_next_path()
                    enemy1.update_position(new_pos, screen)
                    new_pos1 = enemypath2.get_next_path()
                    enemy2.update_position(new_pos1, screen)
                    new_pos2 = enemypath3.get_next_path()
                    enemy3.update_position(new_pos2, screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    character._update_pos_down(screen)
                    new_pos = enemypath1.get_next_path()
                    enemy1.update_position(new_pos, screen)
                    new_pos1 = enemypath2.get_next_path()
                    enemy2.update_position(new_pos1, screen)
                    new_pos2 = enemypath3.get_next_path()
                    enemy3.update_position(new_pos2, screen)
        # Fill screen & draw appropriate level geo
        create_level_geo(screen)
        character.draw(screen)
        enemy1.draw(screen)
        enemy2.draw(screen)
        enemy3.draw(screen)
        # Flip displays
        pygame.display.flip()
        # Have clock tick
        clock.tick(12)
    # Quit pygame after event loop is set to false
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
    