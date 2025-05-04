import pygame

WIDTH = 800
HEIGHT = 600


def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    step = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 255), (WIDTH // 2, HEIGHT // 2), 50)
        red_square = pygame.Rect((50, 50), (100, 100))
        pygame.draw.rect(screen, (200, 0, 0), red_square, 1)
        text_font = pygame.font.SysFont("any_font", 60)
        text_block = text_font.render("Hello, World! From Pygame " + str(step), False, (200, 100, 0))
        screen.blit(text_block, (50, HEIGHT - 50))
        pygame.display.flip()
        step += 1


if __name__ == '__main__':
    main()
