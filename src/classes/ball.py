import pygame


class Ball:
    x_velocity = 7.0
    y_velocity = 3.5

    def __init__(self, color, radius, x_coordinate, y_coordinate, window_height, window_width):
        self.color = color
        self.radius = radius
        self.window_height = window_height
        self.window_width = window_width
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def __is_bounce_from_paddle(self, paddle_x_position, paddle_y_position):
        paddle_x_start, paddle_x_end = paddle_x_position

        return (paddle_x_end >= self.x_coordinate >= paddle_x_start) and (self.y_coordinate >= paddle_y_position)

    def reverse_x_velocity(self):
        self.x_velocity = -1 * self.x_velocity

    def reverse_y_velocity(self):
        self.y_velocity = -1 * self.y_velocity

    def bounce_paddle(self, paddle_x_position, paddle_y_position):
        if self.__is_bounce_from_paddle(paddle_x_position, paddle_y_position):
            if self.y_velocity < 0:
                self.reverse_y_velocity()

    def bounce_top(self):
        if self.y_coordinate - self.radius <= 0:
            self.reverse_y_velocity()

    def bounce_x(self):
        if (self.x_coordinate - self.radius <= 0) or (self.x_coordinate + self.radius >= self.window_width):
            self.reverse_x_velocity()

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x_coordinate, self.y_coordinate), self.radius)

    def get_y_position(self):
        return self.y_coordinate + self.radius

    def move(self, paddle_x_position, paddle_y_position):
        self.bounce_x()
        self.bounce_top()
        self.bounce_paddle(paddle_x_position, paddle_y_position)
        self.x_coordinate = self.x_coordinate + self.x_velocity
        self.y_coordinate = self.y_coordinate - self.y_velocity

    def update(self, pressed_keys, paddle_x_position, paddle_y_position):
        self.move(paddle_x_position, paddle_y_position)
