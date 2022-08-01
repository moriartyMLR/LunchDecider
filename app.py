from tkinter import *
from tkinter import ttk
from random import choice

class LunchDecider:
    def __init__(self, root):
        root.title("Random Food Decider")
        root.resizable(width=False, height=False)
        root.bind("<Return>", self.get_list)

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N,S,E,W))

        self.list_choices = StringVar()
        self.picked_option = StringVar()

        ttk.Label(mainframe, text="Your Options Separated by Commas").grid(column=0, row=0, padx=10, pady=5)
        ttk.Label(mainframe, text="Your Random Selection is:").grid(column=1, row=0, padx=10, pady=5)
        ttk.Label(mainframe, textvariable=self.picked_option).grid(column=1, row=1)

        list_box = StringVar()
        self.list_box_entry = ttk.Entry(mainframe, textvariable=list_box)
        self.list_box_entry.grid(column=0, row=1, padx=10, pady=10)

        ttk.Button(mainframe, text="Get Random Choice", command=self.get_list).grid(column=0, row=2)

    def get_list(self, *args):
        self.list_choices = self.list_box_entry.get().replace(" ", "").split(",")
        self.picked_option.set(choice(self.list_choices))


root = Tk()
LunchDecider(root)
root = mainloop()