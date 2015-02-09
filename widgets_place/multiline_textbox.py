'''
'''
from textbox_widget import Textbox
from tkinter.scrolledtext import ScrolledText
from tkinter import END

class Multiline_textbox(Textbox):

	def __init__(self, parent_frame, x, y):
		Widget_.__init__(self, parent_frame, x, y)
		self.entry.pack_forget()
		self.entry = ScrolledText(self.widget_frame, width=self.entry_width)
		self.entry.pack(side=LEFT)

	def get_info(self):
		return self.label.cget('text'), self.entry.get('1.0', END+'-1c')

	def set_text_field(self, label=False, entry=False):
		if label:
			self.label.config(text=label)
		if entry:
			self.entry.delete('1.0', END)
			self.entry.insert('1.0', entry)