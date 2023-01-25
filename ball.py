import turtle

class Ball:
    """ Ball class represents a circle that moves and bounces """
    
    def __init__(self, center, rad = 10):
        """ Create a new ball, centered at a Point with given radius """
        self.tr = turtle.Turtle() # create a turtle to draw with
        self.center = center # store center of this circle
        (self.dx, self.dy) = (5, 6) # deltas for each movement
        self.rad = rad # ball radius
        self.paused = True # paused == ball won't move
        self.draw() # initial drawing of circle
        
        
    def move(self):
        """ Move self along dx, dy, then re-draw """
        if self.paused:
            return # don't move if paused
        if self.center.y <= 0:
          #self.tr.up()
          #self.tr.goto(400,300)
          # self.tr.down()
          self.center.x = 400
          self.center.y = 300
          self.dx =5
          self.dy=6
          self.paused = True
        if self.center.y == 600:
            self.dy = -6
        
        if self.center.x == 800:
            self.dx = -5
        if self.center.x == 0:
            self.dx =5
        self.center.x += self.dx
        self.center.y += self.dy
        self.draw() # re-draw in new position
        
    
    def draw(self):
        self.tr.clear() # clear previous drawings for this turtle
        self.tr.penup()
        self.tr.goto(self.center.x, self.center.y - self.rad) # go to just below to draw
        self.tr.pendown()
        self.tr.fillcolor("black")
        self.tr.begin_fill()
        self.tr.circle(self.rad)
        self.tr.ht()
        self.tr.end_fill()
    
        
       



        
        
    def pause(self):
        self.paused = not self.paused
        
        
    
