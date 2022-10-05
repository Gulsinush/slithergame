# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
import threading as tm
import time

basic_coord = ([300,300,320,320],
               [320,300,340,320],
               [340,300,360,320],
               [360,300,380,320]
               )

class Snake:
    
    coord_list = []
    
    def __init__(self):
        self.coord_list=list(basic_coord)
        

    def draw(self):
        color = "red"
        for i in range(len(self.coord_list)):
            if i>0:
                color = "orange"
            canvas.create_rectangle(self.coord_list[i][0], self.coord_list[i][1], 
                                    self.coord_list[i][2], self.coord_list[i][3], 
                                    outline=color, fill="green")
                
    def change_coord(self,step_x,step_y):
        for i in range(len(self.coord_list)-1,0,-1):
            for j in range(4):
                self.coord_list[i][j] = self.coord_list[i-1][j]  
        self.coord_list[0][0] += step_x
        self.coord_list[0][2] += step_x
        self.coord_list[0][1] += step_y
        self.coord_list[0][3] += step_y
            
window = tk.Tk()
window.geometry('600x600')
window.title("Snake")
window.iconbitmap('logo.ico')
size = 600
canvas = tk.Canvas(window, width=size, height=size)
canvas.pack()


snake1 = Snake()
x = -20
y = 0 
x_list = [-20,0,20,0]
y_list = [0,20,0,-20]
count = 0
while True:
    snake1.draw()
    snake1.change_coord(x,y)
    window.update_idletasks()
    window.update()
    time.sleep(0.3)
    count += 1
    y=y_list[count//6]
    x=x_list[count//6]
    if count>22:
        count=0
        
    canvas.delete("all")



  
    



