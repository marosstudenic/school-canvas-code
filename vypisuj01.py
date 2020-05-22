import tkinter
import random

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=600, height=231)

def write():
    global x,y, ones, zeros, cont
    number = random.randint(0,1)
    if number ==1:
        ones+=1
        canvas.create_text(x,y,text=number, fill="blue", font = "Helvetica 15")
    else: 
        zeros +=1
        canvas.create_text(x,y,text =number, fill="green", font = "Helvetica 15")

    x+=10

    if y > 215:
        print( "0: {}".format(zeros))
        print("1: {}".format(ones))
        print("end")
        cont = 0
        root.destroy()


    if x > linewidth:
        y+=17
        x = 10
    
    if cont:
        canvas.after(44, write)

def pause(event):
    global cont
    cont = not(cont)
    write()

        


canvas.pack()
ones, zeros = 0, 0
cont = 1
linewidth = 200
x= 10
y = 10
write()

root.bind('p', pause)

root.mainloop()

