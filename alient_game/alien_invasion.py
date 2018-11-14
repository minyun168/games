#alien_invasion.py

import sys 
import pygame 

def run_game():
	#init game setting and cread an object
	pygame.init()
	screen = pyame.display.set_mode((1200,800))
	pygame.display.set_caption("Alien Invasion")

	#begin the main loop of the game
	while True:

		#watch the event of mouse and keyboard
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#let the monitor be clear
		pygame.display.flip()

run_game()