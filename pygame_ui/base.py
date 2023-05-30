from pygame_ui.constants import *
import pygame_ui.elements
import pygame.locals as pyglocal
import pygame.mouse as pygmouse
import pygame.scrap as pygscrap
import pygame.key as pygkey
from time import time


class Graphical_UI:
	"""
	The main GUI handler.

	Is automatically called on ``pygame_ui.init()``

	Calling this manually is deprecated.
	"""

	elements = {}
	interactive_elements = []
	text_input_elements = []
	held_buttons = []
	backspace_hold_timer = 0
	old_time = time()
	new_time = time()

	def __init__(self, objects:dict):
		for name, data in objects.items():
			element_type = data.pop('type')
			self.elements[name] = getattr(pygame_ui.elements, element_type)(data, parent=None)

	def get_frame(self, frame_path:str=''):
		"""
		Returns the frame of given path.
		"""
		
		frame = self
		for i in frame_path.split('->'):
			if i in frame.elements.keys():
				frame = frame.elements[i]
			else:
				raise KeyError('No frame with name \''+i+'\' was found. '+MORE_INFO+'frame paths')
		return frame

	def get_element(self, name:str, frame_path:str=''):
		"""
		Returns the element with specified name at given path.
		"""

		frame = self.get_frame(frame_path)
		if name in frame.elements.keys():
			return frame.elements[name]
		else:
			raise KeyError('No element with name \''+name+'\' was found. '+MORE_INFO+'frame paths')

	def add_element(self, name:str, element:pygame_ui.elements.UI_Element, frame_path:str=''):
		"""
		Adds the specified element with it's name to the GUI or given frame.
		"""
		
		frame = self.get_frame(frame_path)
		frame.elements[name] = element

	def remove_element(self, name:str, frame_path:str=''):
		"""
		Removes the element specified by name (and path) from it's parent.
		"""

		frame = self.get_frame(frame_path)
		if name in frame.elements.keys():
			frame.elements.pop(name)
		else:
			raise KeyError('No element with name \''+frame_path+'\' was found. '+MORE_INFO+'frame paths')

	def get_interactive_elements(self):
		interactives = []
		for name, element in self.elements.items():
			if element.is_visible:
				if isinstance(element, pygame_ui.frame):
					interactives.extend(element.get_interactive_elements())
				elif element.is_hoverable or element.is_clickable:
					interactives.append(element)
		self.interactive_elements = interactives

	def event_handler(self, event):
		"""
		This handles all interactive elements.

		Must be called in the following context:
		>>> for event in pygame.event.get():
			Interface.event_handler(event)
		"""

		# Gather held buttons
		if event.type == pyglocal.KEYDOWN:
			self.held_buttons.append(event.key)
		elif event.type == pyglocal.KEYUP:
			self.held_buttons.remove(event.key)

		# Handle mouse button presses
		self.get_interactive_elements()

		element = None
		lmb, rmb, mmb = pygmouse.get_pressed(3)
		mpos = pygmouse.get_pos()
		
		for i in self.interactive_elements:
			mouse_in_boundry = i.rectangle.collidepoint(mpos)

			# Add exception to hoverable elements to fix hover_end
			exception = False
			if i.is_hoverable:
				if i.hover_held:
					exception = True

			if mouse_in_boundry or exception:
				if event.type in [pyglocal.MOUSEBUTTONDOWN, pyglocal.MOUSEBUTTONUP] and i.is_clickable:
					element = i
				elif event.type in [pyglocal.MOUSEMOTION, pyglocal.MOUSEWHEEL] and i.is_hoverable:
					element = i
			elif event.type in [pyglocal.MOUSEBUTTONUP, pyglocal.MOUSEMOTION, pyglocal.MOUSEWHEEL] and i.click_held:
				element = i
			
			if event.type == pyglocal.MOUSEBUTTONUP and lmb == 0:
				i.click_end = True
				i.click_held = False

		if element != None:
			if event.type in [pyglocal.MOUSEMOTION, pyglocal.MOUSEWHEEL]:
				if element.is_hoverable:
					if element.rectangle.collidepoint(mpos) and not element.hover_held:
						element.hover_start = True
						element.hover_held = True
					elif not element.rectangle.collidepoint(mpos) and element.hover_held:
						element.hover_end = True
						element.hover_held = False
					
				if isinstance(element, pygame_ui.slider) and element.click_held:
					element.set_value_from_pos(mpos)

			elif event.type == pyglocal.MOUSEBUTTONDOWN and lmb == 1:
				element.click_start = True
				element.click_held = True
				if isinstance(element, pygame_ui.switch):
					element.state = not element.state
				elif isinstance(element, pygame_ui.text_input):
					if element.typing_start_on_click:
						if element.typing == False:
							element.text = ''
						element.typing = True
						element.caret = True


		# Handle keyboard inputs
		self.text_input_elements = []
		for name, element in self.elements.items():
			if element.is_visible:
				if isinstance(element, pygame_ui.frame):
					self.text_input_elements.extend(element.get_text_input_elements())

		if event.type == pyglocal.KEYDOWN:
			key = pygkey.name(event.key)
			for i in self.text_input_elements:
				if i.typing:
					i.caret = True
					i.caret_timer = 0
					if key in ALPHABET:
						if event.mod & pyglocal.KMOD_CTRL:
							if key == 'x':
								pygscrap.put(pyglocal.SCRAP_TEXT, bytes(i.text, 'utf-8'))
								i.text = ''
							elif key == 'c':
								pygscrap.put(pyglocal.SCRAP_TEXT, bytes(i.text, 'utf-8'))
							elif key == 'v':
								i.text += str(pygscrap.get(pyglocal.SCRAP_TEXT), 'utf-8')
						elif event.mod & pyglocal.KMOD_SHIFT:
							i.text += key.upper()
						else:
							i.text += key
					elif key == 'space':
						i.text += ' '
					elif key == 'backspace':
						i.text = i.text[:-1]
					elif key == 'return' and i.typing_end_on_enter:
						i.caret = False
						i.typing = False
		return 1
	
	def draw(self, pygame_window):
		"""
		Main draw function which will draw all visible things layered like painter-style.
		
		Must be called in the following context:
		>>> Interface.draw(pygame_window)
		>>> pygame.display.flip()
		"""

		# Calculate delta-time
		self.new_time = time()
		dtime = (self.new_time-self.old_time)*1000
		self.old_time = time()

		# Update all timers for the vertical line of text input elements
		for i in self.text_input_elements:
			if i.typing:
				i.caret_timer += dtime
				if i.caret_timer >= 520:
					i.caret = not i.caret
					i.caret_timer = 0

		for i in self.elements.values():
			if i.is_visible:
				if i.background_color != None:
					i.draw_bg(pygame_window)
				i.draw(pygame_window)
		
		# Reset all temporary attribute values
		for i in self.interactive_elements:
			if i.is_clickable:
				i.click_start = False
				i.click_end = False
			if i.is_hoverable:
				i.hover_start = False
				i.hover_end = False
				
		return 1


def init(path_to_json:str='Interface.json'):
	"""
	This loads in the ``Interface.json`` file and created a GUI with it
	"""

	import json
	import os
	
	try:
		file = open(os.path.abspath(path_to_json))
	except FileNotFoundError:
		print(ISSUE_REPORT)
	UI = json.load(file)
	file.close()

	interface = Graphical_UI(UI)

	# clearing up namespace
	del json, os, pygame_ui.elements

	# Initialize the pygame module for access to clipboard
	pygscrap.init()

	return interface