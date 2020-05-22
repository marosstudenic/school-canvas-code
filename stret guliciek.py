import tkinter
import random

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=600, height = 200)


def lopticky():
    global x1, x2
    canvas.delete("all")
    canvas.create_oval(x1, y, x1+15, y+15, fill="blue")
    canvas.create_oval(x2,y, x2-15,y+15, fill="red" )
    x1+=random.randint(5,10)
    x2-=random.randint(5,10)
    if x1 < x2:
        canvas.after(44, lopticky)
    else:
        canvas.delete("all")
        canvas.create_text(x1, y, text="Velke Bum", font="Helvetica 55")

canvas.pack()

x1=0
x2=600
y=100

lopticky()


root.mainloop()



