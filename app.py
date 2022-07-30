from tkinter import *
from tkinter import ttk
from random import choice
root = Tk()
root.title("Random Food Decider")

random_option = []

def get_list():
    random_option = list_box_entry.get().split(",").strip()
    print(random_option)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,S,E,W))

ttk.Label(mainframe, text="Fill in Your Options Here").grid(column=0, row=0, padx=10, pady=5)
ttk.Label(mainframe, text="Your Random Selection is:").grid(column=1, row=0, padx=10, pady=5)

list_box = StringVar()
list_box_entry = ttk.Entry(mainframe, textvariable=list_box)
list_box_entry.grid(column=0, row=1, padx=10, pady=10)

ttk.Button(mainframe, text="Get Random Choice", command=get_list).grid(column=0, row=2)

root.bind("<Return>", get_list)



root = mainloop()