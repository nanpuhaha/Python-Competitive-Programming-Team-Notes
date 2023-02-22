import math

''' Check if a number is prime '''
def is_prime_number(x):
    return all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1))

print(is_prime_number(4)) # False
print(is_prime_number(7)) # True
