import turtle
from point import Point

class Paddle:
    
    def __init__(self, pos, width = 150, length = 20):
        self.tr = turtle.Turtle()
        self.width = width
        self.length = length
        self.pos = pos
        self.dx = 15
       
                    
    def draw(self):
        self.tr.penup()
        self.tr.goto(self.pos.x, self.pos.y)
        self.tr.pendown()
        for i in range(2): 
            self.tr.fillcolor("blue")
            self.tr.begin_fill()
            self.tr.forward(self.width)
            self.tr.left(90)
            self.tr.forward(self.length)
            self.tr.left(90)
            self.tr.end_fill()
            self.tr.hideturtle()
            
    def move_left(self):
        self.tr.clear()
        if self.pos.x < 0:
             self.pos.x = self.pos.x
        else:
            self.pos.x -= self.dx
        self.draw()
        
    def move_right(self):
        self.tr.clear()
        if self.pos.x >= 650:
            self.pos.x = self.pos.x
        else:
            self.pos.x += self.dx
        self.draw()
        
#     def collision:
        
        
                
             


        
        
        