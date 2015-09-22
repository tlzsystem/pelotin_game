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

	states=["welcome","game","gameover"]
	current_state = states[0]
	game_over = False
	pantalla_principal = True
	puntos = 0
	imagen_fondo = None 
	imagen_gameover = None
	moneda = None

	fuente = None
	sonido_comer = None
	sonido_morir = None
	nivel = 0




	def __init__(self):
		self.puntos = 0
		self.nivel = 0
		self.game_over = False
		self.lista_todos= pygame.sprite.Group()
		self.lista_coin = pygame.sprite.Group()
		self.lista_enemigos = pygame.sprite.Group()
		self.pantalla_principal = True

		self.jugador = Player()
		self.moneda = Coin()


# Carga de enemigos. 3 maximos.
		for i in range(3):
			self.enemigo = Enemy()
			self.lista_enemigos.add(self.enemigo)
			


		self.lista_todos.add(self.jugador)
		self.lista_todos.add(self.moneda)
		
		self.lista_coin.add(self.moneda)
		

		self.imagen_fondo = pygame.image.load('art/start_screen.jpg')
		self.imagen_gameover = pygame.image.load('art/game_over.jpg')
		self.fuente = pygame.font.SysFont("comicsansms",25)
		self.sonido_comer = pygame.mixer.Sound("art/comer.wav")
		self.sonido_morir = pygame.mixer.Sound("art/morir.wav")



	def event_process(self):
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				return True
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_RETURN:  
					if self.current_state==self.states[0]:
						self.__init__()
						self.moneda.aparecer()
						self.lista_enemigos.sprites()[self.nivel].aparecer()
						self.lista_todos.add(self.lista_enemigos.sprites()[self.nivel])
						self.current_state = self.states[1]

					if self.current_state==self.states[2]:
						self.__init__()
						self.moneda.aparecer()						
						self.lista_enemigos.sprites()[self.nivel].aparecer()
						self.lista_todos.add(self.lista_enemigos.sprites()[self.nivel])
						self.current_state=self.states[1]
						    

		return False


	def game_engine(self):

		if self.current_state==self.states[1]:
			self.lista_todos.update()
			for i in range(self.nivel + 1):
				self.lista_enemigos.sprites()[i].mover()
			impacto = pygame.sprite.spritecollide(self.jugador,self.lista_coin,False)
			for self.moneda in impacto:
				self.puntos = self.puntos +1
				self.sonido_comer.play()
				self.moneda.aparecer()
			if self.puntos ==20 and self.nivel == 0:
				self.nivel = self.nivel + 1
				self.lista_enemigos.sprites()[self.nivel].aparecer()
				self.lista_todos.add(self.lista_enemigos.sprites()[self.nivel])
			if self.puntos ==30 and self.nivel == 1:
				self.nivel = self.nivel + 1
				self.lista_enemigos.sprites()[self.nivel].aparecer()
				self.lista_todos.add(self.lista_enemigos.sprites()[self.nivel])

			impacto_enemigo = pygame.sprite.spritecollide(self.jugador, self.lista_enemigos, True)
			for self.enemigo in impacto_enemigo:
				self.sonido_morir.play()
				self.current_state=self.states[2]


			


	def display_frame(self,panta):

		panta.fill(BLANCO)
		
		if self.current_state == self.states[0]:
			panta.blit(self.imagen_fondo,(0,0))

		if  self.current_state == self.states[1]:
			panta.fill(BLANCO)
			self.lista_todos.draw(panta)
			texto_salida = str(self.puntos)+" Points"
			texto = self.fuente.render(texto_salida,True,NEGRO)
			panta.blit(texto,[10,500])
			texto_nivel = "Level "+str(self.nivel +1)
			textop = self.fuente.render(texto_nivel,True,NEGRO)
			panta.blit(textop,[590,20])


		if self.current_state == self.states[2]:
			panta.blit(self.imagen_gameover,(0,0))
			texto_salida = "You lose :( .  You score "+str(self.puntos)+" points"
			texto = self.fuente.render(texto_salida,True,NEGRO)
			panta.blit(texto,[10,500])
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

