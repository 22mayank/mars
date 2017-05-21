import simplegui
image=simplegui.load_image("file:///C:/Users/vishal/Pictures/wallpapers/interstellar_black_hole-wallpaper-1366x768.jpg")

i_w=1366
i_h=768

scale=2

c_w=i_w//scale
c_h=i_h//scale

mag_size=100
mag_pos=[c_w//2,c_h//2]

def click(pos):
    global mag_pos
    mag_pos=pos

def draw(canvas):
    canvas.draw_image(image,
                     [i_w//2,i_h//2],[i_w,i_h],
                     [c_w//2,c_h//2],[c_w,c_h])
    i_centre=[mag_pos[0]*scale,mag_pos[1]*scale]
    i_rectangle=[mag_size,mag_size]
    canvas.draw_image(image,
                     i_centre,i_rectangle,
                     mag_pos,[mag_size,mag_size])

frame1=simplegui.create_frame("image magnifier",c_w,c_h)
frame1.set_draw_handler(draw)
frame1.set_mouseclick_handler(click)
frame1.start()