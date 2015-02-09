'''
'''
from widget_ import Widget_
from tkinter import Label

class Button_(Widget_):

	def __init__(self, parent_frame, x, y):
		Widget_.__init__(self, parent_frame, x, y)
		self.label = Label(self.widget_frame)
		self.label.pack()
		self.label_bg, self.label_fg = None, None

	def get_info(self):
		return self.label.cget('text')

	def set_text_field(self, label):
		self.label.config(text=label)

	def set_settings(self):
		return