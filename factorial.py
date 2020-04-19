from sys import setrecursionlimit
# The recursion limit by default is 10^4, which will fail if you do a 1000!. We are using this to set it to a higher value
setrecursionlimit(10**6)


def factorial(num):
    return_value = 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return_value = factorial(num-1)*num
    return return_value


for i in range(2000):
     print("factorial({}) = ".format(i), factorial(i))
