
def reactangel(*parameter):
    return {"area" :parameter[0]*parameter[1],"perimeter":2*(parameter[0]+parameter[1])}
def Triangle(*parameter):
    return {"area" :0.5*(parameter[0]*parameter[1]),"perimeter":(parameter[0]+parameter[1]+parameter[2])}

def Circle(parameter):
    return {"area" :3.14*parameter**2,"perimeter":2*3.14*parameter}

print(reactangel(20,50))
print(Triangle(20,60,89))
print(Circle(20))
