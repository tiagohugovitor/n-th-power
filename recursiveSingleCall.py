# Function to calculate power with Divide and Conquer optimized using only one recursive call

def recursivePowerOptimized(x, n):
    if n == 0:
      return 1
    temp = recursivePowerOptimized(x, int(n/2))
    if n%2 == 0:
      return temp * temp 
    
    return x * temp * temp
