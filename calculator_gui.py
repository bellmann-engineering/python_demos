from tkinter import *

# Init Allgemein
frame = Tk()
frame.geometry("200x150")
frame.title("Taschenrechner")

label_result = Label(frame, text="")
label_result.pack()

# Variablen
result = StringVar()
a = IntVar()
b = IntVar()

# Eingabefelder
entry_field_1 = Entry(frame, textvariable=a)
entry_field_2 = Entry(frame, textvariable=b)
entry_field_1.pack()
entry_field_2.pack()

# Summe Funktion
def add():
    result = a.get() + b.get()
    label_result.configure(text=result)

# Minus Funktion
def sub():
    result = a.get() - b.get()
    label_result.configure(text=result)

# Plus Button
button_plus = Button(frame, text="+", command=add)
button_plus.pack()

# Minus Button
button_minus = Button(frame, text="-", command=sub)
button_minus.pack()

# Allgemein
button_quit = Button(frame, text="Close", command=frame.quit)
button_quit.pack(side=RIGHT)

frame.mainloop()
