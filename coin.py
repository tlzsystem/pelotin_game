import pygame
import random

BLANCO    = (255, 255, 255)

class Coin(pygame.sprite.Sprite):


	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("art/coin.png").convert()
		self.image.set_colorkey(BLANCO)
		self.rect = self.image.get_rect()
		
	def aparecer(self):
		self.rect.x = random.randint(20,1180) 
		self.rect.y = random.randint(20,580) 
		
		