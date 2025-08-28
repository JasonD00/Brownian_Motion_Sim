import pygame
import random



WIDTH, HEIGHT = 600, 400
NUM_PARTICLES = 50

# Particle class
# -- X and Y is set to a random number in the windows Width and Height
class Particle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)

    # Surface is taken as argument, and a circle is drawn. Drawn in a radius of 1px
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), 1)

# Main
def main():
    run = True # Control game loop
    pygame.init() # Initialize Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Brownian Motion")
    clock = pygame.time.Clock() # Frame rate

    particles = [Particle() for _ in range(NUM_PARTICLES)]

    # Game loop
    while run:

        clock.tick(60) # FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for p in particles:
            p.draw(screen)

        pygame.display.flip()


    pygame.quit()

if __name__ == '__main__':
    main()