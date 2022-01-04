pos = -1    # global variable , this will help in finding where the psition of found value


def search(list, n):
    i = 0

    while i<len(list):
        if list[i] == n:
           globals()['pos'] = i             # here i will reserve position of pos, Local variable, but we have to make it global using globals to access o/s
           return True
        i = i +1

    return False


list = [5,6,4,8,9,2]
n = 9
if search(list,n):
    print("Found at ", pos)
else:
    print("Not found")
