import pygame
from src.board import Board
WIDTH = 1600 #1800
HEIGHT = 900 #800
MARGIN = 75 #75
BOTTOM_MARGIN = 100
FULLSCREEN = False

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.SCALED)
    if FULLSCREEN:
        pygame.display.toggle_fullscreen()
    pygame.display.set_caption('Sea Battle')
    a = HEIGHT - MARGIN * 2 - BOTTOM_MARGIN
    left = WIDTH - MARGIN - a
    board1 = Board(screen, MARGIN, MARGIN, a)
    board2 = Board(screen, left, MARGIN, a, labels_on_right=True)
    step = 0
    while True:
        event = get_last_event()
        # print(event)
        if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.unicode in ['q', 'Q']:
            break
        if event.type == pygame.KEYDOWN and event.key == 1073741892: # F11 KEY
            pygame.display.toggle_fullscreen()
        if step > 0 and event.type != pygame.MOUSEMOTION:
            continue
        screen.fill((192, 192, 192))

        board1.draw_board(event) # left square
        board2.draw_board(event)   # right square

        pygame.display.flip()
        step += 1
    pygame.quit()


def get_last_event():
    last = None
    for event in pygame.event.get():
        if event.type != pygame.MOUSEMOTION:
            return event
        last = event
    if last is not None:
        return last
    return pygame.event.wait()

if __name__ == '__main__':
    main()
