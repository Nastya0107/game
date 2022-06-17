import pygame
from random import randint
from pygame.math import Vector2

snd_dir = "media/snd/"
img_dir = "media/img/"
file = "1.png"
width = 1366
height = 768

class Enemy_bottom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + "enemy_bottom/" + file)
        self.rect = self.image.get_rect()
        self.rect.y = height - 170
        self.rect.x = randint(0, width)
        self.speedx = randint(1, 5)
        self.speedy = randint(-5, 5)
        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0
        self.snd_expl = pygame.mixer.Sound(snd_dir + "expl2.mp3")
        self.snd_expl.set_volume(0.3)
        self.hp = 100
    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)
        self.angle += rotate_speed  # Изменяем угол поворота
        self.image = pygame.transform.rotate(self.copy, self.angle)  # Поворот картинки
        self.rect = self.image.get_rect(center=self.rect.center)  # Изменение рамки

    def update(self):
        self.rotate(5)
        self.rect.x += self.speedx
        self.rect.y -= self.speedy
        if self.rect.x > width or self.rect.right < 0 or self.rect.bottom < 0:
            self.rect.y = height
            self.rect.x = randint(0, width)
            self.speedx = randint(1, 10)
            self.speedy = randint(-5, 10)

class Enemy_left(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + "enemy_left/" + file)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = randint(0 , height)
        self.speedx = randint(1, 5)
        self.speedy = randint(-5, 5)
        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0
        self.snd_expl = pygame.mixer.Sound(snd_dir + "expl2.mp3")
        self.snd_expl.set_volume(0.3)
        self.hp = 100
    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)
        self.angle += rotate_speed  # Изменяем угол поворота
        self.image = pygame.transform.rotate(self.copy, self.angle)  # Поворот картинки
        self.rect = self.image.get_rect(center=self.rect.center)  # Изменение рамки

    def update(self):
        self.rotate(5)
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x > width or self.rect.y > height or self.rect.bottom < 0 :
            self.rect.x = 0
            self.rect.y = randint(0, height)
            self.speedx = randint(1, 5)
            self.speedy = randint(-5, 5)

class Enemy_right(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + 'enemy_right/' + file)
        self.rect = self.image.get_rect()
        self.rect.x = width - 175
        self.rect.y = randint(0, height)
        self.speedx = randint(1, 5)
        self.speedy = randint(-5, 5)
        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0
        self.snd_expl = pygame.mixer.Sound(snd_dir + "expl2.mp3")
        self.snd_expl.set_volume(0.3)
        self.hp = 100
    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)
        self.angle += rotate_speed  # Изменяем угол поворота
        self.image = pygame.transform.rotate(self.copy, self.angle)  # Поворот картинки
        self.rect = self.image.get_rect(center=self.rect.center)  # Изменение рамки

    def update(self):
        self.rotate(5)
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.x < 0 or self.rect.y > height or self.rect.bottom < 0:
            self.rect.x = width
            self.rect.y = randint(0, height)
            self.speedx = randint(1, 10)
            self.speedy = randint(-5, 10)

class Enemy_top(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + "enemy_top/" + file)
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = randint(0, width)
        self.speedx = randint(1, 5)
        self.speedy = randint(-5, 5)
        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0
        self.snd_expl = pygame.mixer.Sound(snd_dir + "expl2.mp3")
        self.snd_expl.set_volume(0.3)
        self.hp = 100
    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)
        self.angle += rotate_speed  # Изменяем угол поворота
        self.image = pygame.transform.rotate(self.copy, self.angle)  # Поворот картинки
        self.rect = self.image.get_rect(center=self.rect.center)  # Изменение рамки

    def update(self):
        self.rotate(5)
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.x > width or self.rect.right < 0 or self.rect.top > height:
            self.rect.bottom = 0
            self.rect.x = randint(0, width)
            self.speedx = randint(1, 10)
            self.speedy = randint(-5, 10)

class Player(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + "/player/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = [width/2, height/2 ]

        self.speed = 10
        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0
        self.hp = 100

        self.snd_expl = pygame.mixer.Sound(snd_dir + "expl.mp3")
        self.snd_expl.set_volume(0.3)
        self.snd_shoot = pygame.mixer.Sound(snd_dir + "shoot.mp3")
        self.snd_shoot.set_volume(0.3)
        self.snd_scratch = pygame.mixer.Sound(snd_dir + "scratch.mp3")
        self.snd_scratch.set_volume(0.3)

    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)
        self.angle += rotate_speed  # Изменяем угол поворота
        self.image = pygame.transform.rotate(self.copy, self.angle)  # Поворот картинки
        self.rect = self.image.get_rect(center=self.rect.center)  # Изменение рамки

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rotate(-5)
        if key[pygame.K_LEFT]:
            self.rotate(5)
        if key[pygame.K_UP]:
            self.position += self.speed * self.direction
            self.rect.center = self.position
        if key[pygame.K_DOWN]:
            self.position -= self.speed * self.direction
            self.rect.center = self.position

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + "bullet.png")
        self.image = pygame.transform.rotate(self.image, player.angle)
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(player.rect.center)
        self.speed = 30
        self.move = self.speed * player.direction
    def update(self):
        self.rect.center += self.move
        if self.rect.x > width or self.rect.y > height or self.rect.x < 0 or self.rect.y < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

        self.anim_speed = 2
        self.frame = 0
        self.anim = [pygame.transform.scale(
                pygame.image.load(img_dir + f'./explosion/{i}.png'),
                (150, 150)) for i in range(9)]

        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        self.image = self.anim[self.frame // self.anim_speed]
        self.frame += 1
        if self.frame >= self.anim_speed * len(self.anim):
            self.kill()
class Bagroung(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + "bg.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = [width / 2, height / 2]
        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0

    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)
        self.angle += rotate_speed
        self.image = pygame.transform.rotate(self.copy, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
    def update(self):
        self.rotate(0.07)