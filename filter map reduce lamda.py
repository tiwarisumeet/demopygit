

#filter using labda
#nums = [3,2,4,6,8,9,5]

#evens = list(filter(lambda n : n%2==0,nums))

#print (evens)

# to reduce out of chunk we use map

#nums = [3,2,4,6,8,9,5]

#evens = list(filter(lambda n : n%2==0,nums))
#doubles = list(map(lambda n : n*2,evens))

#print (doubles)

#reduce the values, instead having multiple value we will have only one value, lets add all values using reduce
from functools import reduce
def add_all(a,b):
    return a+b

nums = [3,2,4,6,8,9,5]

evens = list(filter(lambda n : n%2==0,nums))
doubles = list(map(lambda n : n*2,evens))
print(doubles)

sum = reduce(lambda a,b : a+b, doubles)


print (sum)
