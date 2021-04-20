import pygame
from pygame.locals import *
import time

APPLE_IMAGE_PATH = "resources/apple.jpg"
BLOCK_IMAGE_PATH = "resources/block.jpg"
BLOCK_SIZE = 40
SURFACE_SIZE = (1000, 800)
FILL_COLOR = (110, 110, 5)


class Apple:
    def __init__(self, screen):
        self.image = pygame.image.load(APPLE_IMAGE_PATH).convert()
        self.screen = screen
        self.x = BLOCK_SIZE * 3
        self.y = BLOCK_SIZE * 3

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()


class Snake:
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    def __init__(self, screen, length):
        self.screen = screen
        self.length = length
        self.block = pygame.image.load(BLOCK_IMAGE_PATH).convert()
        self.x = [BLOCK_SIZE] * length
        self.y = [BLOCK_SIZE] * length
        self.direction = self.DOWN

    def draw(self):
        self.screen.fill(FILL_COLOR)
        for i in range(self.length):
            self.screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_up(self):
        self.direction = self.UP

    def move_down(self):
        self.direction = self.DOWN

    def move_left(self):
        self.direction = self.LEFT

    def move_right(self):
        self.direction = self.RIGHT

    def walk(self):

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == self.UP:
            self.y[0] -= BLOCK_SIZE
        if self.direction == self.DOWN:
            self.y[0] += BLOCK_SIZE
        if self.direction == self.LEFT:
            self.x[0] -= BLOCK_SIZE
        if self.direction == self.RIGHT:
            self.x[0] += BLOCK_SIZE

        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(SURFACE_SIZE)
        self.snake = Snake(self.surface, 6)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.play()

            time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()
