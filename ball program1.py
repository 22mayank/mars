import simplegui
radius=10
width=500
height=500
position_b=[width/2,height/2]

def d_h(c):
    c.draw_circle(position_b,radius,3,"white","red")

def key_d(k):
    vel=4
    if k==simplegui.KEY_MAP["left"]:
        position_b[0]-=vel
    if k==simplegui.KEY_MAP["right"]:
        position_b[0]+=vel
    if k==simplegui.KEY_MAP["up"]:
        position_b[1]-=vel
    if k==simplegui.KEY_MAP["down"]:
        position_b[1]+=vel

frame1 = simplegui.create_frame("move your ball",width,height)
frame1.set_draw_handler(d_h)
frame1.set_keydown_handler(key_d)
frame1.start()