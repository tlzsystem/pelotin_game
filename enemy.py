import pygame
import random

BLANCO    = (255, 255, 255)
NEGRO    = (0, 0, 0)

class Enemy(pygame.sprite.Sprite):

	rect_x = 10
	rect_y = random.randint(50,500) 

	rect_cambio_x = 15
	rect_cambio_y = 15
	enPantalla = False


	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("art/ball.jpg").convert()
		self.image.set_colorkey(BLANCO)
		self.rect = self.image.get_rect()
		self.enPantalla = False
		self.rect.x=1600

	def aparecer(self):
		self.rect.x=self.rect_x
		self.rect.y=self.rect_y
		self.enPantalla = True

	def mover(self):
		if self.enPantalla == True:
			if self.rect.y > 550 or self.rect.y <0:
				self.rect_cambio_y= self.rect_cambio_y * -1
			if self.rect.x > 1150 or self.rect.x <0:
				self.rect_cambio_x = self.rect_cambio_x*-1
			self.rect.x+=self.rect_cambio_x
			self.rect.y+=self.rect_cambio_y

