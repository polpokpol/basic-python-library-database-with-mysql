from tkinter import *
import Remastered


def get_selected_row(event):
	global selected_tuple
	yeah = list1.curselection()[0]
	selected_tuple = list1.get(yeah)
	e1.delete(0,END)
	e1.insert(END,selected_tuple[1])
	e2.delete(0,END)
	e2.insert(END,selected_tuple[2])
	e3.delete(0,END)
	e3.insert(END,selected_tuple[3])
	e4.delete(0,END)
	e4.insert(END,selected_tuple[4])
	

def view_command():
	list1.delete(0, END)
	for row in Remastered.view():
		list1.insert(END, row)


def search_command():
	list1.delete(0, END)
	for row in Remastered.search(title_text.get(), category_text.get(), isbn_text.get()):
		list1.insert(END, row)

def add_command():
	Remastered.insert(title_text.get(), author_text.get(), category_text.get(), isbn_text.get())
	list1.delete(0, END)
	list1.insert(END, (title_text.get(), author_text.get(), category_text.get(), isbn_text.get()))

def delete_command():
	Remastered.delete(selected_tuple[0])

def update_command():
	Remastered.update(selected_tuple[0], title_text.get(), author_text.get(), category_text.get(), isbn_text.get())

def destroy():
	root.destroy()

root = Tk()

root.title("Library for beginners")
root.config(bg = "lightgray")

l1 = Label(root, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(root, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(root, text = "Category")
l3.grid(row = 1, column = 0)

l4 = Label(root, text = "ISBN")
l4.grid(row = 1, column = 2, rowspan = 2, sticky = 'n')


title_text = StringVar()
e1 = Entry(root, textvariable = title_text)
e1.grid(row = 0, column = 1)
e1.config(bg = "orange")

author_text = StringVar()
e2 = Entry(root, textvariable = author_text)
e2.grid(row = 0, column = 3)
e2.config(bg = "orange")

category_text = StringVar()
e3 = Entry(root, textvariable = category_text)
e3.grid(row = 1, column = 1)
e3.config(bg = "orange")

isbn_text = StringVar()
e4 = Entry(root, textvariable = isbn_text)
e4.grid(row = 1, column = 3)
e4.config(bg = "orange")

list1 = Listbox(root, height = 9, width = 40)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)
list1.config(border = 3, relief = "sunken")


sb1 = Scrollbar(root, orient=VERTICAL)
sb1.grid(row = 2, column = 2, rowspan = 6, sticky = 'nsw')

# list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)
list1['yscrollcommand'] = sb1.set
list1.config(bg = "gray")


list1.bind('<<ListboxSelect>>',get_selected_row)


b1 = Button(root, text = "View all", width = 12, command = view_command)
b1.grid(row = 2, column = 3)
b1.config(bg = "green", fg = "white")

b2 = Button(root, text = "Search Entry", width = 12, command = search_command)
b2.grid(row = 3, column = 3)
b2.config(bg = "green", fg = "white")

b3 = Button(root, text = "Add Entry", width = 12, command = add_command)
b3.grid(row = 4, column = 3)
b3.config(bg = "green", fg = "white")

b4 = Button(root, text = "Update", width = 12, command = update_command)
b4.grid(row = 5, column = 3)
b4.config(bg = "green", fg = "white")

b5 = Button(root, text = "Delete", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)
b5.config(bg = "green", fg = "white")

b6 = Button(root, text = "Close", width = 12, command = destroy)
b6.grid(row = 7, column = 3)
b6.config(bg = "green", fg = "white")

root.mainloop()