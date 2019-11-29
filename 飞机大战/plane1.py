import pygame
from pygame.sprite import Sprite
from pygame.locals import K_a,K_d,K_w,K_s
from random import randint

# 我方飞机精灵类
class Myplane(Sprite):
    def __init__(self,w,h):
        super().__init__()
        self.images = [pygame.image.load('res/images/me1.png'),\
                       pygame.image.load('res/images/me2.png')]
        self.destroy_images = [
            pygame.image.load('res/images/me_destroy_1.png'),
            pygame.image.load('res/images/me_destroy_2.png'),
            pygame.image.load('res/images/me_destroy_3.png'),
            pygame.image.load('res/images/me_destroy_4.png'),
        ]
        self.rect = self.images[0].get_rect() 
        self.rect.centerx = w/2 
        self.rect.y = h - 150 
        self.active_flag = True
        self.counter = 0
        self.counter_destroy = 0
        self.speed = 10
        self.w = w
        self.h = h
        self.mask = pygame.mask.from_surface(self.images[0])

    def draw(self,surface):
         # 0  1  2  3  4  5  6
         # 0  0  0  1  1  1  2  2  2 
         # 1     2     1     2
        if self.active_flag:
            surface.blit(self.images[self.counter//2%2],self.rect)
            self.counter +=1
        else:
            surface.blit(self.destroy_images[self.counter_destroy//5%4],self.rect)  
            self.counter_destroy += 1
            if self.counter_destroy == 20:
                self.reset()
                self.counter_destroy = 0

    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            if self.rect.x - self.speed > 0 - 10: 
                self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed 
    
    def update(self,surface):
        self.move()
        self.draw(surface)

    def reset(self):
        self.rect.centerx = self.w/2 
        self.rect.y = self.h - 150 
        self.active_flag = True


# 敌方飞机精灵类
class Enemyplane(Sprite):
    def __init__(self,w,h):
        super().__init__()
        self.image = pygame.image.load('res/images/enemy1.png')
        self.destroy_images =[
            pygame.image.load('res/images/enemy1_down1.png'),
            pygame.image.load('res/images/enemy1_down2.png'),
            pygame.image.load('res/images/enemy1_down3.png'),
            pygame.image.load('res/images/enemy1_down4.png')]
        self.rect = self.image.get_rect()
        self.rect.x = randint(0,w)  
        self.rect.y = randint(-h,0)
        self.speed = 5
        self.active_flag = True
        self.h = h
        self.w = w
        self.counter = 0
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self,surface):
        if self.active_flag:
            surface.blit(self.image,self.rect)
        else:
            surface.blit(self.destroy_images[self.counter%4],self.rect)
            self.counter+=1
            # 0 1 2 3     4
            if self.counter == 4:
                self.counter=0
                self.reset() 

    def move(self):
        if self.rect.bottom + self.speed < self.h:
            self.rect.y+=self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.x = randint(0,self.w)
        self.rect.y = randint(-self.h,0)
        self.active_flag = True 

    def update(self,surface):
        self.move()
        self.draw(surface)











