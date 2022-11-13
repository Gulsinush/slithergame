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
from datetime import timedelta, datetime
timesleep=0.3
counter=0

basic_coord = ([300,300,320,320],
               [320,300,340,320],
               [340,300,360,320],
               [360,300,380,320]
               )

def score_field():
    global size,top_boarder
    canvas.create_rectangle(0,0,size,top_boarder, outline="black")
    canvas.create_text(10, 15, anchor="w", text="Score:     "+ str(counter))
    canvas.create_text(400, 15, anchor="w", text="Time:     "+ str(datetime.now()-start_time)[:-7])



class Snake:
    
    coord_list = []
    
    step_x =0
    step_y =0
    flag_change=False
    
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
        if self.flag_change==False:
            
            if self.step_y==0 and step_x == 0:
               self.step_y = step_y
               self.step_x = step_x
    
            if self.step_x==0 and step_y == 0 :
                self.step_x = step_x
                self.step_y = step_y
            self.flag_change=True
            
    def eating(self, food):
        if self.coord_list[0]==food.food_coord:
            food.change_food()
            food.draw()
            self.coord_list.append([self.coord_list[-1][0]-self.step_x, self.coord_list[-1][1]-self.step_y, self.coord_list[-1][2]-self.step_x, self.coord_list[-1][3]-self.step_y])
            global counter
            counter+=1
            global timesleep
            timesleep*=0.9
            
            
    def game_over(self):
        for i in range(len(self.coord_list[0])):
            if (i%2==0 and self.coord_list[0][i]<0) or (i%2==1 and self.coord_list[0][i]<top_boarder) or self.coord_list[0][i]>size:
                mb.showwarning("Attention","Результат: " + str(counter))
                window.destroy()
        for j in range(1, len(self.coord_list)):
            if self.coord_list[j]==self.coord_list[0]:
                mb.showwarning("Attention","Результат: " + str(counter))
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
        food_x = rd.randrange(0, 580, 20)
        food_y = rd.randrange(top_boarder, 580, 20)
        self.food_coord = [food_x, food_y, food_x+20, food_y+20]
        

            
window = tk.Tk()
window.geometry('600x600')
window.title("Snake")
window.iconbitmap('logo.ico')
size = 600
top_boarder=40

canvas = tk.Canvas(window, width=size, height=size)
canvas.pack()

start_time=datetime.now()
snake1 = Snake()
food = Food()

while True:
    snake1.flag_change=False
    snake1.draw()
    food.draw()
    score_field()
    window.update_idletasks()
    window.update()
    window.bind('<KeyRelease-Left>',lambda e, step_x=-20, step_y=0: 
            snake1.change_step(e,step_x, step_y))
    window.bind('<KeyRelease-Right>',lambda e, step_x=20, step_y=0: 
            snake1.change_step(e,step_x, step_y))
    window.bind('<KeyRelease-Up>',lambda e, step_x=0, step_y=-20: 
            snake1.change_step(e,step_x, step_y))
    window.bind('<KeyRelease-Down>',lambda e, step_x=0, step_y=20: 
            snake1.change_step(e,step_x, step_y))
    snake1.change_coord(food)

    time.sleep(timesleep)  
    canvas.delete("all")
    
    
#window.mainloop()
#mb.showwarning("Предупреждение", step_x)

  
    



