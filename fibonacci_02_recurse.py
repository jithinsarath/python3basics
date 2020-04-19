#implemented using recursion
def fibonacci(num):
    ret_val = 0
    if num == 0:
        ret_val = 0
    elif num == 1:
        ret_val = 1
    else:
        ret_val = fibonacci(num-1) + fibonacci(num-2)

    return ret_val

for i in range(1, 201):
     print("fibonacci({}) = ".format(i), fibonacci(i))