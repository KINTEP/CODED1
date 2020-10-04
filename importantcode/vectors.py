def magnitude(x,y):
    mag = ((x[0] - y[0])**2) + (((x[1] - y[1])**2))
    return mag**(1/2)
    
def grad(x,y):
    mag = ((x[1] - y[1]))/((x[0] - y[0]))
    return mag

def vector_direction(a,b):
    if a != 0:
        return np.degrees(np.arctan(b/a))
    return 0

def vector_direction3(a,b,c):
    d = ((a**2) + (b**2))**(1/2)
    return np.degrees(np.arctan(c/d))

def vector_magnitude(a,b):
    return np.sqrt(a**2 + b**2)

def vector_magnitude3(a,b,c):
    return np.sqrt(a**2 + b**2 + c**2)

def angle_two_vectors(a,b):
    mag = magnitude(a,b)
    angle = np.dot(a,b)/mag
    return np.degrees(np.arccos(angle))