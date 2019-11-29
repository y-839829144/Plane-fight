import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,rect):
		super().__init__()
		self.image = pygame.image.load('res/images/bullet1.png')
		self.rect = self.image.get_rect()
		self.rect.centerx = rect.centerx
		self.rect.y = rect.y
		self.speed = 5
	def draw(self,surface):
		surface.blit(self.image,self.rect)

	def move(self):
		if self.rect.y < 0-10:
			self.kill()
			del self 
		else:
			self.rect.y -= self.speed

	def update(self,surface):
		self.move()
		self.draw(surface)

