import simplegui
import random
msg="hello!"
position=[50,50]
h=600
w=600
i=2000
size=24
color="red"

def i_h(text):
    global msg
    msg=text

def draw(canvas):
    canvas.draw_text(msg, position, size, color)

def t_h():
    global size,color
    x=random.randrange(0,500)
    y=random.randrange(0,500)
    z=random.randrange(5,50)
    size=z
    position[0]=x
    position[1]=y
    r=random.randint(1,4)
    if (r==1):
        color="White"
    if (r==2):
        color="Green"
    if (r==3):
        color="Blue"
    if (r==4):
        color="Yellow"

frame1=simplegui.create_frame("screen saver", w, h)
frame1.set_draw_handler(draw)
frame1.add_input("messsage",i_h,100)
timer=simplegui.create_timer(i, t_h)
frame1.start()
timer.start()