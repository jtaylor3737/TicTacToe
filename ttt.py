import pygame
from pygame import KEYDOWN, K_ESCAPE, QUIT, MOUSEBUTTONDOWN, K_n, K_y
from config import fps, screen_width, screen_height

pygame.init()
clock = pygame.time.Clock()

# Creates window at set resolution
screen = pygame.display.set_mode([screen_width, screen_height])

# Window Name
pygame.display.set_caption("Tic-Tac-Toe")

# Sets Font and Font Size
my_font = pygame.font.Font("Assets/CuteFont-Regular.ttf", 40)

# Tic-Tac-Toe board
board = pygame.image.load("Assets/tttboard.jpg")
board = pygame.transform.scale(board, (screen_height, screen_height))
board_rect = board.get_rect(center=(screen_width / 2, screen_height / 2))

# Stores all game pieces
pieces = pygame.sprite.Group()


# Game pieces (X and O)
class BoardPiece(pygame.sprite.Sprite):
    def __init__(self, positionx, positiony):
        super(BoardPiece, self).__init__()
        self.value = 0
        self.surf = pygame.Surface((screen_height / 4, screen_height / 4))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(screen_width / 2, screen_height / 2))
        self.rect.x = self.rect.x + ((screen_height / 3.5) * positionx)
        self.rect.y = self.rect.y + ((screen_height / 3.5) * positiony)
        pieces.add(self)

    def update(self, x):
        match x:
            case 1:
                self.value = 1
                game.turn_player = 2
                game.tie += 1
                self.surf = pygame.image.load("Assets/X.png").convert()
                self.surf = pygame.transform.scale(
                    self.surf, (screen_height / 4, screen_height / 4)
                )
                check_win()
            case 2:
                self.value = -1
                game.turn_player = 1
                game.tie += 1
                self.surf = pygame.image.load("Assets/O.png").convert()
                self.surf = pygame.transform.scale(
                    self.surf, (screen_height / 4, screen_height / 4)
                )
                check_win()


# Stores game information and spawns initial game pieces
class GameState:
    def __init__(self):
        self.running = True
        self.A1 = BoardPiece(-1, -1)
        self.A2 = BoardPiece(0, -1)
        self.A3 = BoardPiece(1, -1)
        self.B1 = BoardPiece(-1, 0)
        self.B2 = BoardPiece(0, 0)
        self.B3 = BoardPiece(1, 0)
        self.C1 = BoardPiece(-1, 1)
        self.C2 = BoardPiece(0, 1)
        self.C3 = BoardPiece(1, 1)
        self.turn_player = 1
        self.tie = 0


game = GameState()


# Checks if either player has 3 in a row.
def check_win():
    combo_list = [
        (game.A1.value + game.A2.value + game.A3.value),
        (game.B1.value + game.B2.value + game.B3.value),
        (game.C1.value + game.C2.value + game.C3.value),
        (game.A1.value + game.B1.value + game.C1.value),
        (game.A2.value + game.B2.value + game.C2.value),
        (game.A3.value + game.B3.value + game.C3.value),
        (game.A1.value + game.B2.value + game.C3.value),
        (game.A3.value + game.B2.value + game.C1.value),
    ]
    for combo in combo_list:
        if combo == 3:
            screen.fill((255, 255, 255))
            winner_text = "Player 1 Wins!!! Play again? (Y/N)"
            winner_text_surface = my_font.render((winner_text), False, (0, 0, 0))
            winner_text_rect = winner_text_surface.get_rect(
                center=(screen_width / 2, screen_height / 2)
            )
            screen.blit(winner_text_surface, winner_text_rect)
            pygame.display.flip()
            awaiting = True
            while awaiting:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_n:
                            game.running = False
                            awaiting = False
                        elif event.key == K_y:
                            game.turn_player = 1
                            game.tie = 0
                            for piece in pieces:
                                piece.value = 0
                                piece.surf.fill((255, 255, 255))
                            awaiting = False

        elif combo == -3:
            screen.fill((255, 255, 255))
            winner_text = "Player 2 Wins!!! Play again? (Y/N)"
            winner_text_surface = my_font.render((winner_text), False, (0, 0, 0))
            winner_text_rect = winner_text_surface.get_rect(
                center=(screen_width / 2, screen_height / 2)
            )
            screen.blit(winner_text_surface, winner_text_rect)
            awaiting = True
            pygame.display.flip()
            while awaiting:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_n:
                            game.running = False
                            awaiting = False
                        elif event.key == K_y:
                            game.turn_player = 1
                            game.tie = 0
                            for piece in pieces:
                                piece.value = 0
                                piece.surf.fill((255, 255, 255))
                            awaiting = False

        elif game.tie == 9 and not (combo == -3 and combo == 3):
            game.tie = 0
            screen.fill((255, 255, 255))
            tie_text = "Tie! Play again? (Y/N)"
            tie_text_surface = my_font.render((tie_text), False, (0, 0, 0))
            tie_text_rect = tie_text_surface.get_rect(
                center=(screen_width / 2, screen_height / 2)
            )
            screen.blit(tie_text_surface, tie_text_rect)
            pygame.display.flip()
            awaiting = True
            while awaiting:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_n:
                            game.running = False
                            awaiting = False
                        elif event.key == K_y:
                            game.turn_player = 1
                            game.tie = 0
                            for piece in pieces:
                                piece.value = 0
                                piece.surf.fill((255, 255, 255))
                            awaiting = False


while game.running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game.running = False

        elif event.type == QUIT:
            game.running = False

        if event.type == MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            for piece in pieces:
                if piece.rect.collidepoint(mouse_position) and piece.value == 0:
                    piece.update(game.turn_player)

    # Resets screen to white to be drawn on top of
    screen.fill((255, 255, 255))

    # Draws the Tic-Tac-Toe board
    screen.blit(board, board_rect)

    # Draws the pieces
    for piece in pieces:
        screen.blit(piece.surf, piece.rect)

    # Displays text of current turn player
    turn_player_text = "Turn: Player " + str(game.turn_player)
    turn_player_surface = my_font.render((turn_player_text), False, (0, 0, 0))
    screen.blit(turn_player_surface, (0, screen_height * 0.05))

    # updates display
    pygame.display.flip()

    # controls framerate
    clock.tick(fps)
