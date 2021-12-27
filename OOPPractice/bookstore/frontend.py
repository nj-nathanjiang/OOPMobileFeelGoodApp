from tkinter import *
from backend import DataBase

database = DataBase("books.db")


class Window:

    def __init__(self):
        self.window = Tk()
        self.window.wm_title("Book Recorder")

        self.l1 = Label(self.window, text="Title")
        self.l1.grid(column=0, row=0)

        self.l2 = Label(self.window, text="Author")
        self.l2.grid(column=2, row=0)

        self.l3 = Label(self.window, text="Year")
        self.l3.grid(column=0, row=1)

        self.l4 = Label(self.window, text="Rating")
        self.l4.grid(column=2, row=1)

        self.title_entry = StringVar()
        self.e1 = Entry(self.window, textvariable=self.title_entry)
        self.e1.grid(column=1, row=0)

        self.author_entry = StringVar()
        self.e2 = Entry(self.window, textvariable=self.author_entry)
        self.e2.grid(column=3, row=0)

        self.year_entry = StringVar()
        self.e3 = Entry(self.window, textvariable=self.year_entry)
        self.e3.grid(column=1, row=1)

        self.rating_entry = StringVar()
        self.e4 = Entry(self.window, textvariable=self.rating_entry)
        self.e4.grid(column=3, row=1)

        self.list1 = Listbox(self.window, height=6, width=60)
        self.list1.grid(column=0, row=2, rowspan=6, columnspan=2)

        self.sb1 = Scrollbar(self.window)
        self.sb1.grid(column=2, row=2, rowspan=6)

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.list1.bind("<<ListboxSelect>>", self.get_selected_row)

        self.b1 = Button(self.window, text="View all", width=12, command=self.view_command)
        self.b1.grid(column=3, row=2)

        self.b2 = Button(self.window, text="Search entry", width=12, command=self.search_command)
        self.b2.grid(column=3, row=3)

        self.b3 = Button(self.window, text="Add entry", width=12, command=self.add_command)
        self.b3.grid(column=3, row=4)

        self.b4 = Button(self.window, text="Update Entry", width=12, command=self.update_command)
        self.b4.grid(column=3, row=5)

        self.b5 = Button(self.window, text="Delete Entry", width=12, command=self.delete_command)
        self.b5.grid(column=3, row=6)

        self.b6 = Button(self.window, text="Close", width=12, command=self.window.destroy)
        self.b6.grid(column=3, row=7)


        self.window.mainloop()

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.list1.curselection()[0]
            selected_tuple = self.list1.get(index)
            selected_tuple = selected_tuple.split("  ")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e1.insert(END, selected_tuple[1].replace("(", "").replace(")", ""))
            self.e2.insert(END, selected_tuple[2].replace("(", "").replace(")", ""))
            self.e3.insert(END, selected_tuple[3].replace("(", "").replace(")", ""))
            self.e4.insert(END, selected_tuple[4].replace("(", "").replace(")", "").replace("Rating: ", ""))
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END,
                              str(row[0]) + "  " + "(" + row[1].replace("{", "").replace("}", "") + ")" + "  (" +
                              row[2] + ")  " + f"({str(row[3])})" + "  " + f"(Rating: {row[4]})", )

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_entry.get(),
                                   self.author_entry.get(),
                                   self.year_entry.get(),
                                   self.rating_entry.get()):
            self.list1.insert(END, row[0:4] + (f"Rating: {row[4]}",))

    def add_command(self):
        self.list1.delete(0, END)
        if self.title_entry.get() != ""\
                and self.author_entry != ""\
                and self.year_entry != ""\
                and self.rating_entry != "":
            database.insert(self.title_entry.get(),
                            self.author_entry.get(),
                            self.year_entry.get(),
                            self.rating_entry.get())
            self.list1.insert(END, "Added Book Successfully")
        else:
            self.list1.insert(END, "An Error Occurred While Adding Book")

    def update_command(self):
        database.update(selected_tuple[0],
                        self.title_entry.get(),
                        self.author_entry.get(),
                        self.year_entry.get(),
                        self.rating_entry.get())

    def delete_command(self):
        database.delete(selected_tuple[0])
        self.list1.delete(0, END)
        self.list1.insert(END, "Deleted Book Successfully")


window = Window()
del database
