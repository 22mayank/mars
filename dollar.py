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
    
print convert(11.23)
print convert(11.00)
print convert(0.23)
print convert(0.0)
print convert(0)
print convert(-1.23)