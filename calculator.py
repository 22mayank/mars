import simplegui
num1=0
num2=0
def swap():
    global num1
    global num2
    temp=num1
    num1=num2
    num2=temp
    print "num1 is : "+str(num1)
    print "num2 is : "+str(num2)

def add():
    global num1
    global num2
    print "num1 is : "+str(num1)
    print "num2 is : "+str(num2)
    num2=int(num1)+int(num2)
    print "NEW num2 is : "+str(num2)

def sub():
    global num1
    global num2
    print "num1 is : "+str(num1)
    print "num2 is : "+str(num2)
    num2=int(num1)-int(num2)
    print "NEW num2 is : "+str(num2)

def remainder():
    global num1
    global num2
    print "num1 is : "+str(num1)
    print "num2 is : "+str(num2)
    r=int(num1)%int(num2)
    print "Remainder of num1 divided by num2 is : "+str(r)

def v_num1(numx):
    global num1
    num1=numx

def v_num2(numx):
    global num2
    num2=numx
    
    
frame1=simplegui.create_frame("calculator", 300,300)
frame1.add_button("swap", swap)
frame1.add_button("add", add)
frame1.add_button("difference", sub)
frame1.add_button("remainder", remainder)
frame1.add_input("enter num1",v_num1,100)
frame1.add_input("enter num2",v_num2,100)
frame1.start()