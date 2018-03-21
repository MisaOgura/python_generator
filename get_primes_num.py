import math

def sum_prime_num_up_to(limit):
    total = 2
    for next_prime in get_primes(3):
        if next_prime < limit:
            print 'prime number: %d' % next_prime
            total += next_prime
        else:
            print 'sum of the prime numbers found below %d: %d' % (limit, total)
            return

def get_primes(num):
    while True:
        if is_prime(num):
            yield num
        num += 1

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

sum_prime_num_up_to(limit=1000)
