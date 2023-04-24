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

examples_frame = Interface.get_frame('main->examples')
jason = Interface.get_element('jason the switch', 'main')
harry = Interface.get_element('harry the button', 'main->examples')
jonathan = harry.elements['jonathan']
slider = examples_frame.elements['vincent the slider']
slider_label = examples_frame.elements['slider label']

while True:
	for event in pygame.event.get():
		Interface.event_handler(event) # Addition
		if event.type == pygame.QUIT:
			quit()

	screen.fill((0,0,0))

	# Show and hide the frame with buttons
	if examples_frame.is_visible != jason.state:
		examples_frame.is_visible = jason.state

	# Change button color on hold
	if harry.click_held:
		harry.background_color = (20,100,20)
	else:
		harry.background_color = (100,0,0)
	
	# Update value of slider
	slider_label.text = "value = "+str(round(slider.value, 2))

	Interface.draw(screen) # Addition

	pygame.display.flip()
	clock.tick(60)
