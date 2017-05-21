#first python function to calculate area of circle
def area_circle(radius):
    area=(22/7.0)*(radius**2)
    return area
print area_circle(1)
def vol_sphere(radius):
    vol=4*(area_circle(radius))*radius
    return vol
print vol_sphere(1)
def function2callboth(radius):
    a1=area_circle(radius)
    a2=vol_sphere(radius)
    a3=a1+a2
    return a1,a2,a3
a4=function2callboth(222)[0]
print a4