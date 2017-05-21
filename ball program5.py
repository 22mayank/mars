import simplegui
import random
w=500
h=500
p1=random.randint(100,200)
p2=random.randint(100,200)
b_p=[p1,p2]
x=random.randint(2,4)
y=random.randint(2,4)
v=[0,0]
t=0

def t_h():
    global b_p,v,x,y,w,h
    b_p[0]=b_p[0]+v[0]
    b_p[1]=b_p[1]+v[1]


def kd_h(k):
    timer3.stop()
    global t
    t=0
    timer2.start()
    if k==simplegui.KEY_MAP["left"]:
        v[0]-=1
    if k==simplegui.KEY_MAP["right"]:
        v[0]+=1
    if k==simplegui.KEY_MAP["up"]:
        v[1]-=1
    if k==simplegui.KEY_MAP["down"]:
        v[1]+=1

def ku_h(k):
    timer2.stop()
    timer3.start()
    if k==simplegui.KEY_MAP["left"]:
        while v[0]!=0:
            v[0]+=1
    if k==simplegui.KEY_MAP["right"]:
        while v[0]!=0:
            v[0]+=t
    if k==simplegui.KEY_MAP["up"]:
        while v[1]!=0:
            v[1]+=1
    if k==simplegui.KEY_MAP["down"]:
        while v[1]!=0:	
            v[1]-=1

def t2_h():
    global t
    t+=1

def t3_h():
    global t
    while t!=0:
        t-=1




def d_h(canvas):
    canvas.draw_circle(b_p,5,1,"red","white")
    
    
def r_h():
    v[0]=0
    v[1]=0
    b_p[0]=200
    b_p[1]=200

frame1=simplegui.create_frame("velocity program",400,400)
frame1.set_draw_handler(d_h)
frame1.add_button("reset",r_h)
frame1.set_keydown_handler(kd_h)
frame1.set_keyup_handler(ku_h)
timer1=simplegui.create_timer(10,t_h)
timer2=simplegui.create_timer(1000,t2_h)
timer3=simplegui.create_timer(100,t3_h)
frame1.start()
timer1.start()