import pygame


WIDTH, HEIGHT = 600, 400



def main():
    run = True
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Brownian Motion")
    clock = pygame.time.Clock()

    while run:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


    pygame.quit()

if __name__ == '__main__':
    main()