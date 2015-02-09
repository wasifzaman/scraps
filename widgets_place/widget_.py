'''
'''
from tkinter import Frame

class Widget_:

	def __init__(self, parent_frame, x, y, width=50, height=50):
		self.widget_frame = Frame(parent_frame, width=width, height=height)
		self.widget_frame.place(x=x, y=y)
		self.x, self.y, self.width, self.height = x, y, width, height
		self.tags = []
		return

	def add_tag(self, string):
		self.tag.append(string)
		return

	def resize(self, new_width, new_height):
		self.widget_frame.config(width=new_width, height=new_height)
		return

	def delete_widget(self):
		self.widget_frame.destroy()
		return

	def hide_widget(self):
		self.widget_frame.place_forget()
		return

	def show_widget(self, new_x, new_y):
		self.widget_frame.place(x=new_x, y=new_y)
		return

	def get_info(self):
		return

	def set_field(self):
		return

	pass