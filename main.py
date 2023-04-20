import pygame
import pygame_ui # Addition

pygame.init()

# Creating a window
width, height = 1280, 720
flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED
screen = pygame.display.set_mode((width, height), flags, vsync=1)
pygame.display.set_caption("UI Test")
clock = pygame.time.Clock()


# Initializing interface
Interface = pygame_ui.init() # Addition

harry = Interface.get_element('harry the button', 'frame1->frame2')

jonathan = Interface.get_element('richard', 'frame1->frame2->harry the button')


while True:
	for event in pygame.event.get():
		Interface.event_handler(event) # Addition
		if event.type == pygame.QUIT:
			quit()

	screen.fill((0,0,0))

	jonathan.text = "start: "+str(harry.click_start)+", end: "+str(harry.click_end)+", held: "+str(harry.held)

	Interface.draw(screen) # Addition

	pygame.display.flip()
	clock.tick(60)
