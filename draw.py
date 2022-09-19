from struct import pack
from textwrap import fill
import tkinter
from tkinter.messagebox import YES
root=tkinter.Tk()
root.title("Drawing Window")

def draw(event):
    x1,y1=event.x-2 , event.y-2
    x2,y2=event.x+2 , event.y+2
    c.create_oval(x1,y1,x2,y2,fill='blue')
    

c_width , c_height=800,600
root.geometry("800x670")
c=tkinter.Canvas(root,width=c_width,height=c_height,bd=4,bg="white")
c.pack()
c.bind('<B1-Motion>',draw)
def clear():
    c.delete('all')

b=tkinter.Button(root,text="Clear",height="15",bg="red",command=lambda:clear())
b.pack(side=tkinter.BOTTOM,expand=YES,fill=tkinter.BOTH)
root.mainloop()

