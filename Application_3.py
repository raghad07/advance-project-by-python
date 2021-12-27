import numpy as np
from PIL import Image

class Canvas:

  def __init__(self,height,width,color):
    self.height=height
    self.width=width
    self.color=color

    # Creat a 3d numpy array of zeros
    self.data=np.zeros((self.height,self.width,3), dtype=np.uint8)

    # Change (0,0,0) with user given value for color
    self.data[:]=self.color

  def make(self,imagepath):
    # convert the current array into an image file
    img=Image.fromarray(self.data,'RGB')
    img.save(imagepath)
    

class Rectangle:

  def __init__(self,x,y,height,width,color):
    self.x=x
    self.y=y
    self.height=height
    self.width=width
    self.color=color

  def draw(self,canvas):
    #draw itself into the canvas
    #change a slice of the array with nw value
    canvas.data[self.x : self.x + self.height, self.y: self.y +self.width]=self.color

class Square:

  def __init__(self,x,y,side,color):
    self.x=x
    self.y=y
    self.side=side
    self.color=color 

  def draw(self,canvas):
    canvas.data[self.x: self.x+self.side,self.y: self.y+self.side]=self.color  

canvas=Canvas(height=20,width=30,color=(255,255,255)) 
r1=Rectangle(x=1,y=6,height=7,width=10,color=(100,200,125)) 
r1.draw(canvas) 
s1=Square(x=1,y=3,side=3,color=(0,100,222))  
s1.draw(canvas) 
canvas.make('canvas.png') 

canvas_width=int(input('enter canvas width: '))
canvas_height=int(input('enter canvas height: '))

colors={"white" :(255,255,255) ,"black": (0,0,0)}
canvas_color=input('enter canvas color (white or black): ')

canvas_width=int(input('enter canvas width: '))
canvas_height=int(input('enter canvas height: '))

colors={"white" :(255,255,255) ,"black": (0,0,0)}
canvas_color=input('enter canvas color (white or black): ')

canvas=Canvas(height=canvas_height,width=canvas_width, color=colors[canvas_color])

while True:
  shape_type=input('what do you like to draw? enter quit to quit')
  if shape_type.lower()=='rectangle':
     rec_x=int(input('enter x of the rectangle: '))
     rec_y=int(input('enter y of the rectangle: '))
     rec_width=int(input('enter the width of the rectangle:' ))
     rec_height=int(input('enter the height of the rectangle:' ))
     red=int(input('how much red should the  rectangle have?' ))
     green=int(input('how much green? '))
     blue=int(input('how much blue? '))
     r1=Rectangle(x=rec_x,y=rec_y,height=rec_height,width=rec_width ,color=(red,green,blue))
     r1.draw(canvas)
  if shape_type.lower() =='square':
    sqr_x=int(input('enter x of the square: '))
    sqr_y=int(input('enter y of the square: '))
    sqr_said=int(input('enter y of the said: '))
    red=int(input('how much red should the  square have?' ))
    green=int(input('how much green? '))
    blue=int(input('how much blue? '))
    s1=Square(x=rec_x,y=rec_y,side=sqr_said,color=(red,green,blue))
    s1.draw(canvas)
  if shape_type=='quit':
    break   
canvas.make('canvas.png')       
