import pygame

#Const
screen_size = w,h = (1200,600)
screen = pygame.display.set_mode(screen_size)
BLANCO  = ( 255, 255, 255)



def start_screen(pantalla):
	start = False
	imagen_fondo=pygame.image.load("art\start_screen.png")

	while not start:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				start = True
				pygame.quit()
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_RETURN:
					start = True
					
		pantalla.fill(BLANCO)
		pantalla.blit(imagen_fondo,[0,0])
		pygame.display.flip()

	return 0






def game_init():

	
	
	pygame.display.set_caption("Pelotin Game")
	game_run()


def game_run():

	hecho = False
	start_screen(screen)
	reloj = pygame.time.Clock()



	while not hecho:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				hecho = True








		screen.fill(BLANCO)


		reloj.tick(60)

		pygame.display.flip()


	return 0










