"""Hello World Application for Tkinter"""

import tkinter as tk

## root window

# create root application #
root = tk.Tk()

# configure root column layout #
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=2)
root.columnconfigure(10, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=2)
# set the title
root.title('Banana interest survey')

# set the root window size #
root.geometry('640x480+300+300')
root.resizable(False, False)

## Widgets ##

# create title label widget #
title = tk.Label(
    root,
    text='Please take the survey',
    font=('Arial 16 bold'),
    bg='green',
    fg='#ff0000'
)

# place title widget #

title.grid(row=0, column=2)


# create eater_inp checkbox widget to indicate banana usage #
eater_var = tk.BooleanVar()
eater_inp = tk.Checkbutton(
    root,
    variable=eater_var,
    text='Check this box if you eat bananas'
)

# place the eater_inp checkbox #
eater_inp.grid(row=1, column=2)


# create text input prompt widget for user's name #
name_var = tk.StringVar(root)
name_label = tk.Label(root, text='What is your name?')
name_inp = tk.Entry(root, textvariable=name_var)

# place name_label and name_inp #
name_label.grid(row=4, column=2)
name_inp.grid(row=5, column=2)
print(name_var.get())


# create a prompt for number of bananas consumed per day as a spinbox widget #
num_var = tk.IntVar(value=3)
num_label = tk.Label(text='How many bananas do you eat per day?')
num_inp = tk.Spinbox(root, textvariable=num_var, from_=0, to=1000, increment=1)

# place the num_label label and num_inp spinner #
num_label.grid(row=6, column=2)
num_inp.grid(row=7, column=2, columnspan=1, sticky='we')


# create listbox color_inp filled with color_choices and a label asking to select a color preference #
color_var = tk.StringVar(value='Any')
color_label = tk.Label(
    root,
    text='What is the best color for a banana?'
)
color_choices = (
    'Any', 'Green', 'Green-Yellow', 'Yellow',
    'Brown Spotted', 'Black'
)
color_inp = tk.OptionMenu(root, color_var, *color_choices)

# place color_label, color_inp, and color_choices #
color_label.grid(row=9, column=2)
color_inp.grid(row=10, column=2)


# create radio buttons for plantain preferences #
plantain_var = tk.BooleanVar()
plantain_label = tk.Label(root, text='Do you eat plantains?')
plantain_frame = tk.Frame(root)
plantain_yes_inp = tk.Radiobutton(plantain_frame, text='Yes', value=True, variable=plantain_var)
plantain_no_inp = tk.Radiobutton(plantain_frame, text='Ewww, no way!', value=False, variable=plantain_var)

# place plantain objects #
plantain_yes_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plantain_no_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plantain_label.grid(row=13, column=2)
plantain_frame.grid(row=14, column=2)


# create a textbox for banana haiku #
banana_haiku_label = tk.Label (
    root,
    text='Write a haiku about bananas'
)
banana_haiku_inp = tk.Text(root, height=3)

banana_haiku_label.grid(row=15, column=2)
banana_haiku_inp.grid(row=16, column=2)


# create a submit button #
submit_btn = tk.Button(root, text='Submit Survey')

# define method for submit button
def on_submit():
    name = name_inp.get()
    number = num_inp.get()
    color = color_var.get()
    banana_eater = eater_var.get()
    plantain_eater = plantain_var.get()
    haiku = banana_haiku_inp.get('1.0', tk.END)
    message = f'Thanks for taking the survey, {name}.\n'
    if not banana_eater:
        message += "Sorry you don't like bananas!\n"
    else:
        message += f'Enjoy your {number} {color} bananas!\n'
    if plantain_eater:
        message += 'Enjoy your plantains!'
    else:
        message += 'May you successfully avoid plantains!'
    if haiku.strip():
        message += f'\n\nYour Haiku:\n{haiku}'

    output_var.set(message)


# place submit_btn #
submit_btn.configure(command=on_submit)
submit_btn.grid(row=99, column=2)

# create a program output line #
output_var = tk.StringVar(value='')
tk.Label(root, textvariable=output_var, anchor='w', justify='center').grid(row=100, column=2, columnspan=2, sticky="NSEW")


# execute main
root.mainloop()

