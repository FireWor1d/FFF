from pygame import *

clock = time.Clock()

game = True 

window = display.set_mode((700,500))

display.set_caption('TheAloNEFenIXProduct')
background = transform.scale(image.load('galaxy.jpg'),(700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, img,x, y, w, h, speed):
        super().__init__()
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(img), (self.w,self.h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def render(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def move(self):
        if self.rect.y <= 450:
            self.rect.x += self.speed
            self.rect.y += self.speed
        if self.rect.y >= 50:
            self.rect.x += self.speed
            self.rect.y -= self.speed


ball = Ball('ball.png', 200, 300, 50, 50, 3)


while game:
    keys_pressed = key.get_pressed()

    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.render()
    ball.move()

    clock.tick(75)
    display.update()

