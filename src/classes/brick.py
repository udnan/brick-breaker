import pygame


class Brick:

    def __init__(self, color, height, width, x_coordinate, y_coordinate):
        self.color = color
        self.has_collided = False
        self.height = height
        self.width = width
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def did_ball_collide(self, ball):
        if self.has_collided:
            return False

        ball_in_width = (self.x_coordinate + self.width) >= (ball.x_coordinate - ball.radius) >= self.x_coordinate
        ball_in_height = (self.y_coordinate + self.height) >= (ball.y_coordinate - ball.radius) >= self.y_coordinate

        return ball_in_width and ball_in_height

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x_coordinate, self.y_coordinate, self.width, self.height))

    def set_collided(self):
        self.has_collided = True
