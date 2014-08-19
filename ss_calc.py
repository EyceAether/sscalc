__author__ = 'davburge'

import ss_gui

import Tkinter

root = Tkinter.Tk()
root.resizable(0,0)

app = ss_gui.Application(root)

app.master.title("Star Sonata Calculator")

app.mainloop()
