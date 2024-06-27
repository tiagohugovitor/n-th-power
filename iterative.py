# Function to calculate power without Divide and Conquer, using an iterative method

def power(x, n):
    pow = 1

    for _  in range(n):
        pow = pow * x
    
    return pow
