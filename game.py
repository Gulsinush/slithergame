# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
import threading as tm
import time

basic_coord = ([50,50,70,70],
               [70,50,90,70],
               [90,50,110,70],
               [110,50,130,70]
               )

class Snake:
    
    coord_list = list(basic_coord)
    
    def __init__(self):
        pass
        

    def draw(self):
        color = "red"
        for i in range(len(self.coord_list)):
            if i>0:
                color = "orange"
            canvas.create_rectangle(self.coord_list[i][0], self.coord_list[i][1], 
                                    self.coord_list[i][2], self.coord_list[i][3], 
                                    outline=color, fill="green")
         
        
    def change_coord(self):
        step=5
        for i in range(len(self.coord_list)):
            self.coord_list[i][0] -= step
            self.coord_list[i][2] -= step 
       
            
window = tk.Tk()
window.geometry('600x600')
window.title("Snake")
window.iconbitmap('logo.ico')
size = 600
canvas = tk.Canvas(window, width=size, height=size)
canvas.pack()


snake1 = Snake()
while True:
    snake1.draw()
    snake1.change_coord()
    window.update_idletasks()
    window.update()
    time.sleep(0.5)
    canvas.delete("all")



  
    



