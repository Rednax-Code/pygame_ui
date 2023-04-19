from pygame_ui.constants import *
import pygame_ui.elements


class Graphical_UI:
	"""
	The main GUI handler

	Is automatically called on ``pygame_ui.init()``

	Calling this manually is deprecated.
	"""

	elements = {}

	def __init__(self, objects:dict):
		for item_type, data in objects.items():
			element_id = data.pop('name')
			self.elements[element_id] = getattr(pygame_ui.elements, item_type)(data)

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
		Main draw function which will draw all visible things layered like painter-style.
		
		Must be called in the following context:
		>>> Interface.draw(pygame_window)
		>>> pygame.display.flip()
		"""

		for i in self.elements.values():
			if i.is_visible:
				if i.background_color != None:
					i.draw_bg(pygame_window)
				i.draw(pygame_window)
		
		return 1


def init():
	"""
	This loads in the ``Interface.json`` file and created a GUI with it
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