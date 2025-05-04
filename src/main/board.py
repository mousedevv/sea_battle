import pygame

from src.main.cell import Cell

SHIP_COLOR = (240, 0, 0)

ALPHABET = "ABCDEFGHIJKLMNOPRSTUWXYZ" * 10
TEXT_SIZE = 80  # 100 for SIZE = 8, 80 for SIZE = 10
BLACK = (0, 0, 0)
FRAME_COLOR = (0, 0, 255)
HIGHLIGHTED_CELL_COLOR, HIGHLIGHTED_CELL_WIDTH = (0, 255, 0), 3
DEFAULT_CELL_COLOR, DEFAULT_CELL_WIDTH = (0, 0, 255), 1

SHIPS = {      # from left and bottom of board
    1: {'amount': 4, 'cells_x': 2, 'cells_y': 0},
    2: {'amount': 3, 'cells_x': 1.5, 'cells_y': 1},
    3: {'amount': 2, 'cells_x': 6, 'cells_y': 1},
    4: {'amount': 1, 'cells_x': 5.5, 'cells_y': 0}
}  # ship length: numbers of ships
# ex. SHIPS[3]

SIZE = 10  # sqr root of cells, WIDTH and HEIGHT of board


class Board:
    def __init__(self, screen, left, top, a, labels_on_right=False):
        self.screen = screen
        self.left = left
        self.top = top
        self.a = a // SIZE * SIZE
        self.cell_a = self.a / SIZE  # (HEIGHT - MARGIN * 2 - BOTTOM_MARGIN) / SIZE   # one cell length
        self.board = {}
        self.ship_label_font = pygame.font.SysFont("any_font", TEXT_SIZE)
        self.labels_on_right = labels_on_right
        self.text_blocks_rows, self.text_blocks_cols = self.name_rows_and_cols()
        for x in range(SIZE):
            for y in range(SIZE):
                self.board[x, y] = Cell()

    @staticmethod
    def name_rows_and_cols():
        text_font = pygame.font.SysFont("any_font", TEXT_SIZE)
        cols_list, rows_list = [], []
        for i in range(SIZE):
            cols_list.append(text_font.render(ALPHABET[i], True, BLACK))
            rows_list.append(text_font.render(str(i + 1), True, BLACK))
        return rows_list, cols_list

    def get_highlighted_cell(self, cursor_x, cursor_y):
        cursor_x = cursor_x - self.left
        cursor_y = cursor_y - self.top
        x = cursor_x // self.cell_a
        y = cursor_y // self.cell_a
        if 0 <= x < SIZE and 0 <= y < SIZE:
            return x, y
        return None

    @staticmethod
    def get_cursor_position(event):
        try:
            return event.pos[0], event.pos[1]
        except AttributeError:
            return 0, 0

    def ships_start_spawn(self):
        padding = self.cell_a / 10
        for size, config in SHIPS.items():
            amount = config['amount']
            cell_x = config['cells_x']
            cell_y = config['cells_y']
            ship_left = self.left + cell_x * self.cell_a + padding
            ship_w = self.cell_a * size - padding * 2
            ship_top = self.top + self.a + cell_y * self.cell_a + padding
            ship_rect = pygame.Rect(
                (ship_left, ship_top),
                (ship_w, self.cell_a - padding * 2)
            )
            pygame.draw.rect(self.screen, SHIP_COLOR, ship_rect)
            ship_count_text = self.ship_label_font.render(str(amount), True, BLACK)
            ship_text_size_w = ship_count_text.get_size()[0]
            self.screen.blit(ship_count_text, (ship_left + ship_w / 2 - ship_text_size_w / 2, ship_top))

    def draw_board(self, event):
        self.draw_empty_board()
        self.ships_start_spawn()
        cursor_x, cursor_y = self.get_cursor_position(event)
        highlighted_cell = self.get_highlighted_cell(cursor_x, cursor_y)
        if highlighted_cell is not None:
            self.draw_cell(highlighted_cell[0], highlighted_cell[1], True)


    def draw_empty_board(self):
        outside_sqr = pygame.Rect((self.left, self.top), (self.a, self.a))
        pygame.draw.rect(self.screen, FRAME_COLOR, outside_sqr, 5)
        self.label_rows()
        self.label_cols()
        for x in range(SIZE):
            for y in range(SIZE):
                self.draw_cell(x, y, False)

    def label_rows(self):
        for row in range(SIZE):
            text_w, text_h = self.text_blocks_rows[row].get_size()
            offset_y = (self.cell_a - text_h) / 2
            offset_left = self.left - text_w - 10
            if self.labels_on_right:
                offset_left += self.a + text_w + 20
            self.screen.blit(self.text_blocks_rows[row], (offset_left, self.top + row * self.cell_a + offset_y))

    def label_cols(self):
        for col in range(SIZE):
            text_w, text_h = self.text_blocks_cols[col].get_size()
            offset_x = (self.cell_a - text_w) / 2
            self.screen.blit(self.text_blocks_cols[col], (self.left + col * self.cell_a + offset_x, self.top - text_h))

    def draw_cell(self, x, y, is_highlighted):
        m = 3 if is_highlighted else 0  # cell margin / padding
        cell_sqr = pygame.Rect(
            (self.left + x * self.cell_a + m, self.top + y * self.cell_a + m),
            (self.cell_a - 2 * m, self.cell_a - 2 * m)
        )
        pygame.draw.rect(
            self.screen,
            HIGHLIGHTED_CELL_COLOR if is_highlighted else DEFAULT_CELL_COLOR,
            cell_sqr,
            HIGHLIGHTED_CELL_WIDTH if is_highlighted else DEFAULT_CELL_WIDTH
        )
