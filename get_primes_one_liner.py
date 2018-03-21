import math

def get_primes(input_list):
    return (element for element in input_list if is_prime(element))

def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(num) + 1), 2):
            if num % current == 0:
                return False
        return True
    return False

print next(get_primes([1,3,5,8,83]))
