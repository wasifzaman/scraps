from tkinter import *
from PIL import Image, ImageTk



class AppFrame(Frame):

	def __init__(self, parent, num_rows=1, num_columns=1, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.grid_max_rows = num_rows
		self.grid_max_columns = num_columns
		self.grid_items = {}
		self.widgets = {}

	def float(self, state=True):
		if state:
			self.grab_set()
			self.focus_set()
			self.state = 'float'
		else:
			self.grab_release()
			self.state = 'normal'

	def addWidget(self, widget, row=False, column=False):
		is_empty = False

		if type(row) != bool and type(column) != bool and (row, column) not in self.grid_items:
			is_empty = (row, column)
		elif type(row) != bool:
			is_empty = self.grid_search(row=row)
		elif type(column) != bool:
			is_empty = self.grid_search(column=column)
		else:
			is_empty = self.grid_search()

		if not is_empty:
			print('grid slot taken')
			return

		if hasattr(widget, 'fill_tag'):
			self.widgets[widget.fill_tag] = widget
			self.grid_items[is_empty] = widget.fill_tag
		else:
			self.grid_items[is_empty] = True

		widget.create_widget(parent_obj=self, grid_column=is_empty[1], grid_row=is_empty[0])

	def grid_search(self, row=False, column=False):
		found = False
		if type(row) != bool:
			for x in range(0, self.grid_max_columns):
				if (row, x) not in self.grid_items:
					found = (row, x)
					break
		elif type(column) != bool:
			for y in range(0, self.grid_max_rows):
				if (y, column) not in self.grid_items:
					found = (y, column)
					break
		else:
			for x in range(0, self.grid_max_rows):
				if found: break
				for y in range(0, self.grid_max_columns):
					if (x, y) not in self.grid_items:
						found = (x, y)

		return found

class AppWindow(Frame):

	def __init__(self, parent, num_rows=1, num_columns=1, *args, **kwargs):		
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.grid_max_rows = num_rows
		self.grid_max_columns = num_columns
		self.grid_items = {}

		self.main_frame = Frame(self)

		self.frames = {}

		self.pack()
		self.main_frame.grid()

	def newFrame(self, frame_name, frame_size=(1, 1), row=False, column=False):
		rows = frame_size[1]
		columns = frame_size[0]

		is_empty = False

		if type(row) != bool and type(column) != bool and (row, column) not in self.grid_items:
			is_empty = (row, column)
		elif type(row) != bool:
			is_empty = self.grid_search(row=row)
		elif type(column) != bool:
			is_empty = self.grid_search(column=column)
		else:
			is_empty = self.grid_search()

		if not is_empty:
			print('grid slot taken')
			return

		self.grid_items[is_empty] = frame_name

		self.frames[frame_name] = AppFrame(self.main_frame, num_rows=rows, num_columns=columns)
		self.frames[frame_name].grid(
			row=is_empty[0], column=is_empty[1], sticky=N)

		return self.frames[frame_name]

	def grid_search(self, row=False, column=False):
		found = False
		if type(row) != bool:
			for x in range(0, self.grid_max_columns):
				if (row, x) not in self.grid_items:
					found = (row, x)
					break
		elif type(column) != bool:
			for y in range(0, self.grid_max_rows):
				if (y, column) not in self.grid_items:
					found = (y, column)
					break
		else:
			for x in range(0, self.grid_max_rows):
				if found: break
				for y in range(0, self.grid_max_columns):
					if (x, y) not in self.grid_items:
						found = (x, y)

		return found

	def collect(self, relevant):
		crossed = {}

		for frame in self.frames.values():
			for widget in frame.widgets.values():
				if widget.fill_tag in relevant:
					crossed[widget.fill_tag] = widget.getData()

		return crossed

	def populate(self, info):
		for frame in self.frames.values():
			for widget in frame.widgets.values():
				if widget.fill_tag in info:
					try:
						widget.setData(info[widget.fill_tag])
					except:
						continue

class Window(Tk):

	def __init__(self, top=False, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)

		self.main_frame = Frame(self)

		self.main_frame.grid()

	def center(self):
		return

		
	

		
		
if __name__ == '__main__':

	w = Window()

	w.mainloop()