

def is_even(n):
    return n%2==0



nums = [3,2,4,6,8,9,5]

even = list(filter(is_even,nums))

print (even)