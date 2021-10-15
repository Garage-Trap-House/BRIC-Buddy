import math as math 

def talhaInput (a,b):
    answer = math.modf(a,b)
    return str(answer)

def mathAttempt(n, k):

    num = math.pi

    combination = math.comb(n, k)

    num_string = str(num)

    return str(combination)

def abdulAttempt(x, y):
    result = math.copysign(x,y)
    return str(result)

