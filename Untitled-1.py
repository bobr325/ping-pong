from pygame import *
from time import time as timer


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, plaeyr_y, size_x, size_y, player_speed, widht, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = plaeyr_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
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

racket1 = Player('e62e01774f06875ed2139bbf5fc0.jfif', 30, 200, 4, 50, 150)
racket2 = Player('e62e01774f06875ed2139bbf5fc0.jfif', 520, 200, 4, 50, 150)
ball = GameSprite('yellow-orange-tennis-table-ping-pong-ball_925376-43194.jpg', 200, 200, 4, 50, 50)

while Game:
    for e in event.get():
        if e.type == QUIT:
            Game = False
        
        if finish != True:
            window.fill(back)
            racket1.update_l()
            racket2.update_r()



display.update()
clock.tick(FPS)