'''
'''
from widget_ import Widget_
from tkinter import Frame, Label, Entry, StringVar, LEFT

class Textbox(Widget_):

	def __init__(self, parent_frame, x, y):
		Widget_.__init__(self, parent_frame, x, y)
		self.label_width = 20
		self.entry_width = 30
		self.stringvar = StringVar()
		self.label = Label(self.widget_frame, width=self.label_width)
		self.entry = Entry(self.widget_frame, width=self.entry_width, textvariable=self.stringvar)
		self.label.pack(side=LEFT)
		self.entry.pack(side=LEFT)
		self.label_bg, self.label_fg, self.label_hover_bg, self.label_hover_fg = None, None, None, None
		self.entry_bg, self.entry_fg, self.entry_hover_bg, self.entry_hover_fg = None, None, None, None

	def get_info(self):
		return self.label.cget('text'), self.entry.get()

	def set_text_field(self, label=False, entry=False):
		if label:
			self.label.config(text=label)
		if entry:
			self.stringvar.set(entry)

	def set_setting(self):
		return

	def set_input_restriction(self, string):
		def OnValidate(self, d, i, P, s, S, v, V, W, string):
			if d == 0:
				return True
			accepted_inputs = string.split(',')
			if 'int' in accepted_inputs and S.isdigit():
				return True
			if 'lower' in accepted_inputs:
				S = S.lower()
				return True
			if 'upper' in accepted_inputs:
				S = S.upper()
				return True
			return False

		self.vcmd = self.widget_frame.register(OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W', string
		self.entry.config(validate="all", validatecommand=self.vcmd)
		return

	pass



print(int == eval('int'))