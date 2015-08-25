import pygame

BLANCO    = (255, 255, 255)
NEGRO    = (0, 0, 0)

class Enemy(pygame.sprite.Sprite):

	rect_x = 50
	rect_y = 50

	rect_cambio_x = 20
	rect_cambio_y = 20


	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("art/ball.png").convert()
		self.image.set_colorkey(BLANCO)
		self.rect = self.image.get_rect()

	def aparecer(self):
		self.rect.x=self.rect_x
		self.rect.y=self.rect_y

	def mover(self):
		if self.rect.y > 550 or self.rect.y <0:
			self.rect_cambio_y= self.rect_cambio_y * -1
		if self.rect.x > 1150 or self.rect.x <0:
			self.rect_cambio_x = self.rect_cambio_x*-1
		self.rect.x+=self.rect_cambio_x
		self.rect.y+=self.rect_cambio_y

