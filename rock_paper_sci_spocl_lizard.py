import random
def n_t_number(n):
    if (n=="rock"):
        num=0
    elif (n=="spock"):
        num=1
    elif (n=="paper"):
        num=2
    elif (n=="lizard"):
        num=3
    elif (n=="scissor"):
        num=4
    else:
        print "invalid name"
    return num

def num_t_n(num):
    if (num==0):
        n="rock"
    elif (num==1):
        n="spock"
    elif (num==2):
        n="paper"
    elif (num==3):
        n="lizard"
    elif (num==4):
        n="scissor"
    else:
        print "invalid number"
    return n

def rpsls(guess):
    player_num=n_t_number(guess)
    comp_number=random.randint(0,4)
    win=(player_num-comp_number)%5
    if (win==1 or win==2):
        winner="player"
    elif (win==3 or win==4):
        winner="computer"
    elif (win==0):
        winner="there is no winner, it's a tie"
    print "\n"
    print "player choice: "+guess
    print "computer choice: "+num_t_n(comp_number)
    print "winner is : "+ winner
    return None

rpsls("spock")
rpsls("rock")
rpsls("paper")
rpsls("scissor")
rpsls("lizard")