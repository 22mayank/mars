import simplegui

image_col=(0,1,2,3,4,5,6,7)
image_row=(0,1)
image1=simplegui.load_image("file:///C:/Users/vishal/Pictures/wallpapers/prince_of_persia_game_2-1366x768.jpg")
part_size=(170,384)
part_centre=(85,192)

class Parts:
    def __init__(self,image_row,image_col):
        self.col_no=image_col
        self.row_no=image_row
    
    def draw(self,canvas,loc):
        part_pos=[self.col_no*part_size[0]+part_centre[0],
                  self.row_no*part_size[1]+part_centre[1]]
        canvas.draw_image(image1,part_pos,part_size,loc,part_size)     


def d_h(canvas):
    i_part.draw(canvas,(100,200))


frame1=simplegui.create_frame("image part drawer",200,400)
frame1.set_draw_handler(d_h)
i_part=Parts(1,1)
frame1.start()