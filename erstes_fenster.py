from tkinter import *

frame = Tk()
frame.geometry("200x150")
frame.title("Erstes Fenster")

label = Label(frame, text="Hallo")
label.pack()

def change_label():
    label.configure(text="Tschüss")


button_bye = Button(frame, text="ByeBye", fg="red", bg="yellow", command=change_label)
button_bye.pack()

button_quit = Button(frame, text="Close", command=frame.quit)
button_quit.pack(side=RIGHT)

frame.mainloop()
