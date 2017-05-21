import simplegui
import random
vp1=0
vp2=0
w=500
h=300
pad1_p=h/2
pad2_p=h/2
p_w=10
p_h=40
ball_p=[w/2,h/2]
ball_v=[3,3]
p1=0
p2=0
pad_vel=3
in_b_v=0
p1_name=" "
p2_name=" "
num_p=1
winner=" "

"""to change the velcity of paddle change the variable pad_vel but not the timer time of timer1 cause it will affect the 
increase of velocity of ball after every 10 seconds as i have not used any other timer"""

def i1_h(text):
    global p1_name
    p1_name=text

def i2_h(text):
    global p2_name
    p2_name=text
    
def i3_h(text):
    global num_p
    num_p=int(text)


def kd_h(k):
    global vp1,vp2,pad1_p,pad2_p
    if k==simplegui.KEY_MAP["up"]:
        if pad1_p>259:
            pad1_p=259
            vp1=-pad_vel
        else:
            vp1=-pad_vel
    if k==simplegui.KEY_MAP["down"]:
        if pad1_p<0:
            pad1_p=0
            vp1=pad_vel
        else:
            vp1=pad_vel
    if k==simplegui.KEY_MAP["w"]:
        if pad2_p>259:
            pad2_p=259
            vp2=-pad_vel
        else:
            vp2=-pad_vel
    if k==simplegui.KEY_MAP["s"]:
        if pad2_p<0:
            pad2_p=0
            vp2=pad_vel
        else:
            vp2=pad_vel

def ku_h(k):
    global vp1,vp2
    if k==simplegui.KEY_MAP["up"]:
        vp1=0
    if k==simplegui.KEY_MAP["down"]:
        vp1=0
    if k==simplegui.KEY_MAP["w"]:
        vp2=0
    if k==simplegui.KEY_MAP["s"]:
        vp2=0

def t_h():
    global in_b_v,pad1_p,pad2_p,vp1,vp2
    if (pad1_p>=0)and(pad1_p<=259):
        pad1_p+=vp1
    if (pad2_p>=0)and(pad2_p<=259):
        pad2_p+=vp2
    
def t3_h():
    global in_b_v,ball_v
    in_b_v+=1
    if (in_b_v%10)==0:
        if (ball_v[0]>0)and(ball_v[1]>0):
            ball_v[0]+=1
            ball_v[1]+=1
        if (ball_v[0]>0)and(ball_v[1]<0):
            ball_v[0]+=1
            ball_v[1]-=1
        if (ball_v[0]<0)and(ball_v[1]<0):
            ball_v[0]-=1
            ball_v[1]-=1
        if (ball_v[0]<0)and(ball_v[1]>0):
            ball_v[0]-=1
            ball_v[1]+=1

def t4_h():
    global winner,p1_name,p2_name,p1,p2,num_p
    if p2==num_p:
        winner=p2_name+" wins"
    if p1==num_p:
        winner=p1_name+" wins"

def t5_h():
    global winner
    winner=" "


def t2_h():
    t=0
    global ball_p,ball_v,p1,p2,in_b_v,num_p
    if (ball_p[1]>=290)or(ball_p[1]<=10):
        ball_v[1]=-ball_v[1]
    if (ball_p[0]<=20)and(pad1_p<=ball_p[1])and(ball_p[1]<=pad1_p+p_h):
        ball_v[0]=-ball_v[0]
    if (ball_p[0]>=480)and(pad2_p<=ball_p[1])and(ball_p[1]<=pad2_p+p_h):
        ball_v[0]=-ball_v[0]
    if (ball_p[0]<=20)and((ball_p[1]<pad1_p)or(ball_p[1]>pad1_p+p_h)):
        in_b_v=0
        p2+=1
        if p2==num_p:
            timer1.stop()
            timer2.stop()
            timer3.stop()
        ball_v=[3,3]
        ball_p=[w/2,h/2]
        t=random.randint(1,4)
        if t==1:
            ball_v[0]=ball_v[0]
            ball_v[1]=ball_v[1]
        if t==2:
            ball_v[0]=ball_v[0]
            ball_v[1]=-ball_v[1]
        if t==3:
            ball_v[0]=-ball_v[0]
            ball_v[1]=-ball_v[1]
        if t==4:
            ball_v[0]=-ball_v[0]
            ball_v[1]=ball_v[1]

    if (ball_p[0]>=480)and((ball_p[1]<pad2_p)or(ball_p[1]>pad2_p+p_h)):
        in_b_v=0
        p1+=1
        if p1==num_p:
            timer1.stop()
            timer2.stop()
            timer3.stop()
        ball_v=[3,3]
        ball_p=[w/2,h/2]
        t=random.randint(1,4)
        if t==1:
            ball_v[0]=ball_v[0]
            ball_v[1]=ball_v[1]
        if t==2:
            ball_v[0]=ball_v[0]
            ball_v[1]=-ball_v[1]
        if t==3:
            ball_v[0]=-ball_v[0]
            ball_v[1]=-ball_v[1]
        if t==4:
            ball_v[0]=-ball_v[0]
            ball_v[1]=ball_v[1]

    ball_p[0]=ball_p[0]+ball_v[0]
    ball_p[1]=ball_p[1]+ball_v[1]

def s_h():
    timer1.start()
    timer2.start()
    timer3.start()

    
def re_h():
    global pad1_p,pad2_p,ball_p,ball_v,p1,p2,pad_vel,in_b_v
    pad1_p=h/2
    pad2_p=h/2
    ball_p=[w/2,h/2]
    ball_v=[3,3]
    p1=0
    p2=0
    pad_vel=5
    in_b_v=0
    timer1.stop()
    timer2.stop()
    timer3.stop()

def d_h(canvas):
    global ball_v
    v_u=0
    if ball_v[0]<0:
        v_u=-ball_v[0]
    if ball_v[0]>0:
        v_u=ball_v[0]
    canvas.draw_line([w/2,0],[w/2,h],2,"blue")
    canvas.draw_line([10,0],[10,h],1,"red")
    canvas.draw_line([490,0],[490,h],1,"red")
    canvas.draw_line([0,0],[0,h],1,"yellow")
    canvas.draw_polygon([[0,pad1_p],[0,pad1_p+p_h],[p_w,pad1_p+p_h],[p_w,pad1_p]],1,"red","white")
    canvas.draw_polygon([[490,pad2_p],[490,pad2_p+p_h],[490+p_w,pad2_p+p_h],[490+p_w,pad2_p]],1,"red","white")
    canvas.draw_circle(ball_p,10,1,"white","white")
    canvas.draw_text(str(p1),[100,200],100,"red")
    canvas.draw_text(str(p2),[330,200],100,"red")
    canvas.draw_text("game time in seconds :"+str(in_b_v),[80,270],10,"yellow")
    canvas.draw_text("ball velocity :"+str(v_u),[330,270],10,"yellow")
    canvas.draw_text(winner,[130,100],50,"yellow")



frame1=simplegui.create_frame("pong game",w,h)
frame1.set_draw_handler(d_h)
frame1.set_keydown_handler(kd_h)
frame1.set_keyup_handler(ku_h)
frame1.add_button("reset",re_h)
frame1.add_button("start",s_h)
frame1.add_input("player1 name",i1_h,150)
frame1.add_input("player2 name",i2_h,150)
frame1.add_input("number of points",i3_h,50)
timer1=simplegui.create_timer(10,t_h)
timer2=simplegui.create_timer(30,t2_h)
timer3=simplegui.create_timer(1000,t3_h)
timer4=simplegui.create_timer(500,t4_h)
timer5=simplegui.create_timer(1000,t5_h)
frame1.start()
timer4.start()
timer5.start()