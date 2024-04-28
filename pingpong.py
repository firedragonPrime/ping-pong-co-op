from pygame import *
from random import randint
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_higth):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_higth))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 655:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 655:
            self.rect.y += self.speed
class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed
player1 = Player("platforma.png", 100, 200, 6, 200, 420)
player2 = Player("platforma.png", 1620, 200, 6, 200, 420)
ball = Ball("ball.png", 960, 540, 5, 100, 100)
window = display.set_mode((1920, 1080))
display.set_caption("пинг-понг")
FPS = 60
clock = time.Clock()
background = transform.scale(image.load("ctol-pingpong.png"), (1920, 1080))
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit(background, (0, 0))
    player1.reset()
    player2.reset()
    ball.reset()
    player1.update1()
    player2.update2()
    ball.update()
    display.update()
    clock.tick(FPS)