"""
blabla
"""

import PygameUI.elements


class Graphical_UI:
	"""
	blabla
	"""

	Elements = {}

	def __init__(self, objects:dict):
		for item_type, data in objects.items():
			element_id = data.pop('name')
			self.Elements[element_id] = getattr(PygameUI.elements, item_type)(data)

	def add_element(self, name:str, Element:PygameUI.elements.UI_Element):
		self.Elements[name] = Element

	def remove_element(self, name:str):
		try:
			self.Elements.pop(name)
			return
		except KeyError:
			raise KeyError('Tried removing non-existing element.')

	def event_handler(self, event):
		"""
		blabla
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
	del json, os, PygameUI.elements

	return interface