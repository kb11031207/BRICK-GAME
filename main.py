import turtle, ball, paddle, bricks
from point import Point 


# constants for window width & height
WN_WIDTH = 800
WN_HEIGHT = 600

class Game:
    """ Represents a bricks game, storing the objects and updating """
    
    def __init__(self, wn):
        self.wn = wn # store the window object
        self.wn.title("Bricks Game -- Press SPACE to start")
        self.wn.setup(WN_WIDTH, WN_HEIGHT)
        self.wn.setworldcoordinates(0, 0, WN_WIDTH, WN_HEIGHT)

        self.wn.tracer(0) # only redraw on wn.update() calls, to speed up game
        self.ball = ball.Ball(Point(WN_WIDTH // 2, WN_HEIGHT // 2)) # middle
        self.paddle = paddle.Paddle(Point(400, 100))
        self.brick = bricks.Bricks()
        #self.brick.draw_bricks()#DRAWS BRICK
        self.brick.draw_bricks(5, 50, 75, 450, 150)
        self.level = 0
        self.collide_padddle = False
        self.change_dir_1 = self.ball.center.x >= self.paddle.pos.x+75 and self.ball.center.x <= self.paddle.pos.x+120
        self.change_dir_2 = self.ball.center.x in range(self.paddle.pos.x+75+19+19, self.paddle.pos.x+120)
        self.change_dir_3 = self.ball.center.x in range(self.paddle.pos.x+75+19+19, self.paddle.pos.x+75+19+19+19)
        self.change_dir_4 = self.ball.center.x in range(self.paddle.pos.x+75+19+19+19, self.paddle.pos.x+75+19+19+19+19)
        
       # self.brick.draw_bricks(5, 50, 75, 400)
        self.wn.onkeypress(self.ball.pause, 'space')
        self.wn.onkeypress(self.paddle.move_right, "Right")
        self.wn.onkeypress(self.paddle.move_left, "Left")
        self.wn.onkeypress(self.cheat_code, "a")
        self.wn.listen()
        
    def play(self):
        self.ball.move()
        self.paddle.draw() 
        
      
        self.brick_collide()#CHECKS COLLISSION
        self.change_level()
        self.paddle_collide()#CHECKS COLLISSION
       # self.change_direction()
        self.wn.update() # redraw all elements on screen (end_fill does too)
        self.wn.ontimer(self.play, 5) # reset timer, best way loop events        

    def paddle_collide(self):
      if self.ball.center.y in range (self.paddle.pos.y, self.paddle.pos.y+self.paddle.length):
        
        if self.ball.center.x in range(self.paddle.pos.x, self.paddle.pos.x+self.paddle.width):
          print(self.change_dir_1)

          #if self.ball.center.x >= self.paddle.pos.x and self.ball.center.x <= self.paddle.pos.x+75
          #for the directional bouncing off the paddle
          if self.ball.center.x >= self.paddle.pos.x+15 and self.ball.center.x <= self.paddle.pos.x+13*2:
            self.ball.dx = -1
          elif self.ball.center.x >= self.paddle.pos.x+13*2 and self.ball.center.x <= self.paddle.pos.x+13*3:
            self.ball.dx = -2
          elif self.ball.center.x >= self.paddle.pos.x+13*3 and self.ball.center.x <= self.paddle.pos.x+13*4:
            self.ball.dx =  -3
          elif self.ball.center.x >= self.paddle.pos.x+13*4 and self.ball.center.x <= self.paddle.pos.x+13*5:
            self.ball.dx =  -4
          elif self.ball.center.x >= self.paddle.pos.x+13*5 and self.ball.center.x <= self.paddle.pos.x+(13*6):
            self.ball.dx =  -5
          if self.ball.center.x >= self.paddle.pos.x+(13*6) and self.ball.center.x <= self.paddle.pos.x+13*7:
            self.ball.dx = 0
            print("work?")
          elif self.ball.center.x >= self.paddle.pos.x+13*7 and self.ball.center.x <= self.paddle.pos.x+13*8:
            self.ball.dx = -1
          elif self.ball.center.x >= self.paddle.pos.x+13*2*8 and self.ball.center.x <= self.paddle.pos.x+13*9:
            self.ball.dx = -2
          elif self.ball.center.x >= self.paddle.pos.x+13*9 and self.ball.center.x <= self.paddle.pos.x+13*10:
            self.ball.dx =  -3
          elif self.ball.center.x >= self.paddle.pos.x+13*10 and self.ball.center.x <= self.paddle.pos.x+13*11:
            self.ball.dx =  -4
          elif self.ball.center.x >= self.paddle.pos.x+13*11 and self.ball.center.x <= self.paddle.pos.x+13*12:
            self.ball.dx =  -5
         # if self.ball.center.x in range(self.paddle.pos.x+75, self.paddle.pos.x+75+19):
         # elif self.ball.center.x in range(self.paddle.pos.x+75+19, self.paddle.pos.x+75+19):
          #  self.ball.dx = 0 
          self.ball.dy *= -1
          self.collide_padddle = True
          print("does this work?")
          print((self.ball.dx, self.ball.dy))
          if self.ball.center.x == self.paddle.pos.x or self.ball.center.x == self.paddle.pos.x+self.paddle.width:
            self.ball.dx *= -1

    def brick_collide(self):#
      for v, i in enumerate(self.brick.bricks):
        #if self.ball.center.y in range(int(i.ycor()), int(i.ycor()) - self.brick.height):
          if self.ball.center.x in range(int(i.xcor()), int(i.xcor()+self.brick.height)) and self.ball.center.y in range(int(i.ycor()) - self.brick.height, int(i.ycor())) :
            print("BRICK TEST")
            self.ball.dy *= -1
           # i.clear()
            

            if self.ball.center.x == i.xcor() or self.ball.center.x == i.xcor()+self.brick.height:
              self.ball.dx *= -1
            i.clear()
            del self.brick.bricks[v]#DELETES BRICK FROM THE LIST

    def change_level(self):
      if self.brick.bricks ==[]:
        if self.level == 0:
           self.brick.draw_bricks()
           self.level += 1
        else :
          self.brick.draw_bricks(15, 50, 40, 500, 50)#draws with 15 turtles
          self.level=0
      
    def cheat_code(self):
        for i in self.brick.bricks:
          i.clear()#clears the drawing of each turtle
        self.brick.bricks = []#makes the list empty

   # def change_direction(self):
    # if self.collide_padddle == True:
     #   if self.ball.center.x in range(self.paddle.pos.x+75, self.paddle.pos.x+190):
      #    self.ball.dx = 0 
          #self.ball.tr.setheading(0)
         # print(self.ball.tr.heading())
     #   self.collide_paddle = False
        
        
      
def main():
    wn = turtle.Screen() # create the window to be able to edit later
    game = Game(wn) # object to run the game, updates window
    game.play()
    wn.mainloop()


main()

