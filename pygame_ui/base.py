import pygame_ui.elements


class Graphical_UI:
	"""
	The main GUI handler
	"""

	Elements = {}

	def __init__(self, objects:dict):
		for item_type, data in objects.items():
			element_id = data.pop('name')
			self.Elements[element_id] = getattr(pygame_ui.elements, item_type)(data)

	def add_element(self, name:str, Element:pygame_ui.elements.UI_Element):
		self.Elements[name] = Element

	def remove_element(self, name:str):
		try:
			self.Elements.pop(name)
			return
		except KeyError:
			raise KeyError('Tried removing non-existing element.')

	def event_handler(self, event):
		"""
		This handles all interactive elements.

		Must be called in the following context:
		>>> for event in pygame.event.get():
			Interface.event_handler(event)
		"""

		return 1
	
	def draw(self, pygame_window):
		"""
		blabla
		"""

		for i in self.Elements.values():
			if i.is_visible:
				if i.background_color != None:
					i.draw_bg(pygame_window)
				i.draw(pygame_window)
		
		return 1


def init():
	"""
	blabla
	"""

	import json
	import os
	

	file = open(os.getcwd()+'\\Interface.json')
	UI = json.load(file)
	file.close()

	interface = Graphical_UI(UI)

	# clearing up namespace
	del json, os, pygame_ui.elements

	return interface