import pygame

ROJO   = (255,   0,   0)

class Player(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([20,20])
		self.image.fill(ROJO)
		self.rect = self.image.get_rect()

	def update(self):
		pos = pygame.mouse.get_pos()
		self.rect.x = pos[0]
		self.rect.y = pos[1]

