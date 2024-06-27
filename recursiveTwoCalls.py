# Function to calculate power with Divide and Conquer, using two recursive calls

def recursivePower(x, n):
    if n == 0:
      return 1
  
    if n%2 == 0:
      return recursivePower(x, n/2) * recursivePower(x, n/2)
    
    return x * recursivePower(x, (n-1)/2) * recursivePower(x, (n-1)/2)
