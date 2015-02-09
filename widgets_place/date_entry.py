'''
'''
from textbox_widget import Textbox
from datetime import datetime

class Date_entry(Textbox):

	def __init__(self, parent_frame, x, y):
		Textbox.__init__(self, parent_frame, x, y)
		def var_change(*args):
			def OnValidate(d, i, P, s, S, v, V, W):
				if d == 0: return True
				elif len(s) == 10: return False
				elif S == '/': return True
				elif not S.isdigit():
					return False
				return True

			self.entry.config(validate="key", validatecommand=(self.widget_frame.register(OnValidate),
				'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))

			if self.key_press == 'BackSpace' or self.key_press == 'Delete':
				self.key_press = None
				return

			if len(self.stringvar.get()) == 1 and (not self.stringvar.get().isdigit()):
				self.stringvar.set('')
			elif len(self.stringvar.get()) == 2:
				self.entry.insert(2, '/')
			elif len(self.stringvar.get()) == 5:
				self.entry.insert(5, '/')
			return

		def key_pressed(key):
			self.key_press = key

		self.key_press = None
		self.stringvar.trace('w', var_change)
		self.entry.bind('<BackSpace>', lambda event: key_pressed('BackSpace'))
		self.entry.bind('<Delete>', lambda event: key_pressed('Delete'))

	def set_input_restriction(self):
		return

from tkinter import *


t = Tk()
f = Frame(width=500, height=500)
f.pack()

d = Date_entry(f, 0, 0)
d.set_text_field(entry='10/07/1988')

b = Button(f, text='abcd')
b.place(x=50, y=50)
b.config(command=lambda: print(d.get_info()))

t.mainloop()


'''
date_entry example

test_var = StringVar()
test_entry = Entry(content, textvariable=test_var)
test_entry.pack()

def var_change(*args):
	def OnValidate(d, i, P, s, S, v, V, W):
		if len(s) == 10: return False
		if S == '/': return True
		elif not S.isdigit():
			return False
		return True

	test_entry.config(validate="key", validatecommand=(content.register(OnValidate),
		'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))

	if len(test_var.get()) == 1 and (not test_var.get().isdigit()):
		test_var.set('')
	elif len(test_var.get()) == 2:
		test_entry.insert(2, '/')
	elif len(test_var.get()) == 5:
		test_entry.insert(5, '/')
	return

test_var.trace('w', var_change)

'''