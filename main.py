import pygame
import random
from player import *
from coin import *

NEGRO    = (0, 0, 0)
BLANCO    = (255, 255, 255)
VERDE    = (0, 255, 0)

class Juego(object):

	jugador = None
	lista_todos = None

	game_over = False
	pantalla_principal = True
	puntos = 0
	imagen_fondo = None 
	moneda = None



	def __init__(self):
		self.puntos = 0
		self.game_over = False
		self.lista_todos= pygame.sprite.Group()
		self.pantalla_principal = True

		self.jugador = Player()
		self.moneda = Coin()


		self.lista_todos.add(self.jugador)
		self.lista_todos.add(self.moneda)
		self.imagen_fondo = pygame.image.load('art/start_screen.png')

	def event_process(self):
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				return True
			if evento.type == pygame.KEYDOWN:
				
				if evento.key == pygame.K_RETURN:  
					if self.game_over==False:
						print "enter"
						
						self.__init__()
						self.pantalla_principal = False
						self.moneda.aparecer()
		return False


	def game_engine(self):

		if not self.game_over:
			self.lista_todos.update()

	def display_frame(self,pantalla):
		pantalla.fill(BLANCO)

		if self.game_over:
			print "game over"

		if self.pantalla_principal == True:
			pantalla.blit(self.imagen_fondo,(0,0))

		if  self.pantalla_principal == False:
			pantalla.fill(BLANCO)
			self.lista_todos.draw(pantalla)
   

		pygame.display.flip()


def main():
	pygame.init()

	dimensiones = [1200,600]
	pantalla = pygame.display.set_mode(dimensiones)

	pygame.display.set_caption("Pelotin Game")
	pygame.mouse.set_visible(False)

	hecho = False
	reloj = pygame.time.Clock()

	juego = Juego()

	while not hecho:

		hecho = juego.event_process()
		juego.game_engine()
		juego.display_frame(pantalla)

		reloj.tick(60)

	pygame.quit()

if __name__ == "__main__":
	main()

