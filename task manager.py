import simplegui

task=[]

def i1_h(text):
    global task
    task.append(text)

def i2_h(text):
    global task
    if int(text)>0 and int(text)<len(task):
        task.pop(int(text)-1)

def i3_h(text):
    global task
    if text in task:
        task.remove(text)


def d_h(canvas):
    global task
    n=0
    a=100
    while n<len(task):
        canvas.draw_text(str(n+1)+": "+task[n],[50,a],25,"white")
        a+=50
        n+=1

    
frame1=simplegui.create_frame("task manager",700,500)
frame1.add_input("add new task",i1_h,200)
frame1.add_input("remove task by number",i2_h,100)
frame1.add_input("remove message",i3_h,100)
frame1.set_draw_handler(d_h)
frame1.start()