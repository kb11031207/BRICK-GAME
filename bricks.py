import turtle
import random

class Bricks:
  def __init__(self):
    self.bricks = []
    self.rng = random.Random()

  def create_turtle(self, num = 10):#CREATES A LISTS OF TURTLES
    self.num = num
    for i in range(self.num):
      tr = turtle.Turtle()
      rng = self.rng.randrange(0,5)
      colors = ["red", "yellow", "green", "blue", "pink"]
      tr.color(colors[rng])
      
      
      self.bricks.append(tr)

  def draw_bricks(self, num = 10, length = 50, height= 40, y_cor=500, dx = 75):#DRAWS BRICKS WITH EACH OF THE TURTLES
    self.create_turtle(num)
    self.no = num
   # self.length = length 
    self.height = height
    #first_layer = se //
    for i, v in enumerate (self.bricks): #GOES THROUGHT THE LIST OF TURTLES
      v.up()
      v.goto(50+dx*i, y_cor)
      v.down()
      v.begin_fill()
      for s in range(4):
        v.forward(self.height)
        v.right(90)
      
        
      v.end_fill()
      v.ht()
        
    
    