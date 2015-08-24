import pygame
import random

BLANCO    = (255, 255, 255)

class Coin(pygame.sprite.Sprite):

	comido = False

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("art/coin.png").convert()
		self.image.set_colorkey(BLANCO)
		self.rect = self.image.get_rect()

	def mover(self):
		if self.comido ==True:
			self.rect.x = random.randint(1,1180) 
			self.rect.y = random.randint(1,580) 

	def aparecer(self):
		self.rect.x = random.randint(1,1180) 
		self.rect.y = random.randint(1,580) 
		
		