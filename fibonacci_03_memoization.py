# Implementing Memoization in An recursive function to improve performance
# reference https://towardsdatascience.com/memoization-in-python-57c0a738179a

fibonacci_cache = {}


def fibonacci(num):
    if num in fibonacci_cache:
        return fibonacci_cache[num]
    if num == 1:
        value = 1
    elif num == 2:
        value = 1
    elif num > 2:
        value = fibonacci(num - 1) + fibonacci(num - 2)
    fibonacci_cache[num] = value
    return value


for i in range(1, 201):
    print("fibonacci({}) = ".format(i), fibonacci(i))
