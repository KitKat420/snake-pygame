import pygame
from constants import WIDTH, HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT


class Snake(pygame.Rect):

    def __init__(self):
        super().__init__(WIDTH / 2 - SNAKE_WIDTH, HEIGHT / 2 -
                         SNAKE_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)

        self.xcor = 5
        self.ycor = 5
        self.direction = ""

    def move(self):
        if self.direction == "up":
            self.y = self.y - self.ycor
        elif self.direction == "left":
            self.x = self.x - self.xcor
        elif self.direction == "down":
            self.y = self.y + self.ycor
        elif self.direction == "right":
            self.x = self.x + self.xcor
        else:
            self.x = self.x + self.xcor

    def up(self):
        self.direction = "up"

    def left(self):
        self.direction = "left"

    def down(self):
        self.direction = "down"

    def right(self):
        self.direction = "right"
