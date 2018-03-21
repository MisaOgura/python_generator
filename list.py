print 'converting a list to an iterator...'
ls = [1,2,3] # list is iterable but not iterators!
print next(iter(ls))
