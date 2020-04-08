import pygame
from pygame.locals import *
import time
import random


class Hero:

    def __init__(self, screen):
        self.x = 150
        self.y = 575
        self.screen = screen
        self.image = pygame.image.load("./images/hero.jpg")
        self.bullets = []

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        over_bound_bullet = []
        for bullet in self.bullets:
            if bullet.judge_over_bound():
                over_bound_bullet.append(bullet)
        for bullet in over_bound_bullet:
            self.bullets.remove(bullet)
        print('子弹数量', len(self.bullets))

        for bullet in self.bullets:
            bullet.display()
            bullet.move()

    def fashebullet(self):
        bullet = Bullet(self.x, self.y, self.screen)
        self.bullets.append(bullet)


class Bullet:
    def __init__(self, x, y, screen):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen
        self.image = pygame.image.load("./images/bullet.jpg")

    def move(self):
        self.y -= 3

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge_over_bound(self):
        return self.y < 0


class Enemy:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load("./images/aircraft.jpg")
        self.bullets = []
        self.direction = "right"

    def move(self):
        if self.direction == "right":
            self.x += 3
        elif self.direction == "left":
            self.x -= 3
        if self.x <= 0:
            self.direction = "right"
        elif self.x >= 360:
            self.direction = "left"

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.display()
            bullet.move()

    def fire(self):
        if random.randint(0, 50) == 25:
            bullet = EnemyBullet(self.x, self.y, self.screen)
            self.bullets.append(bullet)


class EnemyBullet:
    def __init__(self, x, y, screen):
        self.x = x + 20
        self.y = y + 10
        self.screen = screen
        self.image = pygame.image.load("./images/bullet.jpg")

    def move(self):
        self.y += 3

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge_over_bound(self):
        return self.y < 0


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 700), 0, 32)
    background = pygame.image.load("./images/background.jpg")
    hero = Hero(screen)
    enemy = Enemy(random.uniform(0, 400), -10, screen)

    while True:
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                print('keydown')
                if event.key == K_a or event.key == K_LEFT:
                    hero.move_left()
                if event.key == K_d or event.key == K_RIGHT:
                    hero.move_right()
                if event.key == K_SPACE:
                    hero.fashebullet()
                    print('fashebullet')
            if event.type == KEYUP:
                print('keyup')


if __name__ == '__main__':
    main()
