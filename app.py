from tkinter import *
from tkinter import ttk
from random import choice

class LunchDecider:
    def __init__(self, root):
        # Initializing main frame
        root.title("Random Food Decider")
        root.resizable(width=False, height=False)
        root.bind("<Return>", self.Random_choice)
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N,S,E,W))

        # Setting variables and placing labels
        self.list_choices = StringVar()
        self.picked_option = StringVar()

        ttk.Label(mainframe, text="Your Options Separated by Commas").grid(column=0, row=0, padx=10, pady=5)
        ttk.Label(mainframe, text="Your Random Selection is:").grid(column=1, row=0, padx=10, pady=5)
        ttk.Label(mainframe, textvariable=self.picked_option).grid(column=1, row=1)

        list_box = StringVar()
        self.list_box_entry = ttk.Entry(mainframe, textvariable=list_box)
        self.list_box_entry.grid(column=0, row=1, padx=10, pady=10)
        self.list_box_entry.focus()

        # Button to call random choice function
        ttk.Button(mainframe, text="Get Random Choice", command=self.Random_choice).grid(column=0, row=2)

    def Random_choice(self, *args):
        # Splits the text entered in the entry box into a list, a random selection gets stored
        self.list_choices = self.list_box_entry.get().replace(" ", "").split(",")
        self.picked_option.set(choice(self.list_choices))


root = Tk()
LunchDecider(root)
root = mainloop()