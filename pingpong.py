from pygame import *
from random import randint
from time import time as timer
font.init()

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
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_higth, speed_y):
        super().__init__(player_image, player_x, player_y, player_speed, player_width, player_higth)
        self.speed_y = speed_y
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed
        if self.rect.y > 980:
            self.speed_y *= -1
        if self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(player1, self) or sprite.collide_rect(player2, self):
            self.speed *= -1
player1 = Player("platforma.png", 100, 200, 6, 50, 420)
player2 = Player("platforma.png", 1620, 200, 6, 50, 420)
ball = Ball("ball.png", 960, 540, 5, 100, 100, 5)
window = display.set_mode((0, 0), FULLSCREEN)
display.set_caption("пинг-понг")
FPS = 60
clock = time.Clock()
background = transform.scale(image.load("ctol-pingpong.png"), (1920, 1080))
run = True
game = False
font1 = font.Font(None, 80)
lose1 = font1.render("PLAYER 1 LOSE!", True, (180, 0, 0))
lose2 = font1.render("PLAYER 2 LOSE!", True, (180, 0, 0))
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if game != True:
        window.blit(background, (0, 0))
        player1.reset()
        player2.reset()
        ball.reset()
        player1.update1()
        player2.update2()
        ball.update()
        if ball.rect.x < 0:
            window.blit(lose1, (820, 520))
            game = True
        if ball.rect.x > 1820:
            window.blit(lose2, (820, 520))
            game = True
    display.update()
    clock.tick(FPS)
