import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode([1250, 800])
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break
        screen.fill((255, 255, 255))
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
