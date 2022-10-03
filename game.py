# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk

class Snake:
    
    coord_list = []
    
    def __init__(self, coord_list):
        
        self.coord_list = coord_list
        

    def draw(self):
        color = "red"
        for i in range(len(self.coord_list)):
            if i>0:
                color = "orange"
            canvas.create_rectangle(self.coord_list[i][0], self.coord_list[i][1], 
                                    self.coord_list[i][2], self.coord_list[i][3], 
                                    outline=color, fill="green")
        
          
window = tk.Tk()
window.geometry('600x600')
window.title("Snake")
window.iconbitmap('logo.ico')
size = 600
canvas = tk.Canvas(window, width=size, height=size)
canvas.pack()

list1 = [[50,50,70,70],
               [70,50,90,70],
               [90,50,110,70],
               [110,50,130,70]
               ] 

list2 = [[50,90,70,110],
               [70,90,90,110],
               [90,90,110,110],
               [110,90,130,110]
               ] 

snake1 = Snake(list1)
snake2 = Snake(list2)
snake2.coord_list.append([130,50,150,70])
snake1.draw()
snake2.draw()
window.mainloop()   
    



