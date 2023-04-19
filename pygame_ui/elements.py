"""
blabla
"""

from pygame_ui.constants import *
import pygame.font as pygfont
import pygame.rect as pygrect
import pygame.draw as pygdraw

pygfont.init()


class UI_Element:
	position = [0,0]
	size = [0,0]
	background_color = None
	is_visible = False
	is_hoverable = False
	is_clickable = False
	auto_size = False

	def __init__(self, initial_data, kwargs):
		for dictionary in initial_data:
			for key in dictionary:
				setattr(self, key, dictionary[key])
		for key in kwargs:
			setattr(self, key, kwargs[key])
		
		self.rectangle = pygrect.Rect(self.position, self.size)
	
	def change_position(self, new_position):
		self.position = new_position
		self.rectangle = pygrect.Rect(self.position, self.size)

	def change_size(self, new_size):
		self.size = new_size
		self.rectangle = pygrect.Rect(self.position, self.size)
	
	def draw_bg(self, pygame_window):
		if self.auto_size:
			if isinstance(self, label):
				auto_rect = pygrect.Rect(self.position, self.font.size(self.text))
			pygdraw.rect(pygame_window, self.background_color, auto_rect)
		else:
			pygdraw.rect(pygame_window, self.background_color, self.rectangle)


class frame(UI_Element):


	def __init__(self, *initial_data, **kwargs):
		super().__init__(initial_data, kwargs)
	
	def draw(self, pygame_window):
		pass


class label(UI_Element):
	text = "Empty Label"
	text_color = (255,255,255)
	text_aa = True
	font_name = 'Arial'
	font_size = 10
	font_bold = False
	font_italic = False

	def __init__(self, *initial_data, **kwargs):
		super().__init__(initial_data, kwargs)
		self.font = pygfont.SysFont(self.font_name, self.font_size, self.font_bold, self.font_italic)
	
	def change_font(self, **kwargs):
		for key in kwargs:
			if key in FONT_ATTRIBUTES:
				setattr(self, key, kwargs[key])
			else:
				raise KeyError(key+' is not a font attribute. '+MUST_BE+FONT_ATTRIBUTES+'\n'+ISSUE_REPORT)
		self.font = pygfont.SysFont(self.font_name, self.font_size, self.font_bold, self.font_italic)

	def draw(self, pygame_window):
		text_render = self.font.render(self.text, self.text_aa, self.text_color, self.background_color)
		pygame_window.blit(text_render, self.position)


class button(UI_Element):
	is_clickable = True

	def __init__(self, *initial_data, **kwargs):
		super().__init__(initial_data, kwargs)

	def draw(self, pygame_window):
		pass


class switch(UI_Element):
	is_clickable = True

	def __init__(self, *initial_data, **kwargs):
		super().__init__(initial_data, kwargs)

	def draw(self, pygame_window):
		pass


class slider(UI_Element):
	is_clickable = True

	def __init__(self, *initial_data, **kwargs):
		super().__init__(initial_data, kwargs)

	def draw(self, pygame_window):
		pass


class dropdown(UI_Element):
	is_clickable = True

	def __init__(self, *initial_data, **kwargs):
		super().__init__(initial_data, kwargs)

	def draw(self, pygame_window):
		pass