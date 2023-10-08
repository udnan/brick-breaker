import pygame
from pygame.locals import (K_LEFT, K_RIGHT)


class Paddle:
    left_stop = 2
    horizontal_velocity = 5.0

    def __init__(self, color, height, width, x_coordinate, y_coordinate, window_width):
        self.color = color
        self.height = height
        self.width = width
        self.window_width = window_width
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x_coordinate, self.y_coordinate, self.width, self.height))

    def get_paddle_x_position(self):
        return self.x_coordinate, self.x_coordinate + self.width

    def get_paddle_y_position(self):
        return self.y_coordinate - (self.height / 2)

    def move(self, direction):
        self.x_coordinate = self.x_coordinate + (direction * self.horizontal_velocity)

    def move_left(self):
        if self.x_coordinate < self.horizontal_velocity:
            self.x_coordinate = self.left_stop
        else:
            self.move(-1)

    def move_right(self):
        if (self.x_coordinate + self.horizontal_velocity) > (self.window_width - self.width):
            self.x_coordinate = self.x_coordinate
        else:
            self.move(1)

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.move_left()
        if pressed_keys[K_RIGHT]:
            self.move_right()

