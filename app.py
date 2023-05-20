import customtkinter as ctk
from random import choice

class FoodDecider(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color = 'white')
        # Initializing window
        self.title("Random Food Decider")
        self.resizable(width=False, height=False)
        self.geometry('600x400')

        # variables
        self.entry_string = ctk.StringVar()
        self.output_string = ctk.StringVar()

        # widgets
        EntrySide(self, self.entry_string, self.output_string, self.random_choice)
        OutputSide(self, self.output_string)

        # event
        self.bind('<Return>', self.random_choice)

        # run
        self.mainloop()

    def random_choice(self, *args):
        self.list_choices = self.entry_string.get().split(',')
        self.output_string.set(choice(self.list_choices))
        print(self.output_string.get())

class EntrySide(ctk.CTkFrame):
    def __init__(self, parent, entry_string, output_string, save_func):
        super().__init__(parent, fg_color = '#b3f2dd', corner_radius = 0)
        # placing frame
        self.place(relx = 0.25, rely = 0.5, relwidth = 0.5, relheight = 1, anchor = 'center')

        self.entry_string = entry_string
        self.output_string = output_string

        # layout
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure(1, weight = 1, uniform = 'a')
        self.rowconfigure(2, weight = 2, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')

        # label
        label = ctk.CTkLabel(self, text = 'Enter Options Separated by Commas', text_color = 'gray', font = ctk.CTkFont(family = 'Calibri', size = 15, weight = 'bold'))
        label.grid(row = 0, column = 0, sticky = 'nsew')

        # entrybox
        entry_box = ctk.CTkEntry(self, textvariable = entry_string)
        entry_box.grid(row = 1, column = 0, sticky = 'nsew', padx = 10, pady = 10)

        # button
        button = ctk.CTkButton(
            self,
            text = 'get random',
            command = save_func,
            fg_color = '#97f0d2',
            text_color = 'gray',
            font = ctk.CTkFont(family = 'Calibri', size = 20, weight = 'bold'),
            hover_color = '#88dbc0')
        button.grid(row = 2, column = 0, sticky = 'nsew', padx = 15, pady = 40)
    
class OutputSide(ctk.CTkFrame):
    def __init__(self, parent, output_string):
        super().__init__(parent, fg_color = '#b3f2f1', corner_radius = 0)
        # placing frame
        self.place(relx = 0.75, rely = 0.5, relwidth = 0.5, relheight = 1, anchor = 'center')
        self.output_string = output_string

        # layout
        self.rowconfigure((0,1), weight = 1, uniform = 'b')
        self.columnconfigure(0, weight = 1, uniform = 'b')

        # label
        label = ctk.CTkLabel(self, text = 'Random Choice is:', text_color = 'gray', font = ctk.CTkFont(family = 'Calibri', size = 20, weight = 'bold'))
        label.grid(row = 0, column = 0, sticky = 'nsew')

        # output label
        output_label = ctk.CTkLabel(self, textvariable = self.output_string, text_color = 'gray', font = ctk.CTkFont(family = 'Calibri', size = 20, weight = 'bold'))
        output_label.grid(row = 1, column = 0, sticky = 'new')

FoodDecider()