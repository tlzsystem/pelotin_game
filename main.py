import pygame
import random
from player import *
from coin import *
from enemy import *

NEGRO    = (0, 0, 0)
BLANCO    = (255, 255, 255)
VERDE    = (0, 255, 0)

class Juego(object):

	jugador = None
	lista_todos = None
	lista_coin = None
	lista_enemigos = None

	game_over = False
	pantalla_principal = True
	puntos = 0
	imagen_fondo = None 
	imagen_gameover = None
	moneda = None
	enemigo = None
	fuente = None



	def __init__(self):
		self.puntos = 0
		self.game_over = False
		self.lista_todos= pygame.sprite.Group()
		self.lista_coin = pygame.sprite.Group()
		self.lista_enemigos = pygame.sprite.Group()
		self.pantalla_principal = True

		self.jugador = Player()
		self.moneda = Coin()
		self.enemigo = Enemy()


		self.lista_todos.add(self.jugador)
		self.lista_todos.add(self.moneda)
		self.lista_todos.add(self.enemigo)
		self.lista_coin.add(self.moneda)
		self.lista_enemigos.add(self.enemigo)

		self.imagen_fondo = pygame.image.load('art/start_screen.png')
		self.imagen_gameover = pygame.image.load('art/game_over.png')
		self.fuente = pygame.font.Font(None,25)

	def event_process(self):
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				return True
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_RETURN:  
					if self.game_over==False:
						self.__init__()
						self.pantalla_principal = False
						self.moneda.aparecer()
						self.enemigo.aparecer()

					if self.game_over ==True:
						self.__init__()
						self.pantalla_principal = False
						self.moneda.aparecer()
						self.enemigo.aparecer()
						self.game_over=False
						    

		return False


	def game_engine(self):

		if not self.game_over:
			self.lista_todos.update()
			self.enemigo.mover()
			impacto = pygame.sprite.spritecollide(self.jugador,self.lista_coin,False)
			for self.moneda in impacto:
				self.puntos = self.puntos +1
				print self.puntos 
				self.moneda.aparecer()
			impacto_enemigo = pygame.sprite.spritecollide(self.jugador, self.lista_enemigos, True)
			for self.enemigo in impacto_enemigo:
				self.game_over = True

			


	def display_frame(self,panta):

		panta.fill(BLANCO)


		
		if self.pantalla_principal == True:
			panta.blit(self.imagen_fondo,(0,0))

		if  self.pantalla_principal == False:
			panta.fill(BLANCO)
			self.lista_todos.draw(panta)
			texto_salida = str(self.puntos)+" Puntos"
			texto = self.fuente.render(texto_salida,True,NEGRO)
			panta.blit(texto,[10,50])


		if self.game_over == True:
			panta.blit(self.imagen_gameover,(0,0))
			texto_salida = "Lo siento, tus puntos fueron: "+str(self.puntos)+" pts"
			texto = self.fuente.render(texto_salida,True,NEGRO)
			panta.blit(texto,[10,50])
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

