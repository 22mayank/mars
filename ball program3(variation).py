import simplegui
import math
ball_pos=[]
ball_color="red"

def mc_h(position):   
    global ball_pos,ball_color
    remove_ball_list=[]
    flag=True
    for ball in ball_pos:
        if (math.sqrt(((ball[0]-position[0])**2)+((ball[1]-position[1])**2)))<10:
            remove_ball_list.append(ball)
            flag = False
    if flag==True:
        ball_pos.append(position)

    for ball in remove_ball_list:
        ball_pos.pop(ball_pos.index(ball))

def d_h(canvas):
    for ball in ball_pos:
        canvas.draw_circle(ball,10,1,"white",ball_color)

frame1=simplegui.create_frame("ball",500,500)
frame1.set_draw_handler(d_h)
frame1.set_mouseclick_handler(mc_h)
frame1.start()