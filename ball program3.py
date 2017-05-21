import simplegui
import math
ball_pos=[]
ball_color="red"

def mc_h(position):   
    global ball_pos,ball_color
    flag=True
    for ball in ball_pos:
        if (math.sqrt(((ball[0]-position[0])**2)+((ball[1]-position[1])**2)))<10:
            ball[2]="green"
            flag = False
    if flag==True:
        ball_pos.append([position[0],position[1],"red"])

def d_h(canvas):
    for ball in ball_pos:
        canvas.draw_circle([ball[0],ball[1]],10,1,"white",ball[2])

frame1=simplegui.create_frame("ball",500,500)
frame1.set_draw_handler(d_h)
frame1.set_mouseclick_handler(mc_h)
frame1.start()