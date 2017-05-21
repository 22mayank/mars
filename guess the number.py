import random
import simplegui
n=0
g=0
def f_r1():
    global g,n
    n=random.randint(0,100)
    g=7
    print "new game initialized: range from 0 to 100"
    print "number of guesses are :"+str(g)

def check(t):
    global g,n
    g=g-1
    if ((g+1)>0):
        print "guess : "+t
        print "number of remaining guesses :"+str(g)
        if ((int(t)<n) and (g+1)>0):
            print "higher"
        elif ((int(t)>n) and (g+1)>0):
            print "lower"
        elif (int(t)==n):
            print "correct"
            print "\n"
            f_r1()
    if ((g+1)<=0):
        print "no more guesses left, YOU LOOSE!!"
        print "\n"
        f_r1()

frame1=simplegui.create_frame("guess the number",200,200)
frame1.add_button("create game",f_r1)
frame1.add_input("enter your guess",check,100)
frame1.start()