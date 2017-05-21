import simplegui
char_v=" "

def hmm(canvas):
    canvas.draw_text(char_v,[1,99],99,"white")

def k_d(key):
    global char_v
    char_v=chr(key)

def k_u(key):
    global char_v
    char_v=" "

frame1=simplegui.create_frame("key test",100,100)
frame1.set_draw_handler(hmm)
frame1.set_keydown_handler(k_d)
frame1.set_keyup_handler(k_u)
frame1.start()