def simple_generator():
    while True:
        yield 1
        yield 2
        yield 3

print 'accesing values in the generator one by one...'
generator = simple_generator()
print next(generator)
print next(generator)
print next(generator)
print next(generator)
print next(generator)
print next(generator)

print 'calling generator function in a loop...'
for value in simple_generator():
    print(value)
