import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\widgets')
sys.path.append(os.path.abspath(os.pardir) + '\database')
sys.path.append(os.path.abspath(os.pardir) + '\miscellaneous')
sys.path.append(os.path.abspath(os.pardir) + '\messages windows')

from tkinter import Frame

from uiHandler22 import AppWindow
from dataHandler import *
from textbox import Textbox
from button import Buttonbox
from toggle_option import Toggle_option
from tableWidget2 import Table
import editS2


def main(t, lang, d):
	d.loadData()

	window_ = AppWindow(t)

	window_.lang = None

	teacher_table = Table(repr='teachertable')
	teacher_table_headers = ['Date', 'Check-In Time', 'Start Time', 'Check-Out Time', 'Confirm Time']

	window_.newFrame("First Frame", (1, 0))
	window_.newFrame("Second Frame", (2, 0))
	window_.newFrame("Third Frame", (2, 1))
	window_.newFrame("Fourth Frame", (4, 1))
	window_.newFrame("Fifth Frame", (3, 0))

	window_.frames["Second Frame"].rowconfigure(0, weight=5, minsize=350)
	window_.frames["Second Frame"].columnconfigure(0, weight=5, minsize=630)

	window_.frames["Fifth Frame"].grid(columnspan=3)

	search_value = Textbox(text="Search", repr=None)
	search_options = Toggle_option(
		options=(('Barcode', 'bCode'),('First Name', 'firstName'), \
		('Last Name', 'lastName'), ('Chinese Name', 'chineseName'), \
		('Phone Number', 'phoneNumber')), repr=None)
	search_button = Buttonbox(text='Search', lang=window_.lang, repr='searchbutton')

	window_.frames["First Frame"].addWidget(search_value, (0, 0))
	window_.frames["First Frame"].addWidget(search_options, (1, 0))
	window_.frames["First Frame"].addWidget(search_button, (0, 1))
	
	fward = Buttonbox(text='>> Next 30 >>', lang=window_.lang, repr='>>')
	bward = Buttonbox(text='<< Previous 30 <<', lang=window_.lang, repr='<<')
	blast = Buttonbox(text='>>> Last Page >>>', lang=window_.lang, repr='>>>')
	window_.frames["Fifth Frame"].addWidget(fward, (1, 1))
	window_.frames["Fifth Frame"].addWidget(bward, (1, 0))
	window_.frames["Fifth Frame"].addWidget(blast, (1, 2))

	fward.config(width=17)
	bward.config(width=17)
	blast.config(width=17)

	fward.selfframe.grid(padx=2)
	bward.selfframe.grid(padx=2)
	blast.selfframe.grid(padx=2)

	#window_.frames["Second Frame"].addWidget(teacher_table, (2, 0))

	sL, page_list = [], []
	for s in d.studentList.values():
		dp = s.datapoints
		sL.append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName'], dp['dob']])

	sL.sort()

	students_on_page = []
	new_frame = Frame(window_.frames["Second Frame"])
	for s in sL:
		students_on_page.append(s)
		if len(students_on_page) >= 15:
			teacher_table_on_page = Table(repr='teachertable')
			teacher_table_on_page.place(parent=new_frame, row=0, column=0)
			teacher_table_on_page.setData(
				headers=teacher_table_headers,
				data=students_on_page
			)
			page_list.append(new_frame)
			new_frame = Frame(window_.frames["Second Frame"])
			students_on_page = []
		elif s == sL[-1]:
			teacher_table_on_page = Table(repr='teachertable')
			teacher_table_on_page.place(parent=new_frame, row=0, column=0)
			teacher_table_on_page.setData(
				headers=teacher_table_headers,
				data=students_on_page
			)
			page_list.append(new_frame)

	page_list[0].grid()

	#sL.append(l)

	#if len(sL[-1]) == 0 and len(sL) != 1: sL.pop()

	window_.pNum = 1

		
	def toPage(p):
		teacher_table.setData(headers=teacher_table_headers, data=sL[p])
		teacher_table.canvas.config(width=700, height=350)
		teacher_table.set_width(1, 5, 14)
		def open_edit_window(pos):
			student_id = teacher_table.data[pos[0]-1][0]
			editS2.main(window_.lang, d, i=student_id)
		for pos, cell in teacher_table.cells.items():
			if pos[0] == 0: continue
			cell.config(bind=('<Double-Button-1>', lambda event, pos=pos: open_edit_window(pos)))

	def next():
		if window_.pNum == len(sL) - 1: return
		toPage(window_.pNum + 1)
		window_.pNum = window_.pNum + 1
		
	def previous():
		if window_.pNum == 1: return
		toPage(window_.pNum - 1)
		window_.pNum = window_.pNum - 1

	def last():
		window_.pNum = len(sL) - 1
		toPage(window_.pNum)	

	'''
	if len(sL[0]) > 15:
		toPage(1)
		fward.config(cmd=next)
		bward.config(cmd=previous)
		blast.config(cmd=lambda: toPage(len(sL) - 1))
		first_page.config(cmd=lambda: toPage(0))
	else:
		toPage(0)
	'''

	def s():
		window_.s = window_.search_value.getData()


		if search_options.stringvar.get() != 'bCode':
			sty = search_options.stringvar.get()
			sdp = window_.search_value.getData()

			sl = []

			for s in d.studentList:
				dp = False
				if sty == 'phoneNumber':
					if d.studentList[s].datapoints['hPhone'] == sdp or \
						d.studentList[s].datapoints['cPhone'] == sdp or \
						d.studentList[s].datapoints['cPhone2'] == sdp:
						dp = d.studentList[s].datapoints

				elif d.studentList[s].datapoints[sty] == sdp:
					dp = d.studentList[s].datapoints
				
				if dp:
					sl.append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName']])


			if len(sl) == 0:
				student_does_not_exist(window_.lang)
				return

			window_.s = sl[0][0]
			if len(sl) > 1:
				sl.sort()
				window_.s = spicker(sl)
				if not window_.s: return

		editS2.main(window_.lang, d=d, top=True, i=window_.s)

	search_value.entry.bind("<Return>", lambda x: s())
	search_button.config(cmd=s)