import pygame
import sys
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)
from src.classes.ball import Ball
from src.classes.brick import Brick
from src.classes.paddle import Paddle

BACKGROUND_FILL = (204, 204, 255)
BOTTOM_OFFSET = 5
FRAMES_PER_SECOND = 60
WIDTH, HEIGHT = 1024, 768

PADDLE_COLOR = (51, 51, 51)
PADDLE_WIDTH, PADDLE_HEIGHT = 150, 20
PADDLE_START_X, PADDLE_START_Y = (WIDTH / 2) - (PADDLE_WIDTH / 2), (HEIGHT - PADDLE_HEIGHT - BOTTOM_OFFSET)

BALL_COLOR = (102, 51, 153)
BALL_RADIUS = 10.0
BALL_START_X = WIDTH / 2
BALL_START_Y = HEIGHT - BALL_RADIUS - PADDLE_HEIGHT - BOTTOM_OFFSET

BRICK_COLOR = (199, 0, 57)
BRICK_WIDTH, BRICK_HEIGHT = 103, 40
BRICK_GAP = 10


def check_brick_collision(bricks, ball):
    for brick in bricks:
        if brick.did_ball_collide(ball):
            brick.set_collided()
            ball.reverse_x_velocity()
            ball.reverse_y_velocity()


def draw_bricks(bricks, window):
    for brick in bricks:
        if not brick.has_collided:
            brick.draw(window)


def draw_frame(ball, bricks, paddle, window):
    window.fill(BACKGROUND_FILL)
    paddle.draw(window)
    ball.draw(window)
    check_brick_collision(bricks, ball)
    draw_bricks(bricks, window)
    pygame.display.update()


def draw_game_complete_frame(window):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Good job Shehroze!', True, PADDLE_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH / 2, HEIGHT / 2)
    window.fill(BACKGROUND_FILL)
    window.blit(text, text_rect)
    pygame.display.update()


def draw_game_over_frame(window):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('It\'s okay Shehroze. Papa and mama love you!', True, PADDLE_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH / 2, HEIGHT / 2)
    window.fill(BACKGROUND_FILL)
    window.blit(text, text_rect)
    pygame.display.update()


def draw_window():
    pygame.display.set_caption("Shehroze's Brick Breaker")
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    return window


def game_loop(clock, ball, bricks, paddle, window):
    clock.tick(FRAMES_PER_SECOND)

    for event in pygame.event.get():
        if event.type == QUIT:
            raise Exception("User wants to QUIT")
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                raise Exception("User wants to ESCAPE")

    if ball.get_y_position() >= HEIGHT:
        draw_game_over_frame(window)
    elif have_all_bricks_collided(bricks):
        draw_game_complete_frame(window)
    else:
        pressed_keys = pygame.key.get_pressed()
        paddle.update(pressed_keys)
        ball.update(pressed_keys, paddle.get_paddle_x_position(), paddle.get_paddle_y_position())
        draw_frame(ball, bricks, paddle, window)


def get_initial_bricks():
    bricks = []
    for row in range(1, 3):
        for column in range(1, 8):
            bricks.append(Brick(BRICK_COLOR, BRICK_HEIGHT,  BRICK_WIDTH, ((column * BRICK_WIDTH) + (column * BRICK_GAP)), ((row * BRICK_HEIGHT) + (row * BRICK_GAP))))

    return bricks


def have_all_bricks_collided(bricks):
    for brick in bricks:
        if not brick.has_collided:
            return False

    return True


def initialize_pygame():
    pygame.init()


def quit_pygame():
    pygame.quit()


def main(argv):
    initialize_pygame()
    clock = pygame.time.Clock()
    ball = Ball(BALL_COLOR, BALL_RADIUS, BALL_START_X, BALL_START_Y, HEIGHT, WIDTH)
    paddle = Paddle(PADDLE_COLOR, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_START_X, PADDLE_START_Y, WIDTH)
    window = draw_window()
    bricks = get_initial_bricks()

    while True:
        try:
            game_loop(clock, ball, bricks, paddle, window)
        except Exception as exc:
            print(f"Exception: {exc}")
            break

    quit_pygame()
    quit()


if __name__ == "__main__":
    main(sys.argv)
