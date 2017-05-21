import simplegui
import random
w=500
h=500
p1=random.randint(100,200)
p2=random.randint(100,200)
b_p=[p1,p2]
x=random.randint(2,4)
y=random.randint(2,4)
v=[4,3]

def b_h():
    timer1.start()

def t_h():
    global b_p,v,x,y,w,h
    if (b_p[0]>=395)or(b_p[0]<=5):
        v[0]=-v[0]
    if (b_p[1]>=395)or(b_p[1]<=5):
        v[1]=-v[1]
    b_p[0]=b_p[0]+v[0]
    b_p[1]=b_p[1]+v[1]
        
#difference of 1 value of both v[0] and v[1] is to create
#a deviation in the direction of movement of ball
        
        
def s_h():
    timer1.stop()
    
def re_h():
    global b_p,v
    v=[4,3]
    x1=random.randint(50,450)
    y1=random.randint(50,450)
    timer1.stop()
    b_p=[x1,y1]


def d_h(canvas):
    canvas.draw_circle(b_p,5,1,"red","white")
    
    
frame1=simplegui.create_frame("velocity program",400,400)
frame1.set_draw_handler(d_h)
frame1.add_button("start",b_h)
frame1.add_button("stop",s_h)
frame1.add_button("reset",re_h)
timer1=simplegui.create_timer(10,t_h)
frame1.start()