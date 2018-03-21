def simple_generator():
    yield 1
    yield 2
    yield 3

# how to use the generator function 1
print 'calling generator function...'
for value in simple_generator():
    print(value)

# how to use the generator function 2
print 'calling generator function...'
generator = simple_generator()
print next(generator)
print next(generator)
print next(generator)
print next(generator) # generator has been exhausted -> StopIteration
