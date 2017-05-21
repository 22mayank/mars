"""in this program i used var_check variable to make sure that you can't press stop button again
if the timer is already stopped(i.e. you have already pressed the stop button and didn't press
the start button) otherwise the score can be affected by pressing the stop button again and again 
without pressing the start button"""


import simplegui
ts=0
num1=0
num2=0
var_check="value of timer"
msg1=" "

def format(value):
    m=str(value/600)
    s=str((value%600)/10)
    ts=str((value%600)%10)
    l=len(s)
    if l==1:
        s="0"+s
    timestring = str(m)+":"+str(s)+"."+str(ts)
    return timestring

def time_draw(canvas):
    global ts
    canvas.draw_text("STOP WATCH :  "+format(ts),[30,100],24,"yellow")
    canvas.draw_text("created by : vishal",[228,200],10,"white")
    canvas.draw_text(str(num1)+"/"+str(num2),[260,20],20,"white")
    canvas.draw_text(msg1,[100,120],20,"white")

def t_h():
    global ts
    ts+=1

def sr_t():
    global var_check,msg1
    timer1.start()
    var_check="timer_running"
    msg1=" "

def sp_t():
    global ts,num1,num2,var_check,msg1
    if (var_check=="timer_running"):
        timer1.stop()
        num2+=1
        if (((ts%600)%10)==0):
            num1+=1
        var_check="timer_not_running"
    if (var_check=="timer_not_running"):
        msg1="timer stopped"

def r_t():
    global ts,num1,num2,var_check,msg1
    timer1.stop()
    ts=0
    num1=0
    num2=0
    var_check="value of timer"
    msg1=" "


timer1=simplegui.create_timer(100, t_h)
frame1=simplegui.create_frame("timer",300,200)
frame1.set_draw_handler(time_draw)
frame1.add_button("start",sr_t)
frame1.add_button("stop",sp_t)
frame1.add_button("reset",r_t)
frame1.start()