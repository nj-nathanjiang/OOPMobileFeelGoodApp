from tkinter import *
from backend import DataBase

database = DataBase("books.db")


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        selected_tuple = selected_tuple.split("  ")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.insert(END, selected_tuple[1].replace("(", "").replace(")", ""))
        e2.insert(END, selected_tuple[2].replace("(", "").replace(")", ""))
        e3.insert(END, selected_tuple[3].replace("(", "").replace(")", ""))
        e4.insert(END, selected_tuple[4].replace("(", "").replace(")", "").replace("Rating: ", ""))
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, str(row[0]) + "  " + "(" + row[1].replace("{", "").replace("}", "") + ")" + "  (" + row[2] +
                     ")  " + f"({str(row[3])})" + "  " + f"(Rating: {row[4]})",)


def search_command():
    list1.delete(0, END)
    for row in database.search(title_entry.get(), author_entry.get(), year_entry.get(), rating_entry.get()):
        list1.insert(END, row[0:4] + (f"Rating: {row[4]}",))


def add_command():
    list1.delete(0, END)
    if title_entry.get() != "" and author_entry != "" and year_entry != "" and rating_entry != "":
        database.insert(title_entry.get(), author_entry.get(), year_entry.get(), rating_entry.get())
        list1.insert(END, "Added Book Successfully")
    else:
        list1.insert(END, "An Error Occurred While Adding Book")


def update_command():
    database.update(selected_tuple[0], title_entry.get(), author_entry.get(), year_entry.get(), rating_entry.get())


def delete_command():
    database.delete(selected_tuple[0])
    list1.delete(0, END)
    list1.insert(END, "Deleted Book Successfully")


window = Tk()
window.wm_title("Book Recorder")

l1 = Label(window, text="Title")
l1.grid(column=0, row=0)

l2 = Label(window, text="Author")
l2.grid(column=2, row=0)

l3 = Label(window, text="Year")
l3.grid(column=0, row=1)

l4 = Label(window, text="Rating")
l4.grid(column=2, row=1)

title_entry = StringVar()
e1 = Entry(window, textvariable=title_entry)
e1.grid(column=1, row=0)

author_entry = StringVar()
e2 = Entry(window, textvariable=author_entry)
e2.grid(column=3, row=0)

year_entry = StringVar()
e3 = Entry(window, textvariable=year_entry)
e3.grid(column=1, row=1)

rating_entry = StringVar()
e4 = Entry(window, textvariable=rating_entry)
e4.grid(column=3, row=1)

list1 = Listbox(window, height=6, width=60)
list1.grid(column=0, row=2, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(column=2, row=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(column=3, row=2)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(column=3, row=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(column=3, row=4)

b4 = Button(window, text="Update Entry", width=12, command=update_command)
b4.grid(column=3, row=5)

b5 = Button(window, text="Delete Entry", width=12, command=delete_command)
b5.grid(column=3, row=6)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(column=3, row=7)

window.mainloop()
