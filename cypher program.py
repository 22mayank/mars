import simplegui
import random

msg=""
lis1=[1,2,3]
print lis1
lis1.pop()
print lis1
def i_h(text):
    global msg
    msg=text

a_l1="abcdefghijklmnopqrstuvwxyz"
a_l2=list(a_l1)
random.shuffle(a_l2)
dict1={}
for alpha in a_l1:
    dict1[alpha] = a_l2.pop()
print dict1

def e_h():
    global msg,dict1
    e_msg=""
    for alpha in msg:
        e_msg+=dict1[alpha]
    print msg+"  encodes to  "+e_msg


def d_h():
    d_msg=''
    for alpha in msg:
        for key in dict1:
            if alpha==dict1[key]:
                d_msg+=key
    print msg+" decoded to "+ d_msg

frame1=simplegui.create_frame("msg encoding",1,200)
frame1.add_input("message",i_h,200)
frame1.add_button("encode",e_h)
frame1.add_button("decode",d_h)
frame1.start()