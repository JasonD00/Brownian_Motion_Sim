import pygame
import random
import math


WIDTH, HEIGHT = 600, 400
NUM_PARTICLES = 50
MOVE_SIZE = 2


# Particle class
# -- X and Y is set to a random number in the windows Width and Height
class Particle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        # dir: angle, math.pi * 2 is a full circle, rand.uniform picks number between 0 and a full circle
        self.angle = random.uniform(0, math.pi * 2)

    def move(self):

        # Calc the horizontal distance to move, takes the angle and moves X co-ord
        self.x += math.cos(self.angle) * MOVE_SIZE
        # Calc the vertical distance to move, move the Y co-ord
        self.y += math.sin(self.angle) * MOVE_SIZE

        # Contain particles within width and height of the screen, 0 and -1
        self.x %= WIDTH
        self.y %= HEIGHT


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

    # New surface
    fading_surface = pygame.Surface((WIDTH, HEIGHT))

    # List Comprehension
    particles = [Particle() for _ in range(NUM_PARTICLES)]

    # Game loop
    while run:

        clock.tick(60) # FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Fade out trailing lines of particles, keeps 1px particle
        fading_surface.fill((0,0,0))


        for p in particles:
            p.move()
            p.draw(fading_surface) # Draw particle as a fading surface

        # -- Block Transfer. copy pixel from one surface to another --
        # Blit transfers drawing onto the screen every frame
        screen.blit(fading_surface, (0, 0))
        pygame.display.flip() # Updates the physical display


    pygame.quit()

if __name__ == '__main__':
    main()