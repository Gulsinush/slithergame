import tkinter as tk
from tkinter import Tk, Canvas, Frame, BOTH
 
window = tk.Tk()
window.title("Snake")
window.geometry('600x600')
window.iconbitmap('logo.ico')

coord_snake = [[50,50,70,70],
               [70,50,90,70],
               [90,50,110,70],
               [110,50,130,70]
               ]


def draw(coord_snake):
    color='red'
    for i in range(len(coord_snake)):
        if i>0:
            color='orange'
        canvas.create_rectangle(coord_snake[i][0], coord_snake[i][1],
                                coord_snake[i][2], coord_snake[i][3],
                                outline=color, fill='green')
    window.mainloop()
    
    
    
size = 600
canvas = tk.Canvas(window, width=size, height=size)
canvas.pack()

draw(coord_snake)