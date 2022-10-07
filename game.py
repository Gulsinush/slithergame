# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
import threading as tm
import time
import tkinter.messagebox as mb
import random as rd


basic_coord = ([300,300,320,320],
               [320,300,340,320],
               [340,300,360,320],
               [360,300,380,320]
               )

class Snake:
    
    coord_list = []
    
    step_x =0
    step_y =0
    
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
                
    def change_coord(self, food):
        
        if self.step_x+self.step_y != 0:
            for i in range(len(self.coord_list)-1,0,-1):
                for j in range(4):
                    self.coord_list[i][j] = self.coord_list[i-1][j]  
            self.coord_list[0][0] += self.step_x
            self.coord_list[0][2] += self.step_x
            self.coord_list[0][1] += self.step_y
            self.coord_list[0][3] += self.step_y
            self.eating(food)
            self.game_over()
        
    def change_step(self, event, step_x, step_y):
        if abs(step_x-self.step_x)!=40 and abs(step_y-self.step_y)!=40:
            self.step_x = step_x
            self.step_y = step_y
            
    def eating(self, food):
        if self.coord_list[0]==food.food_coord:
            mb.showwarning("Attention","Вкусно")
            window.destroy()
            
    def game_over(self):
        for i in self.coord_list[0]:
            if i<0 or i>size:
                mb.showwarning("Attention","Game over")
                window.destroy()
                
class Food:
    
    food_coord=[200, 300, 220, 320]
    
    def __init__(self):
        pass
    
    def draw(self):
        canvas.create_rectangle(self.food_coord[0], self.food_coord[1], 
                                    self.food_coord[2], self.food_coord[3], 
                                    outline="black", fill="red")
    
    def change_food(self):
        food_x = rd.randint(0, 580)
        food_y = rd.randint(0, 580)
        self.food_coord = [food_x, food_y, food_x+20, food_y+20]
        

            
window = tk.Tk()
window.geometry('600x600')
window.title("Snake")
window.iconbitmap('logo.ico')
size = 600
canvas = tk.Canvas(window, width=size, height=size)
canvas.pack()


snake1 = Snake()
food = Food()

while True:
    snake1.draw()
    food.draw()
    window.bind('<KeyRelease-Left>',lambda e, step_x=-20, step_y=0: 
            snake1.change_step(e,step_x, step_y))
    window.bind('<KeyRelease-Right>',lambda e, step_x=20, step_y=0: 
            snake1.change_step(e,step_x, step_y))
    window.bind('<KeyRelease-Up>',lambda e, step_x=0, step_y=-20: 
            snake1.change_step(e,step_x, step_y))
    window.bind('<KeyRelease-Down>',lambda e, step_x=0, step_y=20: 
            snake1.change_step(e,step_x, step_y))
    snake1.change_coord(food)
    window.update_idletasks()
    window.update()
    time.sleep(0.3)  
    canvas.delete("all")
    
#window.mainloop()
#mb.showwarning("Предупреждение", step_x)

  
    



