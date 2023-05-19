import customtkinter as ctk
from random import choice

class FoodDecider(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color = 'white')
        # Initializing window
        self.title("Random Food Decider")
        self.resizable(width=False, height=False)
        self.geometry('600x400')

        self.bind("<Return>", self.Random_choice)

        # Setting variables and placing labels
        self.list_choices = ctk.StringVar()
        self.picked_option = ctk.StringVar()

        # widgets
        EntrySide(self)

        # ctk.CTkLabel(mainframe, text="Options Separated by Commas").grid(column=0, row=0, padx=10, pady=5)
        # ctk.CTkLabel(mainframe, text="Random Selection is:").grid(column=1, row=0, padx=10, pady=5)
        # ctk.CTkLabel(mainframe, textvariable=self.picked_option).grid(column=1, row=1)

        list_box = ctk.StringVar()
        # self.list_box_entry = ctk.CTkEntry(mainframe, textvariable=list_box)
        # self.list_box_entry.grid(column=0, row=1, padx=10, pady=10)
        # self.list_box_entry.focus()

        # Button to call random choice function
        # ctk.CTkButton(mainframe, text="Get Random Choice", command=self.Random_choice).grid(column=0, row=2)

        # run
        self.mainloop()

    def Random_choice(self, *args):
        # Splits the text entered in the entry box into a list, a random selection gets stored
        self.list_choices = self.list_box_entry.get().split(",")
        self.picked_option.set(choice(self.list_choices))

class EntrySide(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = 'blue')
        self.place(relx = 0.25, rely = 0.5, relwidth = 0.5, relheight = 1, anchor = 'center')

        # layout
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure(1, weight = 1, uniform = 'a')
        self.rowconfigure(2, weight = 2, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')

        # label
        label = ctk.CTkLabel(self, text = 'Options Separated by Commas', text_color = 'white', font = ctk.CTkFont(family = 'Calibri', size = 17, weight = 'bold'))
        label.grid(row = 0, column = 0, sticky = 'nsew')

        # entrybox
        entry_box = ctk.CTkEntry(self)
        entry_box.grid(row = 1, column = 0)

        # button
        button = ctk.CTkButton(self, text = 'get random')
        button.grid(row = 2, column = 0)


FoodDecider()