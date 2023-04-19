import pygame
import PygameUI # Addition


pygame.init()

# Creating a window
width, height = 1280, 720
flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED
screen = pygame.display.set_mode((width, height), flags, vsync=1)
pygame.display.set_caption("UI Test")
clock = pygame.time.Clock()

# Initializing interface
Interface = PygameUI.init() # Addition


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		Interface.event_handler(event) # Addition

	screen.fill((0,0,0))

	Interface.draw(screen) # Addition

	pygame.display.flip()
	clock.tick(60)
