import math # using for pi value


def area(r):
    '''
    Receive:
        r (int/float): radius of circle
    Return:
        circle area (float): S = Pi*r^2  
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Receive:
        r (int/float): radius of circle
    Return:
        circle perimeter (float): P = 2*Pi*r
    '''
    return 2 * math.pi * r

