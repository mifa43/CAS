"""
Example script for testing the Forest theme

Author: rdbende
License: MIT license
Source: https://github.com/rdbende/ttk-widget-factory
"""

import tkinter as tk
from tkinter import ttk
import sys
import os

# Dodajte putanju do glavnog direktorijuma
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(module_path)

# Sada možete importovati modul
from main import modify_HTML, get_data
# Dobijanje apsolutne putanje do direktorijuma u kojem se nalazi trenutni fajl
current_directory = os.path.dirname(os.path.abspath(__file__))

# Formiranje putanje do datoteke "forest-dark.tcl" u istom direktorijumu
tcl_file_path = os.path.join(current_directory, "forest-dark.tcl")


html_path = '/home/mifa43/Desktop/CAS/htmlStructure/jubilej-14.html'

root = tk.Tk()
root.title("Clean Air Solution")
root.option_add("*tearOff", False) # This is always a good idea

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# Create a style
style = ttk.Style(root)

# Import the tcl file
# Učitavanje datoteke "forest-dark.tcl"
root.tk.call("source", tcl_file_path)
# Set the theme with the theme_use method
style.theme_use("forest-dark")
# Create lists for the Comboboxes
option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
combo_list = [
    "None",
    "ZEMUN",
    "NOVI BEOGRAD",
    "STARI GRAD",
    "ZVEZDARA",
    "VRAČAR",
    "PALILULA",
    "ŽELEZNIK",
    "ŽARKOVO",
    "VIDIKOVAC",
    "RAKOVICA",
    "ČUKARICA",
    "CERAK",
    "BANOVO BRDO",
    "SAVSKI VENAC",
    "BORČA",
    "KALUĐERICA",
    "SREMČICA",
    "UGRINOVCI",
    "VELIKA MOŠTANICA",
    "VOŽDOVAC",
    "VOŽDOVAC-RAKOVICA",
    "VOŽDOVAC-BARAJEVO"
]
readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

# Create control variables
a = tk.BooleanVar()
b = tk.BooleanVar(value=True)
c = tk.BooleanVar()
d = tk.IntVar(value=2)
e = tk.StringVar(value=option_menu_list[1])
f = tk.BooleanVar()
g = tk.DoubleVar(value=75.0)
h = tk.BooleanVar()

# Create a Frame for the Checkbuttons
check_frame = ttk.LabelFrame(root, text="Checkbuttons", padding=(20, 10))
check_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

# Checkbuttons
check_1 = ttk.Checkbutton(check_frame, text="Unchecked", variable=a)
check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
check_2 = ttk.Checkbutton(check_frame, text="Checked", variable=b)
check_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
check_3 = ttk.Checkbutton(check_frame, text="Third state", variable=c)
check_3.state(["alternate"])
check_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
check_4 = ttk.Checkbutton(check_frame, text="Disabled", state="disabled")
check_4.state(["disabled !alternate"])
check_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

# Separator
separator = ttk.Separator(root)
separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

# Create a Frame for the Radiobuttons
radio_frame = ttk.LabelFrame(root, text="Radiobuttons", padding=(20, 10))
radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

# Radiobuttons
radio_1 = ttk.Radiobutton(radio_frame, text="Deselected", variable=d, value=1)
radio_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
radio_2 = ttk.Radiobutton(radio_frame, text="Selected", variable=d, value=2)
radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
radio_3 = ttk.Radiobutton(radio_frame, text="Mixed")
radio_3.state(["alternate"])
radio_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
radio_4 = ttk.Radiobutton(radio_frame, text="Disabled", state="disabled")
radio_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

# Create a Frame for input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)


def retrieve_text():
    user_range = spinbox.get()
    grad_param = entry.get()
    kampanja_param = combobox.get()
    print(user_range, grad_param, kampanja_param)
    if kampanja_param == "None":
        kampanja_param = ""

    modify_HTML(html_path, user_range, grad_param, kampanja_param)


# Entry
entry = ttk.Entry(widgets_frame)
entry.insert(0, "Unesi naziv grada")
entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

# Spinbox
spinbox = ttk.Spinbox(widgets_frame, from_=0, to=100)
spinbox.insert(0, "Unesi broj dokumenta")
spinbox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

# Combobox
combobox = ttk.Combobox(widgets_frame, values=combo_list)
combobox.current(0)
combobox.grid(row=2, column=0, padx=5, pady=10,  sticky="ew")

def clear_text():
    entry.delete(0, tk.END)
    spinbox.delete(0, tk.END)
    combobox.delete(0, tk.END)

# Button
button = ttk.Button(widgets_frame, text="Poništi unose", command=clear_text)
button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

# Accentbutton
accentbutton = ttk.Button(widgets_frame, text="Generiši", style="Accent.TButton", command=retrieve_text)
accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")
def format_data():
    all_rows = []
    rows = get_data()
    counter = 1
    for i in rows:
        # Define treeview data
        treeview_data = [
            ("", "end", counter, f"{i.ime}", (f"{i.prezime}", f"{i.adresa}", f"{i.grad}", f"{i.indentification_code}", f"{i.is_printed}"))
        ]
        all_rows.append(treeview_data)
        counter += 1
    # print(all_rows)
    return all_rows

def set_data():
    treeview_data = format_data()
    treeview.delete(*treeview.get_children())  # Briše postojeće podatke iz stabla
    # Insert treeview data
    for i in range(1, len(treeview_data)):
        for item in treeview_data[i]:
            # print(item)
            treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])
            if item[0] == "" or item[2] in (8, 12):
                treeview.item(item[2], open=True) # Open parents
# Togglebutton
button = ttk.Checkbutton(widgets_frame, text="Prikaži podatke", style="ToggleButton", command=set_data)
button.grid(row=8, column=0, padx=5, pady=10, sticky="nsew")

# Switch
switch = ttk.Checkbutton(widgets_frame, text="Da, ištampan", style="Switch")
switch.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")

# Panedwindow
paned = ttk.PanedWindow(root)
paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

# Pane #1
pane_1 = ttk.Frame(paned)
paned.add(pane_1, weight=1)

# Create a Frame for the Treeview
treeFrame = ttk.Frame(pane_1)
treeFrame.pack(expand=True, fill="both", padx=5, pady=5)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

# Treeview
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2, 3, 4, 5), height=12)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)

# Treeview columns
treeview.column("#0", width=120)
treeview.column(1, anchor="w", width=120)
treeview.column(2, anchor="w", width=120)
treeview.column(3, anchor="w", width=120)  # Add a new column
treeview.column(4, anchor="w", width=120)  # Add a new column
treeview.column(5, anchor="w", width=120)  # Add a new column

# Treeview headings
treeview.heading("#0", text="Ime", anchor="center")
treeview.heading(1, text="Prezime", anchor="center")
treeview.heading(2, text="adresa", anchor="center")
treeview.heading(3, text="Grad", anchor="center")
treeview.heading(4, text="Indentifikacija", anchor="center")
treeview.heading(5, text="Stampan", anchor="center")



# Insert treeview data
# treeview_data = set_data()
# Select and scroll
treeview.selection_set()
# treeview.see(20)

# Pane #2
pane_2 = ttk.Frame(paned)
paned.add(pane_2, weight=3)

# Notebook
notebook = ttk.Notebook(pane_2)

# Tab #1
tab_1 = ttk.Frame(notebook)
tab_1.columnconfigure(index=0, weight=1)
tab_1.columnconfigure(index=1, weight=1)
tab_1.rowconfigure(index=0, weight=1)
tab_1.rowconfigure(index=1, weight=1)
notebook.add(tab_1, text="Tab 1")

# Scale

scale = ttk.Scale(tab_1, from_=100, to=0, variable=g, command=lambda event: g.set(scale.get()))
scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

# Progressbar
progress = ttk.Progressbar(tab_1, value=0, variable=g, mode="determinate")
progress.grid(row=0, column=1, padx=(10, 20), pady=(20, 0), sticky="ew")

# Label
label = ttk.Label(tab_1, text="Broj redova: ", justify="center")
label.grid(row=1, column=0, pady=10, columnspan=2)

# Tab #2
tab_2 = ttk.Frame(notebook)
notebook.add(tab_2, text="Tab 2")

# Tab #3
tab_3 = ttk.Frame(notebook)
notebook.add(tab_3, text="Tab 3")

notebook.pack(expand=True, fill="both", padx=5, pady=5)

# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
root.mainloop()
