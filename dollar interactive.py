import simplegui
input1 = 1.12
def names(val1,val2):
    s1=str(val1)+" "+val2
    if (val1>1):
        s1=s1+"s"
    return s1

def convert(val):
    d=int(val)
    c=round(100*(val-int(val)))
    d1=names(d,"dollar")
    c1=names(c,"cent")
    if d==0 and c==0:
        return "you got no money!"
    elif d==0:
        return c1
    elif c==0:
        return d1
    else:
        return d1+" and "+c1
    
def dh(canvas):
    canvas.draw_text(convert(input1), [60,100], 24, "White")

def ih(text):
    global input1
    input1=float(text)

frame2 = simplegui.create_frame("converter", 300, 200)
frame2.set_draw_handler(dh)
frame2.add_input("enter money",ih,100)
frame2.start()