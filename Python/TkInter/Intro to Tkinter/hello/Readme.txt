This is hello Script for using the Python Tkinter Library

In this exercise we are going to make a simple widget window and say "Hello World", and shove the text onto the screen within the widget.

NOTES

from tkinter import * 
This means that you are importing everything from the tkinter library.
There are other ways to do it but in MOST scenarios you are going to use this method.

In Tkinter EVERYTHING you implement is a widget.
And typically you use/make a root widget (a box Window)

What an event Loop is that when you have GUI(Graphical User Interface) it will constantly be looping and when you apply a root like this:
root.mainloop()

It will end that loop sequence.