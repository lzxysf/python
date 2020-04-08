import pygame
from pygame.locals import *
import time


def main():
    pressed = False
    key = -1
    pygame.init()
    screen = pygame.display.set_mode((400, 700), 0, 32)
    background = pygame.image.load("./images/background.jpg")
    hero = pygame.image.load('./images/hero.jpg')

    x = 150
    y = 575

    while True:
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))
        pygame.display.update()
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                print('keydown')
                if event.key == K_a or event.key == K_LEFT:
                    x -= 5
                    pressed = True
                    key = K_a
                if event.key == K_d or event.key == K_RIGHT:
                    x += 5
                    pressed = True
                    key = K_d
            if event.type == KEYUP:
                print('keyup')
                pressed = False
        if pressed:
            if key == K_a:
                 x -= 5
            if key == K_d:
                 x += 5


if __name__ == '__main__':
    main()
