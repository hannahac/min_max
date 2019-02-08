import math
def is_fibonacci(n):
    a = 5 * (n ** 2) + 4
    b = 5 * (n ** 2) - 4
    if 5 * (n ** 2) + 4 == int(math.sqrt(a)) * int(math.sqrt(a)): 
        return True
    if 5 * (n ** 2) - 4 == int(math.sqrt(b)) * int(math.sqrt(b)):
        return True     
    return False

for n in range(30g):
    print(is_fibonacci(n))