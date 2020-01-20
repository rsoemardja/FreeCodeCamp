from tkinter import *
from PILl import ImageTk, Image

root = Tk()
root.Title('Learn To Code at Codemy.com')
root.iconbitmap('c:/gui/codemy.ico')

my_img = ImageTk.PhotoImage(Image.open("images/aspen.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()