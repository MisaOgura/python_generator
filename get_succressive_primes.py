import math

def get_successive_primes(iterations, base=10):
    prime_generator = get_primes(base)
    prime_generator.send(None)

    for power in range(iterations): # starts from zero
        val = prime_generator.send(base ** power)
        print 'smallest number after %d to the power of %d is %d' % (
            base, power, val)

# generator function
def get_primes(num):
    while True:
        if is_prime(num):
            num = yield num
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

get_successive_primes(iterations=5)
