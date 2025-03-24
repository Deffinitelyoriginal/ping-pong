from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back_color = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
"""window.fill(back_color)"""

game = True 
finish = False
clock = time.Clock()
fps = 60

player_1 = Player('Player.png', 30, 200, 4, 50, 150)
player_2 = Player('Player.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('Player 1 LOSE!', True, (180,0,0))
lose2 = font.render('Player 2 LOSE!', True, (180,0,0))
speed_ball_x = 3
speed_ball_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    background = transform.scale(image.load('background,.png'),(win_width, win_height))
    if finish != True:
        window.blit(background,(0,0))
        player_1.update_l()
        player_2.update_r()
        ball.rect.x += speed_ball_x
        ball.rect.y += speed_ball_y

        if sprite.collide_rect(player_1,ball) or sprite.collide_rect(player_2,ball):
            speed_ball_x *= -1
            speed_ball_y += randint(-1,1)

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_ball_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
            gameover = True 

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))
            gameover = True 

        player_1.reset()
        player_2.reset()
        ball.reset()
    display.update()
    clock.tick(fps)