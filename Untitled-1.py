from pygame import *
from time import time as timer


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, plaeyr_y, size_x, size_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = plaeyr_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

Game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('e62e01774f06875ed2139bbf5fc0.png', 30, 200, 50, 50, 50, 5, 5)
racket2 = Player('e62e01774f06875ed2139bbf5fc0.png', 520, 200, 50, 50, 50, 5, 5)
ball = GameSprite('yellow-orange-tennis-table-ping-pong-ball_925376-43194 (1).png', 200, 200, 50, 50, 50, 5, 5)
speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))

while Game:
    for e in event.get():
        if e.type == QUIT:
            Game = False
        
        if finish != True:
            ball.rect.x += speed_x
            ball.rect.y += speed_y
            window.fill(back)
            racket1.update_l()
            racket2.update_r()
            racket1.reset()
            racket2.reset()
            ball.reset()
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > 600:
            finish = True
            window.blit(lose2, (200, 200))

            
   



    display.update()
    clock.tick(FPS)