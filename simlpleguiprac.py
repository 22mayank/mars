import simplegui
counter = 0
def fun1():
    global counter 
    counter+=1
    print counter

def fun2():
    global counter 
    counter-=1
    print counter

def b_p():
    timer1.start()

def b_p_stop():
    timer1.stop()
    
frame1=simplegui.create_frame("my first frame", 100,100)
frame1.add_button("value printer ", b_p)
frame1.add_button("Stop button ", b_p_stop)
timer = simplegui.create_timer(2000, fun1)
timer1 = simplegui.create_timer(1000, fun2)
frame1.start()
timer.start()